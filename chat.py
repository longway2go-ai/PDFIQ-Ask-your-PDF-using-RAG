import os
import tempfile
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Qdrant as QdrantVectorStore
from langchain.chains import RetrievalQA
from qdrant_client import QdrantClient

# 🌟 Page configuration
st.set_page_config(page_title="📘 Chat With PDF", layout="wide")

# 💄 Styling
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-bottom: 0;
        }
        .subtitle {
            font-size: 18px;
            color: #333;
            text-align: center;
            margin-top: 0;
        }
        footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: #888;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# 📌 Header
st.markdown('<div class="title">📚 PDFIQ : Ask Your PDF 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a PDF 📄 | Ask questions ❓ | Get instant answers ⚡</div>', unsafe_allow_html=True)
st.markdown("---")

# 📤 File uploader
uploaded_file = st.file_uploader("📎 Upload a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # 1. Load PDF
    loader = PyPDFLoader(tmp_path)
    pages = loader.load()

    # 2. Split text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = text_splitter.split_documents(pages)

    # 3. Embed
    embedding = OpenAIEmbeddings(api_key=st.secrets["OPENAI_API_KEY"])

    # 4. Set up Qdrant (ephemeral client)
    qdrant_client = QdrantClient(":memory:")  # In-memory for now, or use file/db-backed

    # 5. Store embeddings
    vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    embedding=embedding,
    url="http://localhost:6333",
    collection_name="uploaded_pdf",
    force_recreate=True  # 🔄 This will overwrite if it already exists
)

    st.success("✅ PDF indexed. Ask your question!")

    # 6. Query input
    query = st.text_input("Ask a question:")

    if query:
        retriever = vector_store.as_retriever()
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=st.secrets["OPENAI_API_KEY"])
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        result = qa.run(query)
        st.markdown("### 🤖 Answer")
        st.success(result)

# 🧠 Footer
st.markdown("<footer>✨ Created with ❤️ by Arnab</footer>", unsafe_allow_html=True)
