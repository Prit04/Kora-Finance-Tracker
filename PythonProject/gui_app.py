import customtkinter as ctk
from logic import save_expense, fetch_chart_data
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class KoraGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kora Finance Intelligence")
        self.geometry("400x450")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Kora Finance", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount (e.g. 50.00)")
        self.amount_entry.pack(pady=10)

        self.category_entry = ctk.CTkEntry(self, placeholder_text="Category (e.g. Food)")
        self.category_entry.pack(pady=10)

        self.add_btn = ctk.CTkButton(self, text="Add Expense", command=self.add_data)
        self.add_btn.pack(pady=10)

        self.chart_btn = ctk.CTkButton(self, text="View All-Time Chart", fg_color="green", command=self.show_chart)
        self.chart_btn.pack(pady=10)

    def add_data(self):
        try:
            amt = float(self.amount_entry.get())
            cat = self.category_entry.get().capitalize()
            if amt > 0 and cat:
                save_expense(amt, cat)
                self.amount_entry.delete(0, 'end')
                self.category_entry.delete(0, 'end')
                print("Saved!")
        except ValueError:
            print("Invalid Input")

    def show_chart(self):
        data = fetch_chart_data("all")
        if data:
            plt.figure(figsize=(6, 4))
            plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
            plt.title("Kora: Spending Breakdown")
            plt.show()

if __name__ == "__main__":
    app = KoraGUI()
    app.mainloop()