import streamlit as st
from fact_checker_bot.src.fact_checker import FactChecker

def main():
    st.title("AI Fact-Checker Bot")

    st.write("Enter a claim to fact-check:")
    query = st.text_input("Claim:")

    if st.button("Fact-Check"):
        if query:
            fact_checker = FactChecker()
            result = fact_checker.check(query)

            st.header("Initial Response")
            st.write(result["initial_response"])

            st.header("Assumptions")
            st.write(result["assumptions"])

            st.header("Verified Assumptions")
            st.write(result["verified_assumptions"])

            st.header("Evidence")
            for i, evidence in enumerate(result["evidence"]):
                st.subheader(f"Evidence {i+1}")
                st.write(f"**Title:** {evidence['title']}")
                st.write(f"**URL:** {evidence['href']}")
                st.write(f"**Snippet:** {evidence['body']}")
                st.write(f"**Credibility:** {evidence['credibility']['score']}/100 - {evidence['credibility']['explanation']}")

            st.header("Synthesized Evidence")
            st.write(result["synthesized_evidence"])

            st.header("Final Answer")
            st.write(result["final_answer"])
        else:
            st.write("Please enter a claim to fact-check.")

if __name__ == "__main__":
    main()
