import sqlite3

DB_PATH = "knowledge.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
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

def insert_article(title, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO articles (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    conn.close()

def get_all_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM articles")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_articles(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT title, content FROM articles WHERE content LIKE ?",
        (f"%{query}%",)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
