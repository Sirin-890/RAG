# RAG
The RAG System is made using 
1. ChromaDB vector store
2. OpenAI API,Embedding

# Workflow
1. Parsing (using PyMupdf and BeautifulSoup)
2. Contextual retrieval
3. Dense Embeddings using OpenAI 
4. Sparse Embeddings (TF-IDF)
5. Rank Fusion
6. Generation using OpenAI LLM


Clone the repository and switch into its directory:

```bash
git clone https://github.com/Sirin-890/RAG
cd RAG
python3.10 -m venv rag_venv
source rag_venv/bin/activate  # For Linux/macOS
# OR for Windows
# rag_venv\Scripts\activate
pip install -r requirements.txt
python fast_api.py
```

After Contextual Retrieval and embedding formation finishes, the server will start. Then run the UI:

```bash
python ui.py
```

Then access the interface at: http://127.0.0.1:7860
