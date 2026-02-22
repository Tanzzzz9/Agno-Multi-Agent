"""
Finance Image Generator Agent using NanoBananaTools + Groq + AgentOS (Agno 2.4.7)

Usage:
- Set your Google API key:
    export GOOGLE_API_KEY="your_google_api_key"
- Set your Groq API key:
    export GROQ_API_KEY="your_groq_api_key"
- Run:
    python test.py
"""

from pathlib import Path
from fastapi import FastAPI
import uvicorn

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.nano_banana import NanoBananaTools
from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

# -------------------- AGENT SETUP --------------------

finance_image_agent = Agent(
    name="Finance Image Generator",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[NanoBananaTools()],
    instructions=[
        "You are a finance visualization expert.",
        "Generate clear, professional finance-related images.",
        "Examples: stock charts, investment growth graphs, budgeting visuals, fintech dashboards.",
        "Ensure images look realistic, clean, and suitable for presentations or reports.",
    ],
    markdown=True,
)

# -------------------- AGENTOS SETUP --------------------

agent_os = AgentOS(
    agents=[finance_image_agent],
    interfaces=[AGUI(agent=finance_image_agent)],
)

app = agent_os.app  # This exposes the AgentOS API

# -------------------- OPTIONAL: LOCAL TEST --------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Finance Image Generator AgentOS Server Running")
    print("=" * 60)

    # Example test generation (runs once on startup)
    response = finance_image_agent.run(
        "Generate a professional stock market growth chart showing long-term investment returns.",
        markdown=True,
    )

    if response.images and response.images[0].content:
        output_path = Path("finance_generated_image.png")
        with open(output_path, "wb") as f:
            f.write(response.images[0].content)
        print(f"✅ Image generated and saved to: {output_path}")
    else:
        print("⚠️ No image returned in response.")

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
