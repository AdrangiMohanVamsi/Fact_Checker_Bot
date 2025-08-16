# AI Fact-Checker Bot

This project is an intelligent fact-checking bot that uses advanced AI techniques including prompt chaining, web search capabilities, and structured reasoning to verify claims and provide accurate information.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY="YOUR_API_KEY"
     ```

## Usage

### Command-Line Interface (CLI)

To use the CLI, run the following command:

```bash
python main.py --ui cli
```

You will be prompted to enter a claim to fact-check. The bot will then provide a detailed analysis of the claim, including an initial response, assumptions, verified assumptions, evidence, a synthesized summary of the evidence, and a final answer.

### Streamlit UI

To use the Streamlit UI, run the following command:

```bash
python main.py --ui streamlit
```

This will launch a web-based interface where you can enter a claim and view the fact-checking results in a structured way.

## Project Structure

```
fact_checker_bot/
├── src/
│   ├── __init__.py
│   ├── fact_checker.py         # Main fact-checking logic
│   ├── prompt_chains.py        # Prompt templates and chains
│   ├── search_tools.py         # Web search integration
│   ├── credibility_assessment.py # Source credibility assessment
│   └── utils.py                # Helper functions
├── ui/
│   ├── streamlit_app.py        # Streamlit interface
│   ├── gradio_app.py           # Gradio interface (not implemented)
│   └── cli.py                  # Command-line interface (not implemented)
├── config/
│   ├── prompts.yaml            # Prompt templates
│   └── settings.py             # Configuration settings
├── tests/
│   ├── test_fact_checker.py
│   └── test_search_tools.py
├── examples/
│   ├── example_queries.txt
│   └── demo_notebook.ipynb
├── requirements.txt
├── .env.example
├── README.md
└── main.py                     # Entry point
```
