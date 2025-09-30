"""Create embeddings for documents and build a FAISS index.
Usage: python scripts/create_embeddings_and_index.py --input data/sample_reports.csv
"""
import argparse, os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='CSV file with columns: report_id, report_text')
parser.add_argument('--model', default='sentence-transformers/all-MiniLM-L6-v2')
parser.add_argument('--index-out', default='app/embeddings/faiss_index.bin')
parser.add_argument('--meta-out', default='app/embeddings/metadata.csv')
args = parser.parse_args()

df = pd.read_csv(args.input)
model = SentenceTransformer(args.model)
texts = df['report_text'].astype(str).tolist()
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True).astype('float32')

d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)
os.makedirs(os.path.dirname(args.index_out), exist_ok=True)
faiss.write_index(index, args.index_out)
df[['report_id','report_text']].to_csv(args.meta_out, index=False)
print('Index and metadata saved.')