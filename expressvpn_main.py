from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Finance Advisor Agent Test")

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    return {"response": f"You said: {query.message}"}
