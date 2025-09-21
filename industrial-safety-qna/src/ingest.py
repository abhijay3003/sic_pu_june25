import os
import json
import sqlite3
from pathlib import Path

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import PyPDF2
from tqdm import tqdm  # progress bar

# --------------------------
# CONFIG
# --------------------------
DATA_DIR = Path(__file__).parent.parent / "data" / "sources" # folder where PDFs are stored
DB_PATH = "qna.db"
INDEX_PATH = "faiss.index"
IDMAP_PATH = "id_map.npy"
SOURCES_JSON = "sources.json"
LOG_PATH = "ingest_errors.log"
SUMMARY_PATH = "ingest_summary.txt"

# --------------------------
# LOAD EMBEDDING MODEL
# --------------------------
print("🔹 Loading embedding model (MiniLM-L6-v2)...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# --------------------------
# HELPERS
# --------------------------
def log_error(msg):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(msg + "\n")

def read_pdf(path):
    """Extract raw text from a PDF file"""
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if not page_text:
                log_error(f"{path.name} → Page {i+1} has no extractable text.")
            text += page_text or ""
    return text

def chunk_text(text, chunk_size=200, overlap=30):
    """Split text into overlapping word chunks"""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap
    return chunks

# --------------------------
# MAIN INGEST
# --------------------------
def main():
    # Load sources.json (title + url mapping)
    print("🔹 Loading sources.json...")
    with open(SOURCES_JSON, "r", encoding="utf-8") as f:
        sources = {s["title"]: s["url"] for s in json.load(f)}

    # Setup SQLite
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS docs")
    c.execute("CREATE TABLE docs (id INTEGER PRIMARY KEY, text TEXT, source TEXT, url TEXT)")

    all_chunks = []
    all_sources = []
    id_map = []
    total_chunks = 0
    total_pdfs = 0
    skipped_pdfs = 0

    # Process each PDF
    pdf_files = list(DATA_DIR.glob("*.pdf"))
    for pdf_file in tqdm(pdf_files, desc="📄 Processing PDFs"):
        total_pdfs += 1
        text = read_pdf(pdf_file)
        word_count = len(text.split())

        if word_count < 50:
            log_error(f"Skipped {pdf_file.name} — too little text ({word_count} words)")
            skipped_pdfs += 1
            continue

        chunks = chunk_text(text)
        if not chunks:
            log_error(f"Skipped {pdf_file.name} — no chunks generated")
            skipped_pdfs += 1
            continue

        source_title = next((s for s in sources if pdf_file.stem.lower() in s.lower()), pdf_file.stem)
        source_url = sources.get(source_title, "")
        if not source_url:
            log_error(f"No matching source URL for {pdf_file.name}")

        for chunk in chunks:
            c.execute("INSERT INTO docs (text, source, url) VALUES (?, ?, ?)", (chunk, source_title, source_url))
            doc_id = c.lastrowid
            all_chunks.append(chunk)
            all_sources.append(doc_id)

        total_chunks += len(chunks)

    conn.commit()
    conn.close()

    if total_chunks == 0:
        print("⚠️ No chunks found. Did you put PDFs in data/sources/?")
        return

    # Batch embedding
    print("\n🔹 Embedding all chunks...")
    embeddings = model.encode(all_chunks, convert_to_numpy=True, normalize_embeddings=True)

    # Build FAISS index
    print("🔹 Building FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    np.save(IDMAP_PATH, np.array(all_sources))

    # Write summary
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write(f"PDFs processed: {total_pdfs}\n")
        f.write(f"PDFs skipped: {skipped_pdfs}\n")
        f.write(f"Total chunks: {total_chunks}\n")
        f.write(f"SQLite DB: {DB_PATH}\n")
        f.write(f"FAISS index: {INDEX_PATH}\n")
        f.write(f"ID map: {IDMAP_PATH}\n")

    print("\n✅ Ingestion complete!")
    print(f"   PDFs processed : {total_pdfs}")
    print(f"   PDFs skipped   : {skipped_pdfs}")
    print(f"   Total chunks   : {total_chunks}")
    print(f"   SQLite DB      : {DB_PATH}")
    print(f"   FAISS index    : {INDEX_PATH}")
    print(f"   ID map         : {IDMAP_PATH}")
    print(f"   Summary report : {SUMMARY_PATH}")
    print(f"   Error log      : {LOG_PATH}")

if __name__ == "__main__":
    main()