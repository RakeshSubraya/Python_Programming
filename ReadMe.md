# Python Programming

This repository is a collection of Python learning projects and implementation experiments. Each project should live in its own folder with its own README, dependencies, source files, and examples.

The goal is to keep different Python topics organized in one repository while allowing each project to grow independently.

## Repository Structure

```text
Python_Programming/
|-- ReadMe.md
|-- .gitignore
|
`-- RAG_Implementaion/
    |-- README.md
    |-- requirements.txt
    |-- *.py
    `-- old/
```

## Current Projects

### RAG_Implementaion

This project focuses on building a Retrieval-Augmented Generation (RAG) workflow with Python.

Planned implementation areas:

1. Document loading.
2. PDF chunking.
3. OpenAI embeddings.
4. ChromaDB vector storage.
5. Cosine similarity search.
6. RAG pipeline.
7. Streaming responses.
8. FastAPI service.
9. Dockerized application.

Project folder:

```text
RAG_Implementaion/
```

## Planned Future Projects

More Python projects can be added as separate folders, for example:

```text
Python_Programming/
|-- RAG_Implementaion/
|-- FastAPI_Projects/
|-- Data_Analysis/
|-- Automation_Scripts/
|-- Machine_Learning/
`-- OpenAI_Agents/
```

## Adding a New Python Project

For every new project, create a separate folder:

```text
Project_Name/
|-- README.md
|-- requirements.txt
|-- src/
|-- data/
`-- tests/
```

Recommended project guidelines:

- Add a project-specific `README.md`.
- Keep dependencies in that project's `requirements.txt`.
- Store reusable code inside `src/`.
- Store test files inside `tests/` when needed.
- Keep secrets in `.env` files and do not commit them.
- Keep virtual environments out of Git.

## Setup Notes

Create virtual environments inside individual project folders or at the repository root as needed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies from the project folder you are working on:

```powershell
pip install -r requirements.txt
```

## Git Notes

The repository `.gitignore` excludes local environment files, virtual environments, Python cache files, notebook checkpoints, and generated vector database files.
