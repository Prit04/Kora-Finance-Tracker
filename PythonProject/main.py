import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense():
    # --- INPUT VALIDATION ---
    while True:
        try:
            amount = float(input("Amount spent: "))
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number (e.g., 12.50).")

    category = input("Category (Food, Transport, Rent, etc.): ").strip().capitalize()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print(f"✅ Saved ${amount} under {category}!")


def show_chart(filter_month=False):
    categories = {}
    current_month = datetime.now().strftime("%Y-%m")

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date_str, amount, cat = row[0], float(row[1]), row[2]

                # --- DATE FILTERING ---
                if filter_month and not date_str.startswith(current_month):
                    continue

                categories[cat] = categories.get(cat, 0) + amount

        if not categories:
            print("No data found for this period.")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
        title = f"Spending for {current_month}" if filter_month else "Total Spending"
        plt.title(title)
        plt.show()

    except FileNotFoundError:
        print("No data file found. Add some expenses first!")


def main():
    while True:
        print("\n--- SpendWise: Personal Finance Tracker ---")
        print("1. Add Expense")
        print("2. View All-Time Spending")
        print("3. View This Month's Spending Only")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_chart(filter_month=False)
        elif choice == '3':
            show_chart(filter_month=True)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-4.")


if __name__ == "__main__":
    main()