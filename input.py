
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    """Create CSV file if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "amount", "category", "notes"])


def add_expense():
    """Get expense information from the user."""

    print("\n===== Add New Expense =====")

    # Get date
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")

    # Get amount
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break
        except ValueError:
            print("Please enter a valid number.")

    # Get category
    while True:
        category = input(
            "Enter category (Food/Transport/Shopping/Other): "
        ).strip()

        if category:
            break

        print("Category cannot be empty.")

    # Get optional notes
    notes = input("Enter notes (optional): ")

    # Save expense
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, notes])

    print("\nExpense added successfully!")


def main():
    initialize_file()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
