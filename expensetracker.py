import csv
import os
from collections import defaultdict

FILE_NAME = "expenses.csv"


def add_expense(date, category, amount, description):
    file_exists = os.path.isfile(FILE_NAME)
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!\n")


def view_expenses():
    if not os.path.isfile(FILE_NAME):
        print("⚠️ No expenses found. Add some first.\n")
        return
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


def show_summary():
    if not os.path.isfile(FILE_NAME):
        print("⚠️ No expenses found. Add some first.\n")
        return
    
    summary = defaultdict(float)
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            summary[row["Category"]] += float(row["Amount"])
    
    print("\n Expense Summary by Category:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")
    print()


while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, category, amount, description)
    
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        show_summary()
    
    elif choice == "4":
        print("👋 Exiting... Your data is saved in expenses.csv")
        break
    
    else:
        print("❌ Invalid choice. Try again.\n")
