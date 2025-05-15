import chromadb
chroma_client = chromadb.Client()

# def vector_store(embed_vector,chunk,chunk_no):
#     na="LSTM"+str(chunk_no)
#     collection = chroma_client.create_collection(name=na)
#     collection.add(
#     embeddings = embed_vector,
#     documents = [chunk["text"]],
#     metadatas = [chunk["metadata"]],
#     ids = ["id1"]
#     )
def vector_store(collection, embed_vector, chunk, chunk_no):
    collection.add(
        embeddings=[embed_vector],
        documents=[chunk["text"]],
        metadatas=[chunk["metadata"]],
        ids=[f"id{chunk_no}"]
    )