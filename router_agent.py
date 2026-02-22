from agno.agent import Agent

class RouterAgent(Agent):
    def run(self, input, **kwargs):
        text = input.lower()

        if any(word in text for word in ["sip", "investment", "mutual fund", "stock", "tax", "loan"]):
            return "ROUTE: finance"

        if any(word in text for word in ["vpn", "expressvpn", "server", "privacy", "streaming", "location"]):
            return "ROUTE: vpn"

        return "ROUTE: unknown"

router_agent = RouterAgent(
    name="RouterAgent",
    description="Routes queries to the correct specialist agent.",
    instructions="Return only ROUTE: finance, ROUTE: vpn, or ROUTE: unknown."
)
