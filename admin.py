import tkinter as tk
from tkinter import ttk
from db_config import get_db_connection


def main():
    root = tk.Tk()
    root.title("Admin Dashboard")
    root.geometry("800x600")

    # Simple admin interface
    label = tk.Label(root, text="Admin Dashboard", font=('Arial', 16))
    label.pack(pady=20)

    # Add your admin functionality here
    root.mainloop()