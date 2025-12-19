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


def show_chart(filter_type="all"):
    """
    filter_type options: "all", "current", "choose"
    """
    categories = {}
    target_prefix = ""

    if filter_type == "current":
        target_prefix = datetime.now().strftime("%Y-%m")
    elif filter_type == "choose":
        year = input("Enter year (YYYY, e.g., 2025): ")
        month = input("Enter month (MM, e.g., 01 to 12): ")
        target_prefix = f"{year}-{month}"

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date_str, amount, cat = row[0], float(row[1]), row[2]

                # Filter logic
                if filter_type != "all" and not date_str.startswith(target_prefix):
                    continue

                categories[cat] = categories.get(cat, 0) + amount

        if not categories:
            print(f"No data found for {target_prefix if target_prefix else 'all time'}.")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
        plt.title(f"Spending: {target_prefix if target_prefix else 'All Time'}")
        plt.show()

    except FileNotFoundError:
        print("No data file found. Add some expenses first!")


def main():
    while True:
        print("\n--- Kora: Personal Finance Tracker ---")
        print("1. Add Expense")
        print("2. View All-Time Spending")
        print("3. View This Month's Spending")
        print("4. View Specific Month/Year")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_chart(filter_type="all")
        elif choice == '3':
            show_chart(filter_type="current")
        elif choice == '4':
            show_chart(filter_type="choose")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-5.")


if __name__ == "__main__":
    main()