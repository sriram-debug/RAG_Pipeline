# RAG ML Assistant

A lightweight Retrieval-Augmented Generation (RAG) pipeline that answers machine learning questions using personal Markdown notes.

This project was built from scratch as a learning exercise to understand the core mechanics of Retrieval-Augmented Generation instead of relying on high-level frameworks. Every stage of the pipeline—from document loading to semantic retrieval and response generation—is implemented with minimal dependencies.

---

## Features

* Load knowledge from Markdown (`.md`) notes
* Automatically chunk documents into smaller retrieval units
* Generate sentence embeddings using `all-MiniLM-L6-v2`
* Store embeddings locally in a NumPy vector store (`.npz`)
* Perform semantic search using cosine similarity
* Retrieve the most relevant context for a query
* Generate grounded answers using Groq's Llama model
* Minimal, framework-free implementation focused on understanding the fundamentals

---

## How It Works

```
                Markdown Notes
                       │
                       ▼
             Load & Chunk Documents
                       │
                       ▼
             Generate Embeddings
                       │
                       ▼
          Save NumPy Vector Store
                       │
────────────────────────────────────────────
                       │
                 User Question
                       │
                       ▼
                 Embed Query
                       │
                       ▼
          Cosine Similarity Search
                       │
                       ▼
          Retrieve Top-k Chunks
                       │
                       ▼
        Build Grounded Prompt
                       │
                       ▼
              Groq Llama Model
                       │
                       ▼
                 Final Answer
```

### Retrieval Pipeline

1. Load Markdown notes from `data/notes/`.
2. Split each document into semantic chunks.
3. Generate embeddings for every chunk using `all-MiniLM-L6-v2`.
4. Store embeddings and chunk metadata in a compressed NumPy file.
5. Embed the user's question.
6. Compute cosine similarity between the query and every stored embedding.
7. Retrieve the top-*k* most relevant chunks.
8. Build a prompt containing the retrieved context.
9. Send the prompt to Groq's Llama model to generate a grounded response.

---

## Project Structure

```
rag-ml-assistant/
├── data/
│   └── notes/              # Markdown knowledge base
│
├── src/
│   ├── loader.py           # Load and chunk documents
│   ├── embedder.py         # Generate & save embeddings
│   ├── retriever.py        # Cosine similarity search
│   └── generator.py        # Prompt builder + Groq API
│
├── store/
│   └── chunks.npz          # Local vector store
│
├── main.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sriram-debug/RAG_Pipeline.git
cd RAG_Pipeline
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

Generate the embeddings:

```bash
python src/embedder.py
```

---

## Usage

Run the application:

```bash
python main.py
```

Example:

```text
Enter your query:
What is bias?
```

Output:

```text
Bias is the inability of a machine learning model to capture the true
relationship in the data.

High-bias models tend to oversimplify the problem,
leading to underfitting and poor performance on both
training and unseen data.
```

---

## Tech Stack

| Component         | Technology                                 |
| ----------------- | ------------------------------------------ |
| Language          | Python 3.12                                |
| Embeddings        | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector Store      | NumPy                                      |
| Similarity Search | Cosine Similarity                          |
| LLM               | Groq (`llama-3.3-70b-versatile`)           |

---

## Why Not LangChain?

The purpose of this project is to understand how Retrieval-Augmented Generation works under the hood.

Frameworks such as LangChain make building RAG applications much faster, but they abstract away many of the core components. Instead of relying on those abstractions, this project implements each stage manually—including document loading, chunking, embedding generation, vector storage, semantic retrieval, and prompt construction.

By building every component from scratch, I gained a deeper understanding of how modern RAG systems operate before moving on to higher-level frameworks.

---

## Current Limitations

* Linear (`O(n)`) retrieval over all embeddings
* Designed for small personal knowledge bases
* No reranking or hybrid retrieval
* No metadata filtering
* CLI interface only

These trade-offs keep the implementation simple while highlighting the core ideas behind semantic retrieval.

---

## Future Improvements

* FAISS-based approximate nearest-neighbor search
* Hybrid keyword + semantic retrieval
* Metadata filtering
* Streaming responses
* FastAPI backend
* React frontend
* Source citation highlighting
* Support for PDF and DOCX documents

---

## Learning Outcomes

Through this project I learned how to:

* Build a Retrieval-Augmented Generation pipeline from scratch
* Generate and manage embedding vectors
* Implement cosine similarity search without external vector databases
* Construct grounded prompts for LLMs
* Understand where frameworks like LangChain fit into the RAG ecosystem

---

## License

This project is open source and available under the MIT License.
