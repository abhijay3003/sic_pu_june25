# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from baseline_search import search
from reranker_hybrid import score_candidates
import sqlite3

app = FastAPI()
ABSTAIN_THRESHOLD = 0.35  # if top reranked score < threshold, abstain

class AskRequest(BaseModel):
    q: str
    k: int = 5
    mode: str = "hybrid"  # options: baseline, hybrid

@app.post("/ask")
def ask(req: AskRequest):
    q = req.q
    k = req.k
    mode = req.mode
    baseline_results = search(q, k=max(k, 20))  # retrieve many, then rerank to get top k
    if mode == "baseline":
        contexts = baseline_results[:k]
        reranker_used = "none"
    else:
        reranked = score_candidates(q, baseline_results)
        contexts = reranked[:k]
        reranker_used = "hybrid"
    # Decide answer: extract short extractive answer from top context(s)
    if len(contexts) == 0 or (mode != "baseline" and contexts[0]['reranked_score'] < ABSTAIN_THRESHOLD):
        return {
            "answer": None,
            "contexts": [],
            "reranker_used": reranker_used
        }
    # Build a short answer: pick up to 2 top chunks and return concatenated 1-2 sentence extract
    top = contexts[:2]
    # simple extractive answer: take first 250 chars of top chunk(s)
    answer_text = " ".join([c['text'][:400].strip() for c in top])
    contexts_out = []
    for c in contexts:
        contexts_out.append({
            "chunk_id": c['chunk_id'],
            "score": c.get('reranked_score', c['score']),
            "text": c['text'],
            "title": c['title'],
            "url": c['url']
        })
    return {
        "answer": answer_text,
        "contexts": contexts_out,
        "reranker_used": reranker_used
    }
