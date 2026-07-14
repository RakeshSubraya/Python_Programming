import sqlite3


class DatabaseService:

    def __init__(self, db_name="expense.db"):
        self.db_name = db_name

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
            """
        )
        conn.commit()
        return conn
