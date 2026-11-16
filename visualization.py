
import csv
import os
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


def load_expenses():
    """Load expense data from CSV."""

    expenses = []

    if not os.path.exists(FILE_NAME):
        print("Error: expenses.csv not found!")
        return expenses

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["amount"])
                category = row["category"].strip()

                if amount > 0 and category:
                    expenses.append({
                        "amount": amount,
                        "category": category
                    })

            except (ValueError, KeyError):
                print("Skipping invalid expense record.")

    return expenses


def create_pie_chart(expenses):
    """Generate pie chart based on expense categories."""

    if not expenses:
        print("No expense data available!")
        return

    # Calculate total amount by category
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Create pie chart
    plt.figure(figsize=(8, 6))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%",
        startangle=90,
        shadow=False
    )

    plt.title("Expense Distribution by Category")
    plt.axis("equal")

    # Save chart
    plt.savefig("screenshots/pie_chart.png", dpi=300,
                bbox_inches="tight")

    plt.show()

    print("Pie chart saved successfully!")


def main():
    expenses = load_expenses()
    create_pie_chart(expenses)


if __name__ == "__main__":
    main()
