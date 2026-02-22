from agno.agent import Agent
from knowledge_store import search_articles

class VPNAgent(Agent):
    def run(self, input, **kwargs):
        results = search_articles(input, domain="vpn")
        if results:
            context = ""
            for title, content in results:
                context += f"{title}: {content}\n\n"
            self.context = context
        return super().run(input, **kwargs)

vpn_agent = Agent(
    name="VPNAgent",
    description="Handles ExpressVPN and VPN-related support questions.",
    instructions="Use ExpressVPN knowledge base to answer accurately."
)
