🧑‍⚕️ RAG-powered Q&A for Medical Reports

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange.svg)](https://faiss.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

🚀 Retrieval-Augmented Generation (RAG) system designed for **question-answering over medical reports**.  
This project uses **FAISS for retrieval**, **sentence-transformers for embeddings**, and a simple FastAPI app for Q&A.

---

## 📂 Project Structure

RAG_medical_qa_project/
│── app/
│ ├── main.py # FastAPI app
│ ├── retrieval.py # FAISS retrieval
│ ├── generator.py # Simple text generator (LLM placeholder)
│ └── embeddings/ # FAISS index + metadata
│
│── scripts/
│ └── create_embeddings_and_index.py # Build embeddings + index
│
│── data/
│ └── sample_reports.csv # Example dataset
│
│── prompts/
│ └── prompt_template.md # Conservative QA prompt
│
│── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
│
│── requirements.txt
│── README.md
│── LICENSE

yaml
Copy code

---

## ⚡ Quick Start

### 1️⃣ Setup environment
```bash
git clone https://github.com/<mohsin9407-spec>/<RAG_MEDICAL_QA_PROJECT>.git
cd RAG_medical_qa_project

python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
2️⃣ Build embeddings & FAISS index
bash
Copy code
python scripts/create_embeddings_and_index.py --input data/sample_reports.csv
3️⃣ Run the API
bash
Copy code
uvicorn app.main:app --reload --port 8000
Visit 👉 http://127.0.0.1:8000/docs to test.

🧪 Example Query
bash
Copy code
curl -X POST "http://127.0.0.1:8000/qa" \
  -H "Content-Type: application/json" \
  -d '{"question": "What does the MRI show?", "k": 2}'
Response:

json
Copy code
{
  "answer": "MRI brain shows no acute intracranial hemorrhage. Mild chronic microvascular ischemic changes.",
  "sources": ["1"]
}
🐳 Run with Docker
bash
Copy code
docker-compose -f docker/docker-compose.yml up --build
📌 Features
✅ Retrieval-Augmented Q&A over structured medical reports

✅ FAISS vector database for fast similarity search

✅ Embeddings powered by sentence-transformers

✅ FastAPI REST API with Swagger docs (/docs)

✅ Docker-ready deployment

🔮 Roadmap
 Replace placeholder generator with real OpenAI GPT / Llama 2 / Mistral

 Add Streamlit frontend for user-friendly interaction

 Add evaluation metrics (precision/recall, hallucination detection)

📜 License
This project is licensed under the MIT License.

⚠️ Disclaimer: This project uses only synthetic/dummy medical text.  
It is for educational and research purposes only — **not for clinical or diagnostic use**.
