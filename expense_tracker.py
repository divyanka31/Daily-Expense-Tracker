
import json
import os

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def add_expense(expenses):
    name = input("Expense name: ").strip()

    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    expenses.append({"name": name, "amount": amount})

    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    print("\n-- Your Expenses --")

    for item in expenses:
        print(f"{item['name']}: ₹{item['amount']:.2f}")
        total += item["amount"]

    print(f"Total spent: ₹{total:.2f}")


expenses = load_expenses()

while True:
    print("\n=== Daily Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.")
