import tkinter as tk
from tkinter import ttk
from db_config import get_db_connection


def view_attendance():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Implement attendance viewing logic here
            pass
        finally:
            conn.close()


def main():
    root = tk.Tk()
    root.title("Student Dashboard")
    root.geometry("800x600")

    tk.Label(root, text="Student Dashboard", font=('Arial', 16)).pack(pady=20)
    tk.Button(root, text="View Attendance", command=view_attendance).pack()

    root.mainloop()