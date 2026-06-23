from models.expense import Expense


class ExpenseRepository:

    def __init__(self, db_service):
        self.db_service = db_service

    def save(self, expense: Expense):

        conn = self.db_service.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO expenses
            (
                expense_date,
                amount,
                category,
                description
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                expense.expense_date,
                expense.amount,
                expense.category,
                expense.description
            )
        )

        conn.commit()
        conn.close()
        
    def get_all(self):

        conn = self.db_service.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                expense_date,
                amount,
                category,
                description
            FROM expenses
            ORDER BY expense_date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows        
        
    def get_monthly_summary(self, month, year):

        conn = self.db_service.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                category,
                SUM(amount)
            FROM expenses
            WHERE strftime('%m', expense_date) = ?
              AND strftime('%Y', expense_date) = ?
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """,
        (
            f"{month:02d}",
            str(year)
        ))

        rows = cursor.fetchall()
        
        conn.close()

        return rows       
        
    def search(self, keyword):

        conn = self.db_service.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                expense_date,
                amount,
                category,
                description
            FROM expenses
            WHERE
                LOWER(category) LIKE LOWER(?)
                OR LOWER(description) LIKE LOWER(?)            
            ORDER BY expense_date DESC
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        rows = cursor.fetchall()

        conn.close()

        return rows        