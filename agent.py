from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector

knowledge = Knowledge(
    vector_db=PgVector(
        table_name="documents",
        db_url="postgresql+psycopg://postgres:Sudha123@localhost:5433/postgres",
    ),
)

knowledge.insert(url="Personal finance guide.txt")
