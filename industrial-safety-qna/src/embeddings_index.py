# embeddings_index.py
import os
import sqlite3
import numpy as np
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

DB_PATH = "../db/chunks.db"
FAISS_PATH = "../db/faiss_index.bin"
EMB_DIM = 384  # all-MiniLM-L6-v2 dim
MODEL_NAME = "all-MiniLM-L6-v2"
SEED = 42
np.random.seed(SEED)

def load_chunks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT chunk_id, chunk_text FROM chunks")
    rows = c.fetchall()
    conn.close()
    return rows

def build_index():
    model = SentenceTransformer(MODEL_NAME)
    rows = load_chunks()
    ids = []
    embeddings = []
    for chunk_id, text in tqdm(rows, desc="Embedding chunks"):
        emb = model.encode(text, show_progress_bar=False)
        embeddings.append(emb)
        ids.append(chunk_id)
    matrix = np.vstack(embeddings).astype('float32')
    index = faiss.IndexFlatIP(EMB_DIM)  # inner-product on normalized vectors -> cosine
    faiss.normalize_L2(matrix)
    index.add(matrix)
    faiss.write_index(index, FAISS_PATH)
    # save mapping chunk_id -> row index
    np.save("../db/ids.npy", np.array(ids))
    print("FAISS index saved to", FAISS_PATH)

if __name__ == "__main__":
    build_index()
