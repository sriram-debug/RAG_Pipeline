# run this file to embeed the data into the vector database

from sentence_transformers import SentenceTransformer
import numpy as np
from loader import load_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

strings = load_chunks("data/notes")

text = [ i["text"] for i in strings ]

vdb  = model.encode(text)

print(vdb.shape)

np.savez("store/chunks.npz", embeddings=vdb, texts= text)