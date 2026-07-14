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

This project is a local AI-powered expense tracker with both graphical and console interfaces. It uses Ollama to parse human-written expense details into JSON and stores the records in a SQLite database.

Current implementation areas:

1. **Graphical User Interface (Tkinter)** - Desktop app for managing expenses
2. **Natural-language expense entry** - Parse free-form expense descriptions
3. **Direct form entry** - Add expenses with explicit fields (amount, category, date, description)
4. **Ollama-based JSON extraction** - Convert natural language to structured data
5. **SQLite database storage** - Persistent local expense records
6. **Expense listing and searching** - View and filter expenses by category or keyword
7. **Monthly expense reports** - Formatted reports with category breakdown and totals
8. **Console CLI interface** - Full-featured command-line interface as fallback or standalone
9. **Export functionality** - Export expenses to CSV or Excel
10. **Full CRUD support** - Create, read, update, delete expenses

**Key Features:**
- Dual-interface design (GUI default, CLI fallback)
- Real-time expense list and report generation
- Formatted monthly summaries with totals
- Search by category or description
- Natural language parsing with progress feedback
- Export to multiple formats (CSV, Excel)

Project folder:

```text
expense-agent/
|-- main.py              # Entry point (GUI or Console)
|-- gui.py               # Tkinter GUI interface
|-- models/
|-- repositories/
|-- services/
`-- utils/
```

**How to Run:**

GUI mode (default):
```powershell
python expense-agent\main.py
```

Console mode:
```powershell
python expense-agent\main.py --console
```

For detailed usage, see `expense-agent/README.md`.

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
