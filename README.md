# 📚 PDFIQ : Ask Your PDF 🤖

PDFIQ is a powerful, interactive PDF reader and question-answering system that uses **OpenAI's GPT models** (or any OpenAI-compatible model) and **Qdrant VectorDB** to understand your documents. It parses PDFs into chunks, stores them in a vector database, and retrieves relevant content based on your query using semantic search.


User can give their own PDF file and get the information related to it.

---

## 🚀 Features

- 📂 Upload any PDF and extract structured text automatically
- 🤖 Query document content with **GPT-4.1-nano** or other models
- 🧠 Define a **custom system prompt** to control model behavior
- 🔎 Uses **Qdrant VectorDB** for chunked document storage and fast retrieval
- 🔁 Easily swap PDFs and continue querying
- 💬 Real-time streaming answers with a clean **Streamlit** UI
- 🐳 **Dockerized** vector store for local development and testing

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Frontend UI
- [OpenAI Python SDK](https://github.com/openai/openai-python) – Model integration
- [Qdrant VectorDB](https://github.com/qdrant-ai/vector-db) – Semantic search & storage
- [Docker](https://www.docker.com/) – Isolated vector DB environment
- [PyMuPDF / fitz](https://pymupdf.readthedocs.io/en/latest/) – PDF parsing
- Python (3.8+)

---

## 🧪 Example Workflow

1. **Upload** a PDF document.
2. PDF is **parsed and chunked**, then embedded and stored in **Qdrant VectorDB**.
3. When you **ask a question**, the system:
   - Embeds your query
   - Finds **relevant chunks** using vector similarity
   - Passes the results + your prompt to the **GPT model**
4. GPT returns a **context-aware** response.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PDFIQ.git
cd PDFIQ
