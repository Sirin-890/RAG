def get_rank_dict(id_list):
    """Given a ranked list of IDs, return a dict mapping ID to rank."""
    return {doc_id: rank for rank, doc_id in enumerate(id_list)}

def reciprocal_rank_fusion(rank_dicts, k=60):
    """Apply Reciprocal Rank Fusion to combine rank dictionaries."""
    rrf_scores = {}
    for rank_dict in rank_dicts:
        for doc_id, rank in rank_dict.items():
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

def get_final_results_rrf(result_dense, chunk_list, topk_sparse_indices, k=5):
    # Step 1: Extract dense IDs
    dense_ids = result_dense["ids"][0]  # List of doc IDs from dense retrieval

    # Step 2: Extract sparse IDs using indices
    sparse_ids = [chunk_list[i]["id"] for i in topk_sparse_indices]

    # Step 3: Build rank dicts
    dense_rank = get_rank_dict(dense_ids)
    sparse_rank = get_rank_dict(sparse_ids)

    # Step 4: Apply RRF
    fused = reciprocal_rank_fusion([dense_rank, sparse_rank], k=60)

    # Step 5: Pick top-k fused results
    topk_fused_ids = [doc_id for doc_id, _ in fused[:k]]

    # Step 6: Retrieve full chunk info from chunk_list
    for chunk in chunk_list:
        if chunk["id"] in topk_fused_ids:
            

    final_chunks = [chunk["text"] for chunk in chunk_list if chunk["id"] in topk_fused_ids]

    return final_chunks
