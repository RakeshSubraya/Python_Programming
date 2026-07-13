# Python Programming

This repository is a collection of Python learning projects and implementation experiments. Each project should live in its own folder with its own README, dependencies, source files, and examples.

The goal is to keep different Python topics organized in one repository while allowing each project to grow independently.

## Repository Structure

```text
Python_Programming/
|-- ReadMe.md
|-- .gitignore
|
|-- RAG_Implementaion/
|   |-- README.md
|   |-- requirements.txt
|   |-- *.py
|   `-- old/
|
`-- expense-agent/
    |-- README.md
    |-- requirements.txt
    |-- main.py
    |-- models/
    |-- repositories/
    |-- services/
    `-- utils/
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

### expense-agent

This project is a local AI expense tracker. It uses Ollama to parse human-written expense details into JSON and stores the records in a SQLite database.

Current implementation areas:

1. Natural-language expense entry.
2. Ollama-based JSON extraction.
3. SQLite database storage.
4. Expense listing.
5. Expense search.
6. Monthly expense summaries.
7. Future full CRUD support.

Project folder:

```text
expense-agent/
```

The `expense-agent` project now includes a helper script to clone a reference virtual environment from the repository root into `expense-agent/.venv`.

## Planned Future Projects

More Python projects can be added as separate folders, for example:

```text
Python_Programming/
|-- RAG_Implementaion/
|-- expense-agent/
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

### expense-agent environment helper

If the root reference environment is already configured, you can clone it into the `expense-agent` project with:

```powershell
python expense-agent\setup_env_from_root.py
expense-agent\.venv\Scripts\python.exe expense-agent\main.py
```

If you want to create a fresh environment instead, use the normal venv setup inside `expense-agent`.

## Git Notes

The repository `.gitignore` excludes local environment files, virtual environments, Python cache files, notebook checkpoints, and generated vector database files.
