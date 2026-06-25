# RAG Implementation

This project folder is a learning and implementation workspace for Python-based LLM experiments. It starts with tokenizer and OpenAI API demos, then grows into a Retrieval-Augmented Generation (RAG) application using PDF loading, embeddings, vector search, streaming responses, FastAPI, and Docker.

## Current Files

The folder currently contains these starter scripts:

```text
RAG_Implementaion/
|-- README.md
|-- requirements.txt
|-- openai_tokenizer.py
`-- old/
```

## Planned Project Structure

The intended structure for the complete project is:

```text
RAG_Implementaion/
|-- README.md
|-- requirements.txt
|-- tokenizer_demo.py
|-- embeddings_demo.py
|-- similarity_demo.py
|-- vector_db_demo.py
|-- rag_demo.py
|-- chat_completion_demo.py
|-- streaming_demo.py
|-- agent_demo.py
|
|-- data/
|   `-- books.pdf
|
|-- notebooks/
|
`-- src/
    |-- tokenizer.py
    |-- embeddings.py
    |-- rag.py
    `-- utils.py
```

## Project Goals

This project will be built step by step:

1. Create a document loader.
2. Implement PDF chunking.
3. Create embeddings using OpenAI.
4. Store embeddings in ChromaDB.
5. Implement cosine similarity search.
6. Write a RAG pipeline.
7. Add streaming responses.
8. Convert the project into a FastAPI service.
9. Dockerize the application.

## Planned Demo Files

- `tokenizer_demo.py`: Demonstrates token encoding, decoding, token counts, and model-specific tokenization.
- `embeddings_demo.py`: Generates embeddings for text using OpenAI embedding models.
- `similarity_demo.py`: Compares text similarity using cosine similarity.
- `vector_db_demo.py`: Stores and retrieves embeddings from ChromaDB.
- `rag_demo.py`: Loads documents, chunks content, retrieves relevant chunks, and answers questions.
- `chat_completion_demo.py`: Shows basic chat completion usage.
- `streaming_demo.py`: Demonstrates streaming model responses.
- `agent_demo.py`: Experiments with a simple agent-style workflow.

## Source Modules

- `src/tokenizer.py`: Reusable tokenizer helper functions.
- `src/embeddings.py`: Embedding generation and vector helpers.
- `src/rag.py`: RAG pipeline logic.
- `src/utils.py`: Shared utility functions.

## Setup

From the `RAG_Implementaion` folder, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Running Scripts

Run any demo script with:

```powershell
python tokenizer_demo.py
```

For the currently available starter files, run:

```powershell
python Encode_Example.py
python decoding_example.py
python Indivisual_token.py
python RawToken_string.py
python Different_Model_Compare.py
```

## Future FastAPI App

The planned FastAPI service will expose endpoints for:

- Uploading or loading documents.
- Creating and storing embeddings.
- Searching relevant chunks.
- Asking questions through the RAG pipeline.
- Streaming model responses.

## Notes

- Do not commit `.env` because it contains secrets.
- Keep large PDFs and generated vector database files out of source control unless they are intentionally required.
- Add `chromadb`, `fastapi`, `uvicorn`, and Docker files when those stages are implemented.

