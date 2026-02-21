import os
import streamlit as st 
from dotenv import load_dotenv

# langchain imports
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1 : page configuration
st.set_page_config(page_title="C++ RAG Chatbot", page_icon="💭")
st.title("💭 C++ RAG Chatbot")
st.write("Ask any question related to C++ introduction")

# Step 2 : load environment variables
load_dotenv()

# Step 3 : cache document loading
@st.cache_resource
def load_vector_store():
    
    # Step A: load documents
    loader = TextLoader("C++_Introduction.txt", encoding="utf-8")
    documents = loader.load()

    # Step B: split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    final_documents = text_splitter.split_documents(documents)

    # Step C: embeddings
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Step D: create FAISS vector store
    db = FAISS.from_documents(final_documents, embedding)

    return db

# Load vector database (runs only once due to caching)
db = load_vector_store()

# User input
query = st.text_input("Enter your question about C++:")

if query:
    # Search FAISS database
    documents = db.similarity_search(query, k=3)

    st.subheader("📙 Retrieved Context")

    for i, doc in enumerate(documents):
        st.markdown(f"**Result {i+1}:**")
        st.write(doc.page_content)