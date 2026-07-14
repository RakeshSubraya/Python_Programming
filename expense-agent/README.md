# Expense Agent

Expense Agent is a local Python application for tracking personal expenses with both GUI and CLI interfaces. It uses a local Ollama model to convert human-written expense text into structured JSON, then stores the parsed records in a SQLite database.

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

- **Graphical User Interface (GUI)**: User-friendly desktop interface for managing expenses
- **Natural Language Parsing**: Parse natural-language expense entries using local Ollama
- **Direct Entry Form**: Enter expenses with amount, category, date, and description fields
- **Expense List**: View all saved expenses in a formatted table with sortable columns
- **Monthly Reports**: Generate formatted monthly expense reports with category breakdown and totals
- **Search Functionality**: Search expenses by category or description
- **Update & Delete**: Modify or remove saved expenses
- **Export**: Export expenses to CSV or Excel format
- **Console Mode**: Full-featured CLI interface available as fallback or standalone option
- **SQLite Storage**: Persistent local database for all expense records

## Project Structure

```text
expense-agent/
|-- README.md
|-- main.py                    # Entry point (GUI or Console)
|-- gui.py                     # Tkinter GUI interface
|-- expense.db                 # SQLite database (runtime)
|
|-- models/
|   `-- expense.py             # Expense data model
|
|-- repositories/
|   `-- expense_repository.py  # Database access layer
|
|-- services/
|   |-- database_service.py    # Database connection management
|   |-- expense_service.py     # Business logic for expenses
|   `-- ollama_service.py      # Ollama LLM integration
|
|-- utils/
|   `-- console_feedback.py    # Console UI utilities
|
`-- version 1.0/               # Legacy version
```

Note: `expense.db` is a local runtime database and should not be committed to Git.

## Requirements

- Python 3.12 or later
- Ollama installed and running locally
- The configured Ollama model pulled locally (default: `gemma3:4b`)
- tkinter (included with Python on most systems)

Pull the Ollama model if needed:

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

The database initializes automatically when the application starts, so you do not need to run the setup script manually.

## Run

### GUI Mode (Default)

Start the graphical interface:

```powershell
python main.py
```

If a GUI is unavailable, the app automatically falls back to console mode.

**GUI Features:**
- Add Expense form with fields for amount, category, date, and description
- Parse natural language expense text
- View all expenses in a searchable list
- Generate monthly expense reports with total breakdown
- Real-time expense list refresh

### Console Mode

Start the console-only interface:

```powershell
python main.py --console
```

**Console Menu Options:**

```text
1. Add Expense              - Add expense via natural language
2. List Expenses           - View all saved expenses
3. Monthly Summary         - Generate monthly report
4. Search Expenses         - Search by keyword
5. Update Expense          - Modify an existing expense
6. Delete Expense          - Remove an expense
7. Export Expenses         - Export to CSV/Excel
8. Exit                    - Quit the application
```

## Data Flow

### GUI Flow
```text
User Input (Form/Natural Language)
-> ExpenseService.parse_expense_text() or add_expense_record()
-> Expense Model Creation
-> ExpenseRepository.save()
-> SQLite Database
-> UI List/Report Refresh
```

### Console Flow
```text
User expense text
-> Console progress indicator
-> OllamaService.extract_expense()
-> JSON expense data
-> Expense preview
-> ExpenseRepository.save()
-> SQLite database
```

## Future Improvements

- Add tests for parsing, repository, and service logic
- Add richer category suggestions and budgeting alerts
- Add history filtering by date range
- Add expense editing from GUI
- Add budget tracking and spending alerts
- Add data visualization (charts/graphs)
- Add multi-user support with authentication
