from src.loader import load_chunks
from src.retriever import retriever
from src.generator import generator


chunks = load_chunks("data/notes")
for c in chunks[:3]:
    print(c["source"], "|", c["text"][:80])
print(f"\nTotal chunks: {len(chunks)}")

query = input("Enter your query: ")

ans = retriever(query, 3)

print(generator(ans , query))

