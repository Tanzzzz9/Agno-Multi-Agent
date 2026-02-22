from agno.agent import Agent
from knowledge_store import search_articles

class FinanceAgent(Agent):
    def run(self, input, **kwargs):
        results = search_articles(input, domain="finance")
        if results:
            context = ""
            for title, content in results:
                context += f"{title}: {content}\n\n"
            self.context = context
        return super().run(input, **kwargs)


fin_agent = FinanceAgent(
    name="FinanceAgent",
    description="Handles finance and investment-related questions.",
    instructions="Use finance knowledge base to answer accurately."
)
