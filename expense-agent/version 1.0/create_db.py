import sqlite3

conn = sqlite3.connect("expense.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")