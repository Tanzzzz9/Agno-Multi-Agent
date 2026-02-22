from knowledge_store import search_articles

def finance_retriever(query):
    return search_articles(query, domain="finance")
