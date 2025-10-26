from google.adk.agents.llm_agent import Agent
import os

# Initialize the root agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='financial_agent',
    description='A helpful assistant for user financial guidance.',
    instruction='Answer user questions to the best of your knowledge about financial matters and create plans for them to achieve financial goals.',
)

# Helper function for mock responses in development
def run_agent(prompt: str):
    if os.environ.get("ENV", "development") == "development":
        # Mock responses for testing
        if "savings" in prompt.lower():
            return {"text": "A detailed savings plan requires X, Y, and Z. Start by creating a 50/30/20 budget."}
        return {"text": f"Agent processing: '{prompt}'. Providing detailed financial advice."}
    else:
        # Call the real agent synchronously
        response = root_agent.run_live({"input": prompt})
        # run_live returns a dict with 'output' containing text
        return {"answer": response.get("output", "")}

# Optional test block
if __name__ == "__main__":
    prompts = [
        "How should I save money?",
        "Give me financial advice about investing in stocks."
    ]
    for p in prompts:
        resp = run_agent(p)
        print(f"Prompt: {p}\nResponse: {resp['text']}\n")
