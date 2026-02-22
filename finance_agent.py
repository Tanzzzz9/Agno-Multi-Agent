from agno.agent import Agent
from agno.models.groq import Groq
import os

finance_agent = Agent(
    name="Personal Finance Advisor",
    role="Helps users manage budgets, savings, investments, and financial goals.",
    instructions=[
        "Provide clear, actionable financial advice.",
        "Ask clarifying questions before giving recommendations.",
        "Explain concepts in simple terms.",
        "Never give illegal or unethical financial advice."
    ],
    model=Groq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"
    ),
)
