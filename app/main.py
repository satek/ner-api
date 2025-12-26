from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.ner import extract_entities, extract_entities_batch

app = FastAPI(title="spaCy NER API (GPU)")

class NERRequest(BaseModel):
    text: str

class NERBatchRequest(BaseModel):
    texts: List[str]
    batch_size: int = 8

@app.post("/ner")
def ner(req: NERRequest):
    return {"entities": extract_entities(req.text)}

@app.post("/ner/batch")
def ner_batch(req: NERBatchRequest):
    return {
        "results": extract_entities_batch(req.texts, req.batch_size)
    }

