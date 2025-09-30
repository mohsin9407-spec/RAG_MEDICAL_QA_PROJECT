# RAG-powered Q&A for Medical Reports (Project Scaffold)

This is a starter project scaffold for a Retrieval-Augmented Generation (RAG) system
tailored to question-answering over medical reports. It includes:

- FastAPI application for a simple QA endpoint
- Embeddings generation using sentence-transformers
- FAISS-based vector store for retrieval
- A simple "generator" placeholder to integrate with an LLM (eg. OpenAI/GPT or local LLM)
- Prompt templates and example data
- Dockerfile, requirements, and usage instructions

**Important:** This scaffold is a template. For production use you must:
- Replace the generator with a real LLM call (OpenAI, local Llama, etc.) and handle keys securely.
- Add proper data privacy, encryption, and access controls for medical data.
- Validate, test, and evaluate retrieval + generation rigorously to avoid hallucinations.

## Quick start (local)
1. Create a Python environment (Python 3.10+ recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Prepare embeddings & FAISS index:
   ```bash
   python scripts/create_embeddings_and_index.py --input data/sample_reports.csv
   ```
3. Run the API:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Query the QA endpoint (example):
   ```bash
   curl -X POST "http://127.0.0.1:8000/qa" -H "Content-Type: application/json" -d '{"question":"What does the MRI show?", "k":3}'
   ```

## Project structure
- app/: FastAPI app
- embeddings/: scripts to create embeddings and faiss index
- data/: example reports
- prompts/: prompt templates
- docker/: Dockerfile & docker-compose examples
