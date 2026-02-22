"""
Simple Financial Chat Agent with AgentOS
"""

import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.runner.agentos import AgentOS

# Groq API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set GROQ_API_KEY environment variable")

# Initialize Groq model
groq_model = Groq(
    id="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.1,
)

# Create Financial Chat Agent
financial_agent = Agent(
    name="Financial Analyst",
    model=groq_model,
    role="Expert financial analyst and advisor",
    instructions=[
        "You are a professional financial analyst with expertise in:",
        "- Company financial analysis and valuation",
        "- Market research and sector analysis", 
        "- Investment strategy and portfolio management",
        "- Risk assessment and financial planning",
        "- Explaining complex financial concepts in simple terms",
        "",
        "Always:",
        "1. Provide accurate, data-driven analysis",
        "2. Include specific metrics when possible",
        "3. Highlight risks and limitations",
        "4. Format responses clearly with markdown",
        "5. Use tables for comparison data",
        "6. Be professional but approachable",
    ],
    markdown=True,
)

# Create AgentOS app
app = AgentOS(
    name="Financial Analyst",
    description="AI-powered financial analysis assistant",
    agents=[financial_agent],
)

if __name__ == "__main__":
    print("🚀 Starting Financial Analyst Agent...")
    print("🌐 Open: http://localhost:8080")
    app.run()