import sqlite3

DB_PATH = "knowledge.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_article(title, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO articles (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def search_articles(query):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT title, content FROM articles WHERE content LIKE ? LIMIT 3",
        (f"%{query}%",)
    )
    results = c.fetchall()
    conn.close()
    return results
