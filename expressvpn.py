import requests
from bs4 import BeautifulSoup
from agno.agent import Agent

# ----------------- Fetch Web Page Content -----------------
def fetch_webpage_text(url):
    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove scripts and styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = " ".join(soup.stripped_strings)
    return text

# ----------------- Knowledge Base -----------------
knowledge = [
    "Systematic Investment Plan (SIP) allows you to invest a fixed amount regularly in mutual funds.",
    "Diversification means spreading investments across different asset classes and sectors to reduce risk.",
    "Emergency funds should cover at least 3 to 6 months of living expenses.",
    "Long-term investing focuses on fundamentals such as revenue growth, profitability, and competitive advantage."
]

# ----------------- Add ExpressVPN Help Pages -----------------
expressvpn_urls = [
    "https://www.expressvpn.com/support/troubleshooting/",
    "https://www.expressvpn.com/support/vpn-setup/",
    "https://www.expressvpn.com/support/general-troubleshooting/",
]

for url in expressvpn_urls:
    try:
        content = fetch_webpage_text(url)
        knowledge.append(content)
        print(f"✅ Added knowledge from: {url}")
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")

# ----------------- Synonyms -----------------
synonyms = {
    "sip": "systematic investment plan",
    "vpn": "virtual private network",
    "etf": "exchange traded fund",
    "nav": "net asset value",
}

# ----------------- Stopwords -----------------
stopwords = {"is", "the", "of", "and", "a", "an", "to", "with", "for", "in", "on", "by", "what", "who", "how", "do", "i", "need", "does", "means", "explain", "tell", "me"}

# ----------------- Smart Search Function -----------------
def normalize_question(question):
    q = question.lower()
    for short, full in synonyms.items():
        if short in q:
            q = q.replace(short, full)
    return q

def answer_from_knowledge(question):
    question = normalize_question(question)
    question_words = {w.lower().strip("?.!,") for w in question.split() if w.lower() not in stopwords}

    best_match = None
    max_overlap = 0

    for fact in knowledge:
        fact_words = {w.lower().strip("?.!,") for w in fact.split() if w.lower() not in stopwords}
        overlap = len(question_words & fact_words)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = fact

    return best_match if best_match else "I don't know."

# ----------------- Agent Wrapper -----------------
agent = Agent(
    instructions="You are a finance advisor agent. Answer ONLY using the knowledge base. If the answer is not found, say 'I don't know.'",
    markdown=True,
)

# ----------------- Queries -----------------
print(answer_from_knowledge("What is SIP?"))
print(answer_from_knowledge("Why should I use a VPN?"))
print(answer_from_knowledge("How much emergency fund should I have?"))
print(answer_from_knowledge("How do I troubleshoot ExpressVPN connection issues?"))
