import chromadb
chroma_client = chromadb.Client()
#vector store 
def vector_store(collection, embed_vector, chunk, chunk_no):
    collection.add(
        embeddings=[embed_vector],
        documents=[chunk["text"]],
        metadatas=[chunk["metadata"]],
        ids=[f"id{chunk_no}"]
    )