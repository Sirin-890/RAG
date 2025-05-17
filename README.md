# RAG Demo

This repository demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using FastAPI for backend services and Gradio for the user interface.

## Features

- Document embedding and contextual retrieval  
- FastAPI backend for processing queries  
- Gradio interface for interacting with the RAG system

## Getting Started

Clone the repository and switch into its directory:

```bash
git clone https://github.com/Sirin-890/RAG
cd RAG
python3.10 -m venv rag_venv
source rag_venv/bin/activate #rag_venv\Scripts\activate.bat for windows
pip install -r requirements.txt
python fast_api.py

##After  Contexual Retrival and embedding  formation will  finish server will start rand run ui.py
```bash
python ui.py

