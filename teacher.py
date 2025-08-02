import tkinter as tk
from tkinter import ttk, messagebox
from db_config import get_db_connection


def mark_attendance():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Implement your attendance marking logic here
            messagebox.showinfo("Success", "Attendance marked")
        finally:
            conn.close()


def main():
    root = tk.Tk()
    root.title("Teacher Dashboard")
    root.geometry("800x600")

    tk.Label(root, text="Teacher Dashboard", font=('Arial', 16)).pack(pady=20)
    tk.Button(root, text="Mark Attendance", command=mark_attendance).pack()

    root.mainloop()