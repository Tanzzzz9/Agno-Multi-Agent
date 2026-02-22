import sqlite3

DB_NAME = "knowledge.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_article(title: str, content: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO articles (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    conn.close()


def search_articles(query: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Simple full-text LIKE search
    cursor.execute(
        "SELECT title, content FROM articles WHERE content LIKE ?",
        (f"%{query}%",)
    )
    results = cursor.fetchall()
    conn.close()
    return results
