# RAG ML Assistant

A minimal Retrieval-Augmented Generation (RAG) system that answers machine learning questions from personal notes. No vector databases, no LangChain — just NumPy, sentence-transformers, and a Groq API call.

Built as a learning project to understand how RAG pipelines work from the ground up.

## How it works

1. Loads `.md` notes from `data/notes/`
2. Chunks them by section/paragraph
3. Embeds chunks using `all-MiniLM-L6-v2` (384-dim vectors)
4. Stores embeddings in a NumPy `.npz` file
5. On query: embeds the question, runs cosine similarity, retrieves top-k chunks
6. Passes retrieved context + question to Groq LLM for a grounded answer

## Project Structure

```
rag-ml-assistant/
├── data/
│   └── notes/          # .md cheat sheet notes
├── src/
│   ├── loader.py       # load and chunk .md files
│   ├── embedder.py     # generate and save embeddings
│   ├── retriever.py    # cosine similarity search
│   └── generator.py    # prompt builder + Groq API call
├── store/
│   └── chunks.npz      # saved embeddings (auto-generated)
└── main.py             # entrypoint
```

## Setup

```bash
git clone https://github.com/yourusername/rag-ml-assistant
cd rag-ml-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set your Groq API key:

```bash
export GROQ_API_KEY="your_key_here"
```

Generate the embeddings store:

```bash
python src/embedder.py
```

## Usage

```bash
python main.py
```

```
Enter your query: what is bias

Bias is the inability of a machine learning method to capture the true 
relationship in the data. A high-bias model oversimplifies the problem — 
for example, fitting a straight line to data that follows a curve. 
This leads to underfitting, where the model performs poorly on both 
training and unseen data.
```

## Stack

- `sentence-transformers` — `all-MiniLM-L6-v2` for embeddings
- `numpy` — vector store and cosine similarity
- `groq` — LLM inference (llama-3.3-70b-versatile)
- Python 3.12, Ubuntu 24
