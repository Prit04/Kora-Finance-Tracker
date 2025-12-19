# Kora: Personal Finance Intelligence 💰📊

Kora is a professional-grade personal finance tracker built with Python. It features a modular architecture that separates business logic from user interfaces, allowing users to interact with their data via either a modern Desktop GUI or a traditional Command Line Interface (CLI).

## 🚀 Key Features
- **Dual Interface:** Choose between a sleek, dark-mode Desktop App or a lightweight CLI.
- **Persistent Data:** All expenses are stored in a local CSV database, ensuring your history is saved across sessions.
- **Intelligent Filtering:** View spending habits for all-time, the current month, or any specific month/year in history.
- **Data Visualization:** Integrated with `matplotlib` to generate instant, easy-to-read spending breakdowns.
- **Robust Validation:** Error-handling logic ensures that invalid inputs (like letters in price fields) won't crash the system.

## 🏗️ System Architecture
Kora follows a **modular design** (Model-View-Controller inspired) to ensure code reusability and clean separation of concerns:

- **`logic.py`**: The "Backend" containing all data processing, file I/O operations, and filtering logic.
- **`gui_app.py`**: A modern desktop frontend built with `CustomTkinter`.
- **`main.py`**: A terminal-based frontend for fast, script-based interactions.

## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Kora-Finance-Tracker.git](https://github.com/YOUR_USERNAME/Kora-Finance-Tracker.git)

## 🛠️ Built With
- **Python 3.10+**
- **Matplotlib** - For data visualization.
- **CSV Module** - For data management.
- **Datetime** - For chronological tracking.
