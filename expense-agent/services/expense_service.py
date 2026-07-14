from models.expense import Expense
from utils.console_feedback import Spinner
from datetime import datetime, date
import calendar
import csv
from pathlib import Path


class ExpenseService:

    ALLOWED_CATEGORIES = [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Medical",
        "Entertainment",
        "Education",
        "Other"
    ]

    def __init__(
        self,
        ollama_service,
        expense_repository
    ):
        self.ollama_service = ollama_service
        self.expense_repository = expense_repository

    def _normalize_expense_data(self, data):

        if not isinstance(data, dict):
            raise ValueError("Expense data must be a JSON object.")

        amount = data.get("amount")
        if amount is None:
            raise ValueError("Expense amount is required.")

        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Expense amount must be a number.")

        category = str(data.get("category", "Other")).strip().title()
        if category not in self.ALLOWED_CATEGORIES:
            category = "Other"

        description = str(data.get("description", "")).strip()
        if not description:
            raise ValueError("Expense description is required.")

        expense_date = str(data.get("expense_date", date.today().isoformat())).strip()
        try:
            datetime.fromisoformat(expense_date)
        except ValueError:
            expense_date = date.today().isoformat()

        return Expense(
            amount=amount,
            category=category,
            description=description,
            expense_date=expense_date
        )

    def _format_expense_row(self, row):
        return (
            f"{row['id']} | "
            f"{row['expense_date']} | "
            f"₹{row['amount']:.2f} | "
            f"{row['category']} | "
            f"{row['description']}"
        )

    def add_expense(self, user_text: str):

        print("\nReading your expense entry...")

        with Spinner("Processing your expense"):
            data = self.ollama_service.extract_expense(
                user_text
            )

        try:
            expense = self._normalize_expense_data(data)
        except ValueError as exc:
            raise Exception(f"Invalid expense data: {exc}")

        print("Expense details extracted:")
        print(f"  Date        : {expense.expense_date}")
        print(f"  Amount      : ₹{expense.amount:.2f}")
        print(f"  Category    : {expense.category}")
        print(f"  Description : {expense.description}")

        print("\nSaving expense to database...")
        self.expense_repository.save(expense)
        print("Expense saved successfully.")

        return expense

    def parse_expense_text(self, user_text: str):
        data = self.ollama_service.extract_expense(user_text)
        return self._normalize_expense_data(data)

    def add_expense_record(
        self,
        amount,
        category,
        description,
        expense_date=None
    ):
        data = {
            "amount": amount,
            "category": category,
            "description": description,
            "expense_date": expense_date
        }
        expense = self._normalize_expense_data(data)
        self.expense_repository.save(expense)
        return expense

    def get_all_expenses(self):
        return self.expense_repository.get_all()

    def get_monthly_summary_data(self, month=None, year=None):
        now = datetime.now()
        if month is None:
            month = now.month
        if year is None:
            year = now.year
        return self.expense_repository.get_monthly_summary(month, year)

    def get_allowed_categories(self):
        return list(self.ALLOWED_CATEGORIES)

    def format_monthly_report(self, month, year, summary_rows):
        now = datetime.now()
        lines = []
        lines.append("========================================")
        lines.append("       PERSONAL EXPENSE TRACKER")
        lines.append("========================================")
        lines.append(f"Generated : {now.strftime('%d-%b-%Y %I:%M %p')}")
        lines.append(f"Report For: {calendar.month_name[month]} {year}")
        lines.append("Report    : Monthly Expense Summary")
        lines.append("========================================")
        lines.append(f"{'Category':<15} {'Amount':>15}")
        lines.append("----------------------------------------")
        total = 0
        for category, amount in summary_rows:
            total += amount
            lines.append(f"{category:<15} ₹{amount:>14.2f}")
        lines.append("----------------------------------------")
        lines.append(f"{'TOTAL':<15} ₹{total:>14.2f}")
        lines.append("========================================")
        return "\n".join(lines)

    def list_expenses(self):

        expenses = self.expense_repository.get_all()

        if not expenses:
            print("\nNo expenses found")
            return

        print("\nExpenses:\n")
        print("ID | Date | Amount | Category | Description")
        print("-- | ---- | ------ | -------- | -----------")

        for expense in expenses:
            print(self._format_expense_row(expense))

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
            f"Generated : {now.strftime('%d-%b-%Y %I:%M %p')}"
        )
        print(
            f"Report For: {calendar.month_name[month]} {year}"
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
            print(f"\nNo expenses found for '{keyword}'")
            return

        print(f"\nResults for '{keyword}'\n")
        print("ID | Date | Amount | Category | Description")
        print("-- | ---- | ------ | -------- | -----------")

        for row in results:
            print(self._format_expense_row(row))

    def update_expense(self, expense_id):

        expense_row = self.expense_repository.get_by_id(expense_id)
        if not expense_row:
            print(f"\nExpense with id {expense_id} not found.")
            return

        print("\nUpdating expense")
        print(self._format_expense_row(expense_row))
        print("Leave an entry blank to keep the current value.")

        new_date = input(f"Date [{expense_row['expense_date']}]: ").strip() or expense_row['expense_date']
        new_amount = input(f"Amount [{expense_row['amount']}]: ").strip()
        new_category = input(f"Category [{expense_row['category']}]: ").strip()
        new_description = input(f"Description [{expense_row['description']}]: ").strip()

        if new_amount:
            try:
                amount = float(new_amount)
            except ValueError:
                print("Invalid amount provided. Keeping existing amount.")
                amount = expense_row['amount']
        else:
            amount = expense_row['amount']

        if new_category:
            new_category = new_category.title()
            category = new_category if new_category in self.ALLOWED_CATEGORIES else expense_row['category']
            if new_category not in self.ALLOWED_CATEGORIES:
                print("Invalid category provided. Keeping existing category.")
        else:
            category = expense_row['category']

        description = new_description or expense_row['description']
        try:
            datetime.fromisoformat(new_date)
            expense_date = new_date
        except ValueError:
            print("Invalid date provided. Keeping existing date.")
            expense_date = expense_row['expense_date']

        updated_expense = Expense(
            amount=amount,
            category=category,
            description=description,
            expense_date=expense_date
        )

        self.expense_repository.update(expense_id, updated_expense)
        print("Expense updated successfully.")

    def delete_expense(self, expense_id):

        expense_row = self.expense_repository.get_by_id(expense_id)
        if not expense_row:
            print(f"\nExpense with id {expense_id} not found.")
            return

        self.expense_repository.delete(expense_id)
        print(f"Expense id {expense_id} deleted successfully.")

    def export_expenses(self, filename=None):

        expenses = self.expense_repository.get_all()
        if not expenses:
            print("\nNo expenses to export.")
            return

        output_path = Path(filename or "expenses_export.csv")
        output_path = output_path if output_path.suffix else output_path.with_suffix('.csv')

        if output_path.suffix.lower() in [".xlsx", ".xls"]:
            try:
                import pandas as pd
            except ImportError:
                print("Pandas is not available. Exporting to CSV instead.")
                output_path = output_path.with_suffix('.csv')
            else:
                df = pd.DataFrame([
                    {
                        "id": row["id"],
                        "expense_date": row["expense_date"],
                        "amount": row["amount"],
                        "category": row["category"],
                        "description": row["description"]
                    }
                    for row in expenses
                ])
                df.to_excel(output_path, index=False)
                print(f"Expenses exported to {output_path}")
                return

        with output_path.open("w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["id", "expense_date", "amount", "category", "description"])
            for row in expenses:
                writer.writerow([
                    row["id"],
                    row["expense_date"],
                    row["amount"],
                    row["category"],
                    row["description"]
                ])

        print(f"Expenses exported to {output_path}")
