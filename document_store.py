import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    content TEXT
)
""")
conn.commit()

def save_document(filename, content):
    cursor.execute(
        "INSERT INTO documents (filename, content) VALUES (?, ?)",
        (filename, content),
    )
    conn.commit()

def search_documents(query):
    cursor.execute(
        "SELECT filename, content FROM documents WHERE content LIKE ?",
        (f"%{query}%",),
    )
    return cursor.fetchall()
