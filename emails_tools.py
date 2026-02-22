from agno.agent import Agent
from agno.tools.email import EmailTools
from groq import Groq

# -----------------------------
# Email Settings
# -----------------------------
receiver_email = "<receiver_email>"
sender_email = "<sender_email>"
sender_name = "<sender_name>"
sender_passkey = "<sender_passkey>"

# -----------------------------
# Initialize Groq client
# -----------------------------
groq_model = Groq()

# -----------------------------
# Finance Agent Setup
# -----------------------------
finance_agent = Agent(
    name="Finance Advisor",
    description="AI assistant for finance advice and email notifications.",
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
            all=True,
        )
    ]
)

# -----------------------------
# Generate Email Content via Groq
# -----------------------------
prompt = "Generate a friendly finance update email for the client about their portfolio."
email_content = groq_model.generate("llama-3.1-8b-instant", prompt)

# -----------------------------
# Send Email via Agent
# -----------------------------
finance_agent.print_response(
    f"Send an email to the receiver with subject 'Finance Update' and this message:\n\n{email_content}",
    markdown=True
)
