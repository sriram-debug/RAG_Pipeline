import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

#comparing the query with vector database

def retriever( query,k):
    data = np.load("store/chunks.npz")
    chunk, text = data["embeddings"], data["texts"]
    
    query_emb = model.encode(query)
    cos_sim = np.dot(chunk , query_emb) / (np.linalg.norm(chunk ,axis=1)* np.linalg.norm( query_emb ))

    top_k_indices = np.argsort(cos_sim)[::-1][:k]
    ans = text[top_k_indices]
    return ans

print(retriever("what is cross validation", 3))