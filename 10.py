def enter_positive_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Error: Please enter a valid numeric amount.")


def enter_text(message):
    while True:
        text = input(message).strip()

        if not text:
            print("Error: This field cannot be empty.")
        else:
            return text


def add_expense(expenses):
    description = enter_text("Enter description: ")
    category = enter_text("Enter category: ")
    amount = enter_positive_amount("Enter amount: Rs. ")

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")

    for expense in expenses:
        print("Description:", expense["description"])
        print("Category   :", expense["category"])
        print("Amount     : Rs.", round(expense["amount"], 2))
        print("--------------------")


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print("Total Expenditure: Rs.", round(total, 2))


def analyze_categories(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n--- Category Analysis ---")

    for category, amount in categories.items():
        print(category, ": Rs.", round(amount, 2))


def show_budget_status(expenses, budget):
    total = sum(expense["amount"] for expense in expenses)
    remaining = budget - total

    print("Monthly Budget :", round(budget, 2))
    print("Total Expenses :", round(total, 2))
    print("Remaining      :", round(remaining, 2))

    if total <= budget:
        print("Budget Status: Within Budget")
    else:
        print("Budget Status: Over Budget")


def show_highest_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\n--- Highest Expense ---")
    print("Description:", highest["description"])
    print("Category   :", highest["category"])
    print("Amount     : Rs.", round(highest["amount"], 2))


def main():
    expenses = []

    print("--- Personal Expense Manager ---")
    budget = enter_positive_amount("Enter monthly budget: Rs. ")

    while True:
        print("\n--- Personal Expense Manager ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Analyze Categories")
        print("5. Show Budget Status")
        print("6. Show Highest Expense")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            calculate_total(expenses)

        elif choice == "4":
            analyze_categories(expenses)

        elif choice == "5":
            show_budget_status(expenses, budget)

        elif choice == "6":
            show_highest_expense(expenses)

        elif choice == "7":
            print("Exiting Expense Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()