import sqlite3
from datetime import datetime

DB_PATH = "memory.db"

def init_memory_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            agent_response TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_memory(user_input, agent_response):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO memory (user_input, agent_response, timestamp) VALUES (?, ?, ?)",
        (user_input, agent_response, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def get_recent_memory(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_input, agent_response FROM memory ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
