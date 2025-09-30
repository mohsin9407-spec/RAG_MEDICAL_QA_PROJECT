import os, numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INDEX_PATH = os.path.join(BASE_DIR, 'embeddings', 'faiss_index.bin')
META_PATH = os.path.join(BASE_DIR, 'embeddings', 'metadata.csv')
MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

_model = None
_index = None
_meta = None

def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def _load_index():
    global _index, _meta
    if _index is None:
        if not os.path.exists(INDEX_PATH):
            raise FileNotFoundError('FAISS index not found. Run the creation script in /scripts.')
        _index = faiss.read_index(INDEX_PATH)
        _meta = pd.read_csv(META_PATH)
    return _index, _meta

def retrieve(question, top_k=3):
    model = _load_model()
    index, meta = _load_index()
    q_emb = model.encode(question, convert_to_numpy=True)
    q_emb = np.array([q_emb]).astype('float32')
    scores, ids = index.search(q_emb, top_k)
    results = []
    for sc, idx in zip(scores[0], ids[0]):
        row = meta.iloc[idx]
        results.append((row['report_id'], row['report_text'], float(sc)))
    return results
