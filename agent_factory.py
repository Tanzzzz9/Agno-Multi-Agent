# agents/agent_factory.py

import os
from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq

from memory.session_configs import mongo_db
from utils.search import semantic_search
from tools.finance_tools import calculate_emi, calculate_ltcg_india,calculate_sip,calculate_future_value,calculate_cagr,calculate_real_return,calculate_npv,calculate_irr,calculate_fd_maturity,calculate_income_tax_new_regime,apply_section_54_exemption
from tools.charts_tools import generate_tax_slab_chart
from learning.extractor import extract_learning
from learning.storage import store_learning
from metrics import init_metrics_db
init_metrics_db()
print("✅ Metrics DB ready")

from metrics import record_tool_call

def track_tool(tool, name):
    def wrapper(*args, **kwargs):
        record_tool_call(name)
        print(f" Tool used: {name}")
        return tool(*args, **kwargs)
    return wrapper
def get_metrics():
    import sqlite3
    conn = sqlite3.connect("metrics.db")
    cursor = conn.cursor()
    cursor.execute("SELECT tool_name, COUNT(*) FROM tool_calls GROUP BY tool_name")
    data = cursor.fetchall()
    conn.close()
    return data

import agno.tools.pubmed as pubmed

PubmedTools = getattr(pubmed, "PubmedTools")
pubmed_tool = PubmedTools()

print("✅ PubMed tool loaded:", pubmed_tool)

def wrap_with_rag(agent):

    if hasattr(agent, "chat"):
        original_call = agent.chat
        method_name = "chat"
    else:
        original_call = agent.run
        method_name = "run"

    def rag_call(message, *args, **kwargs):

        print(" RAG EXECUTED")

        docs = semantic_search(message)
        context = "\n\n".join(docs) if docs else ""

        if context:
            message = f"""
Use this context to answer.

Context:
{context}

User:
{message}
"""

        response = original_call(message, *args, **kwargs)

        print("AGENT RESPONSE:", response)


        try:
            learning = extract_learning(message, str(response))
            print(" EXTRACTED LEARNING:", learning)

            if learning and learning.strip() != "NONE":
                store_learning(learning)
                print("✅ Learning saved")

        except Exception as e:
            print("Learning error:", e)

        return response

    # Replace correct method dynamically
    if method_name == "chat":
        agent.chat = rag_call
    else:
        agent.run = rag_call

    return agent


def create_medical_agent():
    print("✅ create_medical_agent CALLED")

    agent = Agent(
        name="MedicalAgent",
        model=Groq(
            id="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
        ),
        instructions=dedent("""
        You are a medical assistant.
        Provide educational explanations only.
        Recommend consulting a licensed physician.
        Use PubMed tool when user asks health, disease, or medicine questions.
        Always summarize research clearly.
        """),
        tools=[pubmed_tool],
        markdown=True,
    )
    agent.metrics_db = "metrics.db"
    agent.get_metrics = get_metrics
    return wrap_with_rag(agent)

def create_finance_agent():
    print("✅ create_finance_agent CALLED")

    agent = Agent(
        name="FinanceAgent",
        model=Groq(
            id="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
        ),
        tools=[
            calculate_ltcg_india,
            apply_section_54_exemption,
            calculate_emi,
            calculate_sip,
            calculate_future_value,
            calculate_cagr,
            calculate_real_return,
            calculate_npv,
            calculate_irr,
            calculate_fd_maturity,
           calculate_income_tax_new_regime,
           generate_tax_slab_chart,
        ],
        
        instructions=dedent("""
        You are a finance assistant.
        Help users understand investments, budgeting, markets, and financial planning.
        Provide educational explanations only.Use tools whenever calculations are required.
        Always respond in structured markdown.
        Do not give personalized financial advice.
        You are a financial tax assistant for India.
        You are a financial tax assistant for India.
        For capital gains questions:
        - You MUST use the calculate_ltcg_india tool.
        - You MUST NOT calculate manually.
        - You MUST NOT assume inflation rates.
        - You MUST rely only on Cost Inflation Index values.
        Always return final result clearly in markdown.
        If user asks for:
       - chart
       - graph
       - visual tax slab
       - plot
    You MUST call generate_tax_slab_chart tool.
    Do not explain in text.                    
        """),
        markdown=True,

    )
    agent.metrics_db = "metrics.db"
    agent.get_metrics = get_metrics
    return wrap_with_rag(agent)

def create_legal_agent():
    print("✅ create_legal_agent CALLED")

    agent = Agent(
        name="LegalAgent",
        model=Groq(
            id="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
        ),
        instructions=dedent("""
        You are a legal assistant.
        Provide structured legal reasoning.
        Explain laws clearly.
        This is educational information, not legal advice.
        
        """),
        markdown=True,
    )
    agent.metrics_db = "metrics.db"
    agent.get_metrics = get_metrics
    return wrap_with_rag(agent)
