import os
import streamlit as st 
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="C++ rag chatbot",layout="wide")
st.title("💭 C++ rag chatbot")


@st.cache_resource
def load_vector_store():
    loader = TextLoader("C++_Introduction.txt", encoding="utf-8")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    final_documents = text_splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(final_documents, embedding)
    return db

db = load_vector_store()

llm = Ollama(model="gemma2:2b")

#Chat interface
text_input=st.text_input("Ask a question about c++")
if(text_input):
    with st.spinner(text="Thinking...."):
        docs = db.similarity_search(text_input)
        context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""
    Answer the question using the context below
    
    Context : {context}
    Question : {text_input}
    Answer : 
    """    

    response = llm.invoke(prompt)
    st.subheader("Answers")
    st.write(response)