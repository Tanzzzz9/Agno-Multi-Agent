from agno.agent import Agent
from agno.tools.nano_banana import NanoBananaTools
from agno.models.groq import Groq

finance_image_agent = Agent(
    name="Finance Image Generator",
    description="Generates finance-related images and dashboards",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[NanoBananaTools()],
)
