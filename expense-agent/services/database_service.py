import sqlite3


class DatabaseService:

    def __init__(self, db_name="expense.db"):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name)