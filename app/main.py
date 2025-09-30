from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
import uvicorn
from app import retrieval, generator

app = FastAPI(title='RAG Medical QA')

class QARequest(BaseModel):
    question: str
    k: Optional[int] = 3

class QAResponse(BaseModel):
    answer: str
    sources: List[str]

@app.post('/qa', response_model=QAResponse)
async def qa(req: QARequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail='Question is empty')
    docs = retrieval.retrieve(req.question, top_k=req.k)
    # docs is list of (doc_id, text, score)
    passages = [d[1] for d in docs]
    answer = generator.generate_answer(req.question, passages)
    sources = [str(d[0]) for d in docs]
    return {'answer': answer, 'sources': sources}

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
