import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Add Expense Function
def add_expense():
    date = date_entry.get()
    if date == "":
        date = datetime.now().strftime("%d-%m-%Y")

    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()

    if amount == "" or category == "":
        messagebox.showerror("Error", "Amount and Category are required!")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    messagebox.showinfo("Success", "Expense Added Successfully!")

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# View Expenses Function
def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            data = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, data)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No expenses found!")

# Main Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

tk.Label(root, text="Expense Tracker", font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Date (DD-MM-YYYY):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Entry(root)
description_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses, bg="blue", fg="white").pack(pady=5)

text_area = tk.Text(root, height=10)
text_area.pack(pady=10)

root.mainloop()