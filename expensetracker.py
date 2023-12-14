import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()

    def load_data(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self, amount, category, description):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        expense = {'date': date, 'amount': amount, 'category': category, 'description': description}
        self.expenses.append(expense)
        self.save_data()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']} - ${expense['amount']} - {expense['category']} - {expense['description']}")

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                amount = float(input("Enter the amount spent: "))
                category = input("Enter the category: ")
                description = input("Enter a description: ")
                self.add_expense(amount, category, description)
                print("Expense added successfully!")

            elif choice == '2':
                
                print("\nAll Expenses:")
                self.view_expenses()

            elif choice == '3':
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()



