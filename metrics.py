# metrics.py

import sqlite3
from datetime import datetime

DB_FILE = "metrics.db"

def init_metrics_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tool_calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tool_name TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def record_tool_call(tool_name: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tool_calls (tool_name, timestamp) VALUES (?, ?)",
        (tool_name, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
