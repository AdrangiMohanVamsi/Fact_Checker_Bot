import yaml
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from fact_checker_bot.src.search_tools import search
from fact_checker_bot.src.credibility_assessment import assess_credibility

class PromptChainer:
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        with open("fact_checker_bot/config/prompts.yaml", "r") as f:
            self.prompts = yaml.safe_load(f)

    def run(self, claim: str) -> dict:
        # 1. Initial Response
        initial_response_prompt = PromptTemplate(
            template=self.prompts["initial_response_prompt"],
            input_variables=["claim"],
        )
        initial_response_chain = LLMChain(llm=self.llm, prompt=initial_response_prompt)
        initial_response = initial_response_chain.run(claim=claim)

        # 2. Assumption Extraction
        assumption_extraction_prompt = PromptTemplate(
            template=self.prompts["assumption_extraction_prompt"],
            input_variables=["response"],
        )
        assumption_extraction_chain = LLMChain(llm=self.llm, prompt=assumption_extraction_prompt)
        assumptions = assumption_extraction_chain.run(response=initial_response)
        
        # 3. Verification Loop
        verification_prompt = PromptTemplate(
            template=self.prompts["verification_prompt"],
            input_variables=["assumptions"],
        )
        verification_chain = LLMChain(llm=self.llm, prompt=verification_prompt)
        verified_assumptions = verification_chain.run(assumptions=assumptions)

        # 4. Evidence Gathering and Credibility Assessment
        evidence = []
        for assumption in assumptions.split('\n'):
            if assumption.strip():
                search_results = search(assumption.strip())
                for res in search_results:
                    credibility = assess_credibility(res['href'])
                    res['credibility'] = credibility
                    evidence.append(res)

        # 5. Evidence Synthesis
        evidence_synthesis_prompt = PromptTemplate(
            template=self.prompts["evidence_synthesis_prompt"],
            input_variables=["claim", "evidence"],
        )
        evidence_synthesis_chain = LLMChain(llm=self.llm, prompt=evidence_synthesis_prompt)
        synthesized_evidence = evidence_synthesis_chain.run(
            claim=claim,
            evidence=evidence,
        )

        # 6. Final Synthesis
        final_synthesis_prompt = PromptTemplate(
            template=self.prompts["final_synthesis_prompt"],
            input_variables=["claim", "initial_response", "verified_assumptions", "synthesized_evidence"],
        )
        final_synthesis_chain = LLMChain(llm=self.llm, prompt=final_synthesis_prompt)
        final_answer = final_synthesis_chain.run(
            claim=claim,
            initial_response=initial_response,
            verified_assumptions=verified_assumptions,
            synthesized_evidence=synthesized_evidence,
        )

        return {
            "initial_response": initial_response,
            "assumptions": assumptions,
            "verified_assumptions": verified_assumptions,
            "evidence": evidence,
            "synthesized_evidence": synthesized_evidence,
            "final_answer": final_answer,
        }
