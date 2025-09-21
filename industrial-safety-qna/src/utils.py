# utils.py
import re
from typing import List

def clean_text(s: str) -> str:
    s = s.replace('\r', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def chunk_text(text: str, chunk_size=500, overlap=50) -> List[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(' '.join(chunk))
        i += chunk_size - overlap
    return chunks
