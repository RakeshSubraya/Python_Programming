import sqlite3

conn = sqlite3.connect("expense.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO expenses
(expense_date, amount, category, description)
VALUES
(date('now'), 250, 'Food', 'Lunch')
""")

conn.commit()
conn.close()

print("Expense saved")