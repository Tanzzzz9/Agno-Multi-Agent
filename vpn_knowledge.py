from knowledge_store import search_articles

def vpn_retriever(query):
    return search_articles(query, domain="vpn")
