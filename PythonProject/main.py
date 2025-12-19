import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print("✅ Expense saved!")


def show_chart():
    categories = {}
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[1])
                cat = row[2]
                categories[cat] = categories.get(cat, 0) + amount

        # Plotting the data
        labels = categories.keys()
        sizes = categories.values()

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Spending by Category")
        plt.show()

    except FileNotFoundError:
        print("No data found. Add some expenses first!")


def main():
    while True:
        print("\n--- SpendWise Tracker ---")
        print("1. Add Expense")
        print("2. View Spending Chart")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amt = input("Amount spent: ")
            cat = input("Category (Food, Transport, Rent, etc.): ")
            add_expense(amt, cat)
        elif choice == '2':
            show_chart()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()