from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.main import run_rag  # your RAG pipeline
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Allow Gradio frontend to access it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    answer, chunks_info = run_rag(query.question)
    return {"answer": answer, "chunks": chunks_info}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)