#Project Title: 
Agno Multi Agent System

##Overview
This project is a Multi-Agent AI System built using the Agno Framework that brings together specialized Finance, Legal, and Medical AI agents into a single orchestration workflow. Each agent is designed to handle domain-specific queries while collaborating to provide accurate and context-aware responses.
The system leverages modern AI technologies, including Agno Framework, Python, Groq (Llama models), PostgreSQL, pgvector, and Vector Databases to enable intelligent reasoning, semantic search, and efficient knowledge retrieval.

##Tech Stack
Agno Framework – Multi-agent orchestration
Python – Backend development
Groq (Llama Models) – Large Language Model inference
PostgreSQL – Data storage
pgvector / Vector Database – Semantic search and embeddings
AI APIs – Domain-specific response generation
#Features
Multiple AI agents- Finance, Legal, Medical 
Agent collaboration
Memory
Knowledge Base
Metrics
Finance analysis

##Architecture 
User
   │
   ▼
FastAPI Backend
   │
   ▼
Agno Team
├── Finance Agent
├── Technical Agent
├── News/Sentiment Agent
└── Coordinator
   │
   ▼
Memory + Knowledge + Database

Prerequisites

Python version:
PostgreSQL
pgvector
Groq API Key

Installation

Step 1

git clone https://github.com/Tanzzzz9/Agno-Multi-Agent.git

Step 2

cd Agno-Multi-Agent

Step 3

python -m venv .venv

Step 4

source .venv/bin/activate

Windows

.venv\Scripts\activate

Step 5

pip install -r requirements.txt

Environment Variables
Create a .env file.

Example:

GROQ_API_KEY=
OPENAI_API_KEY=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
Database Setup
Install PostgreSQL
Enable pgvector
Create database
Run migration/setup

Running the Backend

uvicorn app:app --reload

Running the Frontend (if any)

npm install
npm run dev
How it Works
User asks a finance question.
Coordinator receives the request.
Appropriate agents are selected.
Agents search knowledge/memory.
Results are combined.
Final answer is returned.

Project Structure

Agno-Multi-Agent/
├── agents/
├── knowledge/
├── memory/
├── storage/
├── api/
├── frontend/
├── data/
├── requirements.txt
├── .env.example
└── README.md

#Technologies
Python
FastAPI
Agno
Groq
PostgreSQL
pgvector
Next.js
Tailwind CSS
