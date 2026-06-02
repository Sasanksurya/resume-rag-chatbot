# Resume RAG Chatbot

## Project Overview

Resume RAG Chatbot is an AI-powered application that allows users to upload a resume PDF and ask questions in natural language.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant resume content and generate accurate responses using Groq Llama 3.

## Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Groq Llama 3
* PyPDF

## Features

* Upload Resume PDF
* Resume Text Extraction
* Semantic Chunking
* Vector Embeddings
* FAISS Vector Database
* Context Retrieval
* AI-Powered Question Answering
* Chat History
* Retrieved Context Display

## Architecture

Resume PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Retriever
↓
Groq LLM
↓
Answer

## Installation

pip install -r requirements.txt

## Run

streamlit run app.py
