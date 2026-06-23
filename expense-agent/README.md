# Expense Agent

Expense Agent is a local Python CLI application for tracking personal expenses. It uses a local Ollama model to convert human-written expense text into structured JSON, then stores the parsed records in a SQLite database.

Example input:

```text
Spent 250 rupees on lunch yesterday
```

Example parsed record:

```json
{
  "amount": 250,
  "category": "Food",
  "description": "lunch",
  "expense_date": "2026-06-22"
}
```

## Features

- Parse natural-language expense entries using local Ollama.
- Convert expense information into JSON.
- Save expense records into SQLite.
- List saved expenses.
- Search expenses by category or description.
- Generate monthly summaries.
- Support future CRUD operations on expense records.

## Project Structure

```text
expense-agent/
|-- README.md
|-- ReadMe.txt
|-- requirements.txt
|-- main.py
|-- expense.db
|
|-- models/
|   `-- expense.py
|
|-- repositories/
|   `-- expense_repository.py
|
|-- services/
|   |-- database_service.py
|   |-- expense_service.py
|   `-- ollama_service.py
|
|-- utils/
|   `-- date_parser.py
|
`-- version 1.0/
```

Note: `expense.db` is a local runtime database and should not be committed to Git.

## Requirements

- Python 3.12 or later.
- Ollama installed and running locally.
- The configured Ollama model pulled locally. The current code uses `gemma3:4b`.

Pull the model if needed:

```powershell
ollama pull gemma3:4b
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Database Setup

The application stores records in SQLite using `expense.db`.

If the database does not exist, create it with the database setup script from the `version 1.0` folder:

```powershell
python "version 1.0\create_db.py"
```

## Run

Start the CLI app:

```powershell
python main.py
```

Menu options:

```text
1. Add Expense
2. List Expenses
3. Monthly Summary
4. Search Expenses
5. Exit
```

## Current Data Flow

```text
User expense text
-> OllamaService
-> JSON expense data
-> Expense model
-> ExpenseRepository
-> SQLite database
```

## Future Improvements

- Add update and delete operations for full CRUD support.
- Add automatic database initialization.
- Add input validation and better error handling.
- Add export support for CSV or Excel.
- Add tests for parsing, repository, and service logic.
