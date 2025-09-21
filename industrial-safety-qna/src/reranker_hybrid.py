# reranker_hybrid.py
# Hybrid reranker: combine FAISS vector score + BM25 keyword score + title match feature
import numpy as np
import sqlite3
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from baseline_search import load_data
from sklearn.linear_model import LogisticRegression
import json
import re

DB_PATH = "../db/chunks.db"
MODEL_NAME = "all-MiniLM-L6-v2"

def simple_tokenize(s):
    return re.findall(r"\w+", s.lower())

def build_bm25():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT chunk_id, chunk_text FROM chunks")
    rows = c.fetchall()
    conn.close()
    id2text = {r[0]: r[1] for r in rows}
    corpus = [simple_tokenize(t) for t in id2text.values()]
    ids = list(id2text.keys())
    bm25 = BM25Okapi(corpus)
    return bm25, ids, id2text

def score_candidates(query, candidates):
    # candidates: list of dicts with chunk_id, score (vector), text, title, url
    bm25, bm25_ids, id2text = build_bm25()
    tokq = simple_tokenize(query)
    bm25_scores_all = bm25.get_scores(tokq)
    # create feature vector: [vec_score, bm25_score, title_match]
    feats = []
    for c in candidates:
        chunk_id = c['chunk_id']
        # bm25 score: need index of chunk in bm25_ids
        try:
            idx = bm25_ids.index(chunk_id)
            bm_score = float(bm25_scores_all[idx])
        except ValueError:
            bm_score = 0.0
        title_match = 1.0 if query.lower() in (c['title'] or '').lower() else 0.0
        feats.append([c['score'], bm_score, title_match])
    feats = np.array(feats, dtype=float)
    # simple learned weights (tiny logistic reg trained on a few hand-labeled examples) OR fallback heuristic:
    # For the purpose of this assessment we provide a simple linear weighting:
    # combined_score = 0.6 * vec_norm + 0.4 * bm25_norm + 0.1*title_match (then normalized)
    # normalize features
    def norm(x):
        if x.max() - x.min() < 1e-6:
            return x
        return (x - x.min()) / (x.max() - x.min())
    v = norm(feats[:,0])
    b = norm(feats[:,1])
    t = feats[:,2]  # 0 or 1
    combined = 0.6 * v + 0.35 * b + 0.05 * t
    # attach new score
    for i, c in enumerate(candidates):
        c['reranked_score'] = float(combined[i])
    # sort
    candidates = sorted(candidates, key=lambda x: x['reranked_score'], reverse=True)
    return candidates

if __name__ == "__main__":
    # quick demo: run baseline top-20 then rerank
    from baseline_search import search
    q = "How to guard moving parts to prevent amputations?"
    base = search(q, k=20)
    rer = score_candidates(q, base)
    for r in rer[:5]:
        print(r['reranked_score'], r['score'], r['title'])
