# AI Coding Agent Instructions

This document helps AI coding agents understand the structure and conventions of the Python Programming repository.

## Repository Overview

This is a collection of independent Python learning projects and implementation experiments, each in its own folder with its own dependencies and documentation.

- **expense-agent**: Local AI-powered CLI expense tracker using Ollama and SQLite
- **RAG_Implementaion**: Learning project for Retrieval-Augmented Generation (RAG) with Python

## Project Structure

Each project is self-contained:
```
Python_Programming/
├── expense-agent/        # Expense tracking with local LLM
├── RAG_Implementaion/    # RAG implementation experiments
├── ReadMe.md             # Repository overview
└── AGENTS.md             # This file
```

## Development Conventions

### Environment Setup

Both projects require Python 3.12+ and isolated virtual environments:

```powershell
# For any project folder:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Project Organization

- **models/**: Data models and schemas
- **services/**: Business logic and external service integration
- **repositories/**: Data persistence and database operations
- **utils/**: Helper functions and utilities
- **version 1.0/**: (expense-agent only) Previous version for reference

## Project Details

### expense-agent

**Purpose**: CLI application to parse natural-language expense entries into structured JSON records stored in SQLite.

**Key Files**:
- [main.py](expense-agent/main.py) - CLI entry point with menu loop
- [models/expense.py](expense-agent/models/expense.py) - Expense dataclass
- [services/expense_service.py](expense-agent/services/expense_service.py) - Business logic
- [services/ollama_service.py](expense-agent/services/ollama_service.py) - Local LLM integration
- [repositories/expense_repository.py](expense-agent/repositories/expense_repository.py) - Database operations

**Architecture Pattern**: Service-Repository-Model (SRM)
- Models define data structures
- Services implement business logic
- Repositories handle database persistence
- Services depend on repositories

**Dependencies**: ollama, pandas, openpyxl

**Setup Requirements**:
```powershell
cd expense-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# The database initializes automatically on first run

# Ensure Ollama is running with gemma3:4b model
ollama pull gemma3:4b
```

**Run Command**: `python main.py`

**Database**: `expense.db` (SQLite, local runtime, not committed to Git)

**Key Patterns**:
- Service layer handles Ollama communication with console feedback/spinners
- Repository abstracts database operations
- Date parsing utilities for flexible date inputs
- Console feedback with spinner animations

### RAG_Implementaion

**Purpose**: Learning project for building a complete RAG pipeline with Python, from tokenizers to FastAPI service.

**Current Implementation**:
- Tokenizer experiments (OpenAI tokenizer, SentencePiece)
- Corpus analysis
- Foundation for embeddings and vector search

**Planned Stages** (see README for full details):
1. Document loading and PDF chunking
2. OpenAI embeddings
3. ChromaDB vector storage
4. Cosine similarity search
5. RAG pipeline
6. Streaming responses
7. FastAPI service
8. Docker containerization

**Key Files**:
- [main.py](RAG_Implementaion/main.py) - Demo entry point
- [openai_tokenizer.py](RAG_Implementaion/openai_tokenizer.py) - OpenAI tokenization demo
- [sentencepiece_tokenizer.py](RAG_Implementaion/sentencepiece_tokenizer.py) - SentencePiece tokenizer
- [bpe_from_scratch/](RAG_Implementaion/bpe_from_scratch/) - BPE implementation module
- [common/logger.py](RAG_Implementaion/common/logger.py) - Shared logging utility

**Dependencies**: openai, tiktoken, pandas, numpy, python-dotenv, regex

**Setup Requirements**:
```powershell
cd RAG_Implementaion
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Create .env file with your OpenAI API key
# .env
# OPENAI_API_KEY=your_key_here
```

**Run Commands**: `python main.py` or run specific demo files

**Key Patterns**:
- Modular demo files for each concept (tokenizer, embeddings, RAG, etc.)
- Utility modules in separate folders (bpe_from_scratch, common)
- Environment variables for sensitive configuration (OpenAI API key)
- Gradual complexity increase from tokenization to full RAG

## Working with These Projects

### Adding a New Project

Create a folder with this structure:
```
NewProject/
├── README.md           # Project description and setup
├── requirements.txt    # Python dependencies
├── main.py             # Entry point
├── src/                # Source code
├── data/               # Data files
└── tests/              # Tests (when applicable)
```

### Running Code

1. **Activate the project's virtual environment** before running any code
2. **Install dependencies** from requirements.txt if they've changed
3. **Check project README** for setup requirements (API keys, external services, etc.)

### Common Issues

**expense-agent**:
- Ollama must be running and have the `gemma3:4b` model pulled
- The database initializes automatically on first run
- Virtual environment must be activated before running

**RAG_Implementaion**:
- OpenAI API key must be set in `.env` file
- Uses newer dependencies (numpy 2.5.0, openai 2.43.0) - ensure compatibility
- Scripts are demos; not all features are fully implemented yet

## AI Agent Guidance

### Best Practices

- **Read project READMEs first** for setup and context
- **Respect the architecture**: Follow the SRM pattern in expense-agent, modular demo structure in RAG
- **Environment variables**: Check for `.env` files and API key requirements
- **Virtual environments**: Always work within the project's virtual environment
- **Database management**: In expense-agent, `expense.db` is runtime-generated, not source-controlled

### Debugging

- Check if virtual environments are activated
- Verify external services are running (Ollama for expense-agent)
- Check API keys and `.env` configuration for RAG_Implementaion
- Review error messages carefully; they often point to missing setup steps

### Extension Ideas

- expense-agent: Add CSV export, expense forecasting, budget alerts
- RAG_Implementaion: Complete the RAG pipeline stages, add more demo files, implement FastAPI layer
