from agno.agent import Agent
from agno.models.groq import Groq
from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI
from agno.guardrails import PIIDetectionGuardrail, PromptInjectionGuardrail, OpenAIModerationGuardrail, BaseGuardrail
from agno.exceptions import InputCheckError, CheckTrigger
from agno.run.agent import RunInput
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# ----------------------
# Optional Custom Guardrail: block URLs
# ----------------------
class URLGuardrail(BaseGuardrail):
    def check(self, run_input: RunInput) -> None:
        if isinstance(run_input.input_content, str):
            if re.search(r'https?://[^\s]+', run_input.input_content):
                raise InputCheckError(
                    "URLs are not allowed.",
                    check_trigger=CheckTrigger.INPUT_NOT_ALLOWED
                )

    async def async_check(self, run_input: RunInput) -> None:
        # Simply call the sync check inside async
        self.check(run_input)


# ----------------------
# Create Agent with Guardrails
# ----------------------
agent = Agent(
    model=Groq(
        id="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
    ),
    description="You are a personal finance advisor. Only answer finance-related questions. Politely refuse unrelated topics.",
    instructions="Give practical financial advice in simple language. Be concise and helpful.",
    pre_hooks=[                          # Add guardrails here
        PIIDetectionGuardrail(),
        PromptInjectionGuardrail(),
        OpenAIModerationGuardrail(),
        URLGuardrail(),                   # Optional custom guardrail
    ]
)

# ----------------------
# Set up AgentOS with GUI
# ----------------------
agent_os = AgentOS(
    agents=[agent],
    interfaces=[AGUI(agent=agent)],
)

app = agent_os.get_app()

# ----------------------
# Run server
# ----------------------
if __name__ == "__main__":
    agent_os.serve(app="main:app", port=8000, reload=True)
