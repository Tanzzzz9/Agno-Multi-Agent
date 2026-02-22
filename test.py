# test.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import psycopg
import os
import sys
import io
from pypdf import PdfReader
from guardrails import agent, agent_os, app
import agno.tools.pubmed as pubmed

PubmedTools = getattr(pubmed, "PubmedTools")
pubmed_tool = PubmedTools()

# Allow local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent.agent_factory import (
    create_finance_agent,
    create_medical_agent,
    create_legal_agent,
)

from utils.embeddings import generate_embedding

# -------------------- ENV --------------------
load_dotenv()

DATABASE_URL = "postgresql://postgres:Sudha123@localhost:5433/postgres"


finance_agent = create_finance_agent()
medical_agent = create_medical_agent()
legal_agent = create_legal_agent()

base_app = FastAPI(title="Multi-Agent API")

base_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@base_app.get("/")
def root():
    return {"status": "running"}

@base_app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()

        # Extract text
        if file.filename.lower().endswith(".pdf"):
            pdf = PdfReader(io.BytesIO(content))
            content_str = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    content_str += text + "\n"
        else:
            content_str = content.decode("utf-8", errors="ignore")

        if not content_str.strip():
            return {"error": "File is empty or unreadable"}

        # Generate embedding
        embedding = generate_embedding(content_str)

        # Store in Postgres
        with psycopg.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
                    (content_str, embedding),
                )
            conn.commit()

        return {"message": "Document uploaded and embedded successfully"}

    except Exception as e:
        print("Upload Error:", e)
        return {"error": str(e)}

from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

agent_os = AgentOS(
    agents=[
        finance_agent,
        medical_agent,
        legal_agent,
    ],
    interfaces=[
        AGUI(agent=finance_agent)
    ],
)


app = agent_os.get_app()

app.mount("/api", base_app)
