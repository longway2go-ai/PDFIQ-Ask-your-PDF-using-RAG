# 📄 PDFIQ: Ask your PDF

PDFIQ is a lightweight, interactive PDF reader and QA system built using **Streamlit** and powered by **OpenAI's GPT-4.1-nano** (or any other OpenAI-compatible model). It reads your PDF files and lets you query their content intelligently using custom prompts and a system message to guide model behavior.

---

## 🚀 Features

- ✅ Upload any PDF and extract structured text content
- 🤖 Use **OpenAI GPT-4.1-nano** (or your preferred model) to answer questions about the PDF
- 🧠 Supports a customizable **system prompt** to guide model tone and reasoning
- 🔁 Easily change the PDF and ask new questions dynamically
- 💬 Streaming answers in real-time with **Streamlit** UI
- 🔧 Modular architecture: swap models, prompts, or PDF logic easily

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Frontend and interaction
- [OpenAI Python SDK](https://github.com/openai/openai-python) – Model calls
- [PyMuPDF / fitz](https://pymupdf.readthedocs.io/en/latest/) – PDF parsing
- Python (3.8+)

---

## 🧪 Example Use Case

1. Upload your research paper, contract, or report in PDF form.
2. Enter a custom system prompt (e.g., "Act like a legal assistant").
3. Ask questions like:
   - "What is the conclusion of this paper?"
   - "List all dates and deadlines."
   - "Summarize the methodology in 3 bullet points."
4. Get instant answers from GPT-4.1-nano.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/PDFIQ.git
cd PDFIQ
pip install -r requirements.txt
