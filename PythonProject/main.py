from logic import save_expense, fetch_chart_data
from datetime import datetime
import matplotlib.pyplot as plt


def main():
    while True:
        print("\n--- Kora: CLI Intelligence ---")
        print("1. Add Expense")
        print("2. View All-Time Spending")
        print("3. View This Month's Spending")
        print("4. View Specific Month/Year")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                amt = float(input("Amount spent: "))
                cat = input("Category: ").strip().capitalize()
                save_expense(amt, cat)
                print(f"✅ Saved ${amt} to {cat}")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

        elif choice in ['2', '3', '4']:
            filter_type = "all"
            target = ""

            if choice == '3':
                filter_type = "current"
                target = datetime.now().strftime("%Y-%m")
            elif choice == '4':
                filter_type = "choose"
                year = input("Year (YYYY): ")
                month = input("Month (MM): ")
                target = f"{year}-{month}"

            data = fetch_chart_data(filter_type, target)
            if data:
                plt.figure(figsize=(8, 6))
                plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
                plt.title(f"Kora Spending: {target if target else 'All Time'}")
                plt.show()
            else:
                print("No data found for that selection.")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()5
