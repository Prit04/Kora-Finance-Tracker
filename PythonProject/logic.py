import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "expenses.csv"

def save_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

def fetch_chart_data(filter_type="all", target_prefix=""):
    categories = {}
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date_str, amount, cat = row[0], float(row[1]), row[2]
                if filter_type != "all" and not date_str.startswith(target_prefix):
                    continue
                categories[cat] = categories.get(cat, 0) + amount
        return categories
    except FileNotFoundError:
        return {}