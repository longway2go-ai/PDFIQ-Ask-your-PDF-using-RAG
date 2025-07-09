from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain_qdrant import QdrantVectorStore


file_path = "Maths behind LLMs.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
#print("Docs[0]",docs[0])
api_key=""

print(f"✅ Loaded {len(docs)} pages from PDF")
#chunking
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,chunk_overlap=200
)

split_docs=text_splitter.split_documents(documents=docs)
print(f"✅ Split into {len(split_docs)} chunks")

#vector embedding
embedding=OpenAIEmbeddings(
    model='text-embedding-3-large',openai_api_key=api_key
    
)
print("✅ Created embedding model")

vectore_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",  # REST endpoint for Qdrant
    collection_name="tutorial",
    embedding=embedding
)
print("✅ Document indexing complete.")


