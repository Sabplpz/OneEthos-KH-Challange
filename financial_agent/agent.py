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
        if any(word in prompt.lower() for word in ["savings", "save", "budget"]):
            return {"text": (
            "Here’s a practical savings plan for you:\n\n"
            "1. **Track Your Expenses:** Review your monthly spending and categorize each expense.\n"
            "2. **50/30/20 Rule:** Allocate 50% of income to necessities, 30% to wants, and 20% to savings.\n"
            "3. **Emergency Fund:** Save at least 3–6 months of living expenses in a separate account.\n"
            "4. **Automate Savings:** Set up automatic transfers to your savings or investment accounts.\n"
            "5. **Review Monthly:** Revisit your budget monthly and adjust for changes in income or expenses.\n\n"
            "Following this plan can help you build financial stability and reach your goals faster."
        )}
        elif any(word in prompt.lower() for word in ["credit score", "credit report", "fico"]):
            return {
                "text": (
                    "Here’s how to improve your credit score:\n"
                    "1. Check your credit report\n"
                    "2. Pay bills on time\n"
                    "3. Keep credit utilization below 30%\n"
                    "4. Avoid opening too many accounts at once\n"
                    "5. Maintain old accounts\n"
                    "6. Dispute errors on your report"
                )
            }
        elif any(word in prompt.lower() for word in ["invest", "stocks", "bonds", "mutual fund","stock","investing"]):
            return {
                "text": (
                    "Investment tips:\n"
                    "1. Diversify your portfolio\n"
                    "2. Consider risk tolerance\n"
                    "3. Invest regularly\n"
                    "4. Keep long-term perspective\n"
                    "5. Research before buying"
                )
            }
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
