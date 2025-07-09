import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
import os

api_key = ""

if not api_key:
    st.error("⚠️ OPENAI_API_KEY is not set. Please add it to your .env file.")
    st.stop()

# Initialize OpenAI and Qdrant clients
client = OpenAI(api_key=api_key)
embedding = OpenAIEmbeddings(openai_api_key=api_key,model="text-embedding-3-large")
qdrant_client = QdrantClient(url="http://localhost", port=6333)

vector_store = QdrantVectorStore(
    client=qdrant_client,
    collection_name="tutorial",
    embedding=embedding
)

st.title("📄 PDFIQ – Ask Your PDF")

query = st.text_input("Ask a question about LLMs:")

if query:
    results = vector_store.similarity_search(query=query)

    context = "\n\n".join([
        f"Page Content: {doc.page_content}\nPage Number: {doc.metadata.get('page_label', 'N/A')}"
        for doc in results
    ])

    system_prompt = f"""
You are a helpful assistant. Use the provided context to answer the user's question.
Always mention relevant page numbers. Do not answer outside the given context.

Context:
{context}
"""

    chat_completion = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )

    st.subheader("Answer:")
    st.write(chat_completion.choices[0].message.content)