from langchain_google_genai import ChatGoogleGenerativeAI
from fact_checker_bot.config import settings
from fact_checker_bot.src.prompt_chains import PromptChainer

class FactChecker:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=settings.GEMINI_API_KEY,
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_output_tokens=settings.MAX_TOKENS,
        )
        self.prompt_chainer = PromptChainer(self.llm)

    def check(self, query: str) -> dict:
        return self.prompt_chainer.run(query)
