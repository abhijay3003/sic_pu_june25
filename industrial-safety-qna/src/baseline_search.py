# baseline_search.py
import faiss
import numpy as np
import sqlite3
from sentence_transformers import SentenceTransformer

FAISS_PATH = "../db/faiss_index.bin"
IDS_PATH = "../db/ids.npy"
DB_PATH = "../db/chunks.db"
MODEL_NAME = "all-MiniLM-L6-v2"

def load_data():
    index = faiss.read_index(FAISS_PATH)
    ids = np.load(IDS_PATH)
    conn = sqlite3.connect(DB_PATH)
    return index, ids, conn

def search(query, k=5):
    model = SentenceTransformer(MODEL_NAME)
    q_emb = model.encode(query)
    q_emb = q_emb.astype('float32')
    faiss.normalize_L2(q_emb.reshape(1,-1))
    index, ids, conn = load_data()
    D, I = index.search(q_emb.reshape(1,-1), k)
    results = []
    c = conn.cursor()
    for score, pos in zip(D[0], I[0]):
        chunk_id = int(ids[pos])
        c.execute("SELECT chunk_text, doc_id FROM chunks WHERE chunk_id = ?", (chunk_id,))
        text, doc_id = c.fetchone()
        c.execute("SELECT title, url FROM docs WHERE doc_id = ?", (doc_id,))
        title, url = c.fetchone()
        results.append({
            "chunk_id": chunk_id,
            "score": float(score),
            "text": text,
            "title": title,
            "url": url
        })
    conn.close()
    return results

if __name__ == "__main__":
    q = "What are safe distances for guards?"
    r = search(q, k=5)
    for x in r:
        print(x["score"], x["title"])
