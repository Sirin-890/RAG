from parsing import parse_all
from contextaul_retrival import all_chunks_context
from embeddings import get_embeddings
from vector_store import vector_store
import chromadb
from rank_calculation import get_final_results_rrf
from sparse_rank import tf_idf
import openai
from openai import OpenAI
from loguru import logger
from prompts import*
chroma_client = chromadb.Client()
import os

# openai.api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI()


# collection = chroma_client.create_collection(name="LSTMNotes")
# k=5
# pdf_path="LSTM.pdf"
# url="https://colah.github.io/posts/2015-08-Understanding-LSTMs/"
# chunk_list=parse_all(pdf_path,url)
# all_chunks_context(chunk_list)
# i=0


# for chunk in chunk_list:
#     i=i+1
#     embedding=get_embeddings(chunk["text"])
#     vector_store(collection,embedding,chunk,i)
#     logger.debug(f"embedding formation of {i}chunk done")

# query=input("enter your quey here")
# embedding_query=get_embeddings(query)
# results_dense = collection.query(
#     query_embeddings=[embedding_query],
#     n_results=k
# )
# topk_sparse_indices=tf_idf(chunk_list,query,k)
# topk_chunks,l = get_final_results_rrf(results_dense, chunk_list, topk_sparse_indices, k=5)


# user_prompt= "Context"+topk_chunks+"Query"+query
# response = client.chat.completions.create(
#     model="gpt-4",  # or "gpt-3.5-turbo"
#     messages=[
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": user_prompt}
#     ],
#     temperature=0  # optional, lower = more accurate
# )

# logger.info(response.choices[0].message.content)
# print(l)


# from parsing import parse_all
# from contextaul_retrival import all_chunks_context
# from embeddings import get_embeddings
# from vector_store import vector_store
# import chromadb
# from rank_calculation import get_final_results_rrf
# from sparse_rank import tf_idf
# from openai import OpenAI
# import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Setup ChromaDB & collection
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="LSTMNotes")

# Parse and store chunks only once
pdf_path = "LSTM.pdf"
url = "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"
chunk_list = parse_all(pdf_path, url)
all_chunks_context(chunk_list)

# You should run this separately once and skip re-embedding later
def store_all_chunks():
    for i, chunk in enumerate(chunk_list, 1):
        embedding = get_embeddings(chunk["text"])
        vector_store(collection, embedding, chunk, i)

def run_rag(query: str, top_k: int = 5) -> str:
    embedding_query = get_embeddings(query)
    results_dense = collection.query(query_embeddings=[embedding_query], n_results=top_k)
    topk_sparse_indices = tf_idf(chunk_list, query, top_k)
    topk_chunks,l = get_final_results_rrf(results_dense, chunk_list, topk_sparse_indices, k=5)


    user_prompt= "Context"+topk_chunks+"Query"+query
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0  # optional, lower = more accurate
    )
    logger.debug(response.choices[0].message.content)
    print(l)
    return response.choices[0].message.content,l
    