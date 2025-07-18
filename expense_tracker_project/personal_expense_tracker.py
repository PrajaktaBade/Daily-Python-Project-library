import json
import os
from datetime import datetime
from collections import defaultdict

DATA_FILE = "expenses_data.json"

CATEGORIES = [
    "Food", "Transport", "Utilities", "Entertainment", "Health",
    "Shopping", "Income", "Other"
]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_transaction(data):
    date_str = input("Date (YYYY-MM-DD, leave blank for today): ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    amount = input("Amount (use negative for expenses, positive for income): ").strip()
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    print("Categories:", ", ".join(CATEGORIES))
    category = input("Category: ").strip().title()
    if category not in CATEGORIES:
        print("Unknown category. Using 'Other'.")
        category = "Other"

    description = input("Description (optional): ").strip()

    transaction = {
        "date": date_str,
        "amount": amount,
        "category": category,
        "description": description
    }
    data.append(transaction)
    save_data(data)
    print("Transaction added.")

def show_report(data):
    if not data:
        print("No transactions found.")
        return

    print("\n--- Summary Report ---")
    totals = defaultdict(float)
    for t in data:
        totals[t["category"]] += t["amount"]

    print("Category-wise totals:")
    for cat in CATEGORIES:
        print(f"{cat:15}: {totals[cat]:.2f}")

    total_income = sum(t["amount"] for t in data if t["amount"] > 0)
    total_expense = -sum(t["amount"] for t in data if t["amount"] < 0)
    print(f"\nTotal Income : {total_income:.2f}")
    print(f"Total Expense: {total_expense:.2f}")
    print(f"Net Savings  : {total_income - total_expense:.2f}")

    # Spending by month
    monthly = defaultdict(float)
    for t in data:
        month = t["date"][:7]
        if t["amount"] < 0:
            monthly[month] += -t["amount"]
    print("\nMonthly Expenses:")
    for month in sorted(monthly):
        print(f"{month}: {monthly[month]:.2f}")

def list_transactions(data):
    if not data:
        print("No transactions found.")
        return
    print("\n--- All Transactions ---")
    for t in data:
        print(f"{t['date']} | {t['category']:12} | {t['amount']:8.2f} | {t['description']}")

def main():
    data = load_data()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Transaction")
        print("2. Show Report")
        print("3. List Transactions")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            show_report(data)
        elif choice == "3":
            list_transactions(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()