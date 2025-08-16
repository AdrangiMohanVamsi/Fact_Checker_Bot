import argparse
import sys
import os
from fact_checker_bot.src.fact_checker import FactChecker
import subprocess

# Add the project root to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

def cli_main():
    print("Welcome to the Fact Checker Bot!")
    print("Please make sure you have set your Gemini API key in the .env file.")

    fact_checker = FactChecker()

    while True:
        query = input("Enter your claim to fact-check (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break

        result = fact_checker.check(query)
        print("\n--- Initial Response ---")
        print(result["initial_response"])
        print("\n--- Assumptions ---")
        print(result["assumptions"])
        print("\n--- Verified Assumptions ---")
        print(result["verified_assumptions"])
        print("\n--- Evidence ---")
        for i, evidence in enumerate(result["evidence"]):
            print(f"  {i+1}. {evidence['title']}")
            print(f"     {evidence['href']}")
            print(f"     {evidence['body']}")
            print()
        print("\n--- Final Answer ---")
        print(result["final_answer"])
        print("\n")

def streamlit_main():
    subprocess.run(["python", "-m", "streamlit", "run", "fact_checker_bot/ui/streamlit_app.py"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fact Checker Bot")
    parser.add_argument("--ui", type=str, default="cli", help="UI to use (cli, streamlit)")
    args = parser.parse_args()

    if args.ui == "cli":
        cli_main()
    elif args.ui == "streamlit":
        streamlit_main()
    else:
        print(f"Invalid UI: {args.ui}")
