from models.expense import Expense
from utils.date_parser import DateParser
from utils.console_feedback import Spinner
from datetime import datetime
from datetime import date
import calendar

class ExpenseService:

    def __init__(
        self,
        ollama_service,
        expense_repository
    ):
        self.ollama_service = ollama_service
        self.expense_repository = expense_repository

    def add_expense(self, user_text: str):

        print("\nReading your expense entry...")

        with Spinner("Asking local Ollama to convert the expense into JSON"):
            data = self.ollama_service.extract_expense(
                user_text
            )

        print("Expense details extracted:")
        print(f"  Date        : {data.get('expense_date', date.today().isoformat())}")
        print(f"  Amount      : {data['amount']}")
        print(f"  Category    : {data['category']}")
        print(f"  Description : {data['description']}")
        
     
        expense = Expense(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            expense_date=data.get(
                "expense_date",
                date.today().isoformat()
            )            
        )
        

        print("\nSaving expense to database...")

        self.expense_repository.save(
            expense
        )

        print("Expense saved successfully.")

        return expense
        
    def list_expenses(self):

        expenses = self.expense_repository.get_all()

        if not expenses:
            print("\nNo expenses found")
            return

        print("\nExpenses:\n")

        for expense in expenses:

            print(
                f"{expense[0]} | "
                f"{expense[1]} | "
                f"{expense[2]} | "
                f"{expense[3]} | "
                f"{expense[4]}"
            )        
                   
    def monthly_summary(self, month=None, year=None):

        now = datetime.now()

        if month is None:
            month = now.month

        if year is None:
            year = now.year

        summary = self.expense_repository.get_monthly_summary(
            month,
            year
        )

        if not summary:
            print(
                f"\nNo expenses found for "
                f"{calendar.month_name[month]} {year}"
            )
            return

        total = 0

        print("\n" + "=" * 41)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 41)

        print(
            f"Generated : "
            f"{now.strftime('%d-%b-%Y %I:%M %p')}"
        )

        print(
            f"Report For: "
            f"{calendar.month_name[month]} {year}"
        )

        print("Report    : Monthly Expense Summary")

        print("=" * 41)
        print(f"{'Category':<15} {'Amount':>15}")
        print("-" * 41)

        for category, amount in summary:

            total += amount

            print(
                f"{category:<15} "
                f"₹{amount:>14.2f}"
            )

        print("-" * 41)

        print(
            f"{'TOTAL':<15} "
            f"₹{total:>14.2f}"
        )

        print("-" * 41)

        print("\nThank you for using Expense Tracker")
        print("=" * 41)
    
    def previous_month_summary(self):

        now = datetime.now()

        if now.month == 1:

            month = 12
            year = now.year - 1

        else:

            month = now.month - 1
            year = now.year

        self.monthly_summary(
            month,
            year
        )
        
    def search_expenses(self, keyword):

        results = self.expense_repository.search(
            keyword
        )

        if not results:

            print(
                f"\nNo expenses found for '{keyword}'"
            )

            return

        print(
            f"\nResults for '{keyword}'\n"
        )

        for row in results:

            print(
                f"{row[0]} | "
                f"{row[1]} | "
                f"{row[2]} | "
                f"{row[3]} | "
                f"{row[4]}"
            )        
