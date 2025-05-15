from parsing import parse_all
from contextaul_retrival import all_chunks_context
from embeddings import get_embeddings
from vector_store import vector_store
import chromadb
from rank_calculation import get_final_results_rrf
from sparse_rank import tf_idf
import openai
from prompts import*
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="LSTMNotes")
k=5
pdf_path=""
url=""
chunk_list=parse_all(pdf_path,url)
all_chunks_context(chunk_list)
i=0


for chunk in chunk_list:
    i=i+1
    embedding=get_embeddings(chunk["text"])
    vector_store(collection,embedding,chunk,i)

query=input("enter your quey here")
embedding_query=get_embeddings(query)
results_dense = collection.query(
    query_embeddings=[embedding_query],
    n_results=k
)
topk_sparse_indices=tf_idf(chunk_list,query,k)
topk_chunks = get_final_results_rrf(results_dense, chunk_list, topk_sparse_indices, k=5)


user_prompt= "Context"+topk_chunks["text"]+"Query"+query
response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0  # optional, lower = more accurate
)

print(response['choices'][0]['message']['content'])

