from services.database_service import DatabaseService
from services.expense_service import ExpenseService
from services.ollama_service import OllamaService

from repositories.expense_repository import ExpenseRepository


def main():

    db_service = DatabaseService()

    repository = ExpenseRepository(
        db_service
    )

    ollama_service = OllamaService()

    expense_service = ExpenseService(
        ollama_service,
        repository
    )

    while True:

        print("\n==== Expense Agent ====")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Monthly Summary")
        print("4. Search Expenses")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":

            user_input = input(
                "Enter expense: "
            )

            expense_service.add_expense(
                user_input
            )

        elif choice == "2":

            expense_service.list_expenses()

        elif choice == "3":

            print("\n===== Monthly Report =====")
            print("1. Current Month")
            print("2. Previous Month")
            print("3. Custom Month")

            choice = input("Choose option: ")

            if choice == "1":
                expense_service.monthly_summary()

            elif choice == "2":
                expense_service.previous_month_summary()

            elif choice == "3":

                month = int(input("Enter Month (1-12): "))
                year = int(input("Enter Year: "))

                expense_service.monthly_summary(month, year)

            else:
                print("Invalid option")            

        elif choice == "4":

            keyword = input(
                "Enter search text: "
            )

            expense_service.search_expenses(
                keyword
            )

        elif choice == "5":

            break

        else:

            print("Invalid option")


if __name__ == "__main__":
    main()