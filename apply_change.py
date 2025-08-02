import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

def open_request_form(username):
    def submit():
        reason = text.get("1.0", tk.END).strip()
        if reason:
            conn = get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO change_requests (student_username, reason) VALUES (%s, %s)", (username, reason))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Request submitted successfully.")
                win.destroy()
        else:
            messagebox.showwarning("Empty", "Please write a reason.")

    win = tk.Toplevel()
    win.title("Change Request")
    win.geometry("400x250")

    tk.Label(win, text="Reason for Change:").pack(pady=5)
    text = tk.Text(win, height=5)
    text.pack(pady=5)

    tk.Button(win, text="Submit", command=submit).pack(pady=10)
