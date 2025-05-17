# RAG

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
