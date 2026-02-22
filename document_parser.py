from utils.embeddings import generate_embedding
from utils.db import get_connection


def save_document(filename, text):
    chunks = chunk_text(text)

    conn = get_connection()
    cur = conn.cursor()

    for chunk in chunks:
        embedding = generate_embedding(chunk)

        cur.execute(
            "INSERT INTO documents (content, embedding, source) VALUES (%s, %s, %s)",
            (chunk, embedding, filename)
        )

    conn.commit()
    cur.close()
    conn.close()
