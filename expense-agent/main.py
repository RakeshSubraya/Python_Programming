import sys

from services.database_service import DatabaseService
from services.expense_service import ExpenseService
from services.ollama_service import OllamaService
from repositories.expense_repository import ExpenseRepository


def run_console(expense_service):
    while True:
        print("\n==== Expense Agent ====")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Monthly Summary")
        print("4. Search Expenses")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Export Expenses")
        print("8. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            user_input = input("Enter expense: ")
            try:
                expense_service.add_expense(user_input)
            except Exception as exc:
                print(f"Failed to add expense: {exc}")

        elif choice == "2":
            expense_service.list_expenses()

        elif choice == "3":
            print("\n===== Monthly Report =====")
            print("1. Current Month")
            print("2. Previous Month")
            print("3. Custom Month")

            report_choice = input("Choose option: ").strip()

            if report_choice == "1":
                expense_service.monthly_summary()

            elif report_choice == "2":
                expense_service.previous_month_summary()

            elif report_choice == "3":
                try:
                    month = int(input("Enter Month (1-12): "))
                    year = int(input("Enter Year: "))
                    expense_service.monthly_summary(month, year)
                except ValueError:
                    print("Invalid month or year. Please enter valid numbers.")

            else:
                print("Invalid option")

        elif choice == "4":
            keyword = input("Enter search text: ")
            expense_service.search_expenses(keyword)

        elif choice == "5":
            try:
                expense_id = int(input("Enter expense id to update: "))
                expense_service.update_expense(expense_id)
            except ValueError:
                print("Invalid expense id.")

        elif choice == "6":
            try:
                expense_id = int(input("Enter expense id to delete: "))
                expense_service.delete_expense(expense_id)
            except ValueError:
                print("Invalid expense id.")

        elif choice == "7":
            filename = input("Enter export filename [expenses_export.csv]: ").strip() or "expenses_export.csv"
            try:
                expense_service.export_expenses(filename)
            except Exception as exc:
                print(f"Failed to export expenses: {exc}")

        elif choice == "8":
            break

        else:
            print("Invalid option")


def main():
    db_service = DatabaseService()
    repository = ExpenseRepository(db_service)
    ollama_service = OllamaService()
    expense_service = ExpenseService(ollama_service, repository)

    if len(sys.argv) > 1 and sys.argv[1] == "--console":
        run_console(expense_service)
        return

    try:
        from gui import ExpenseApp
    except Exception as exc:
        print("Unable to start graphical interface, falling back to console.")
        print(str(exc))
        run_console(expense_service)
        return

    app = ExpenseApp(expense_service)
    app.run()


if __name__ == "__main__":
    main()
