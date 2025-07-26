from tkinter import *
from tkinter import messagebox
import sqlite3
from admin_dashboard import open_admin_dashboard
from teacher_dashboard import open_teacher_dashboard

def open_login(main_root):
    login_win = Toplevel(main_root)
    login_win.title("Login")
    login_win.geometry("300x250")

    Label(login_win, text="Email").pack(pady=5)
    email_entry = Entry(login_win)
    email_entry.pack()

    Label(login_win, text="Password").pack(pady=5)
    password_entry = Entry(login_win, show='*')
    password_entry.pack()

    def attempt_login():
        email = email_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM teachers WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()

        if result:
            login_win.destroy()
            if email == "admin@admin.com":
                open_admin_dashboard(main_root)
            else:
                open_teacher_dashboard(main_root, result[1])
        else:
            messagebox.showerror("Error", "Invalid Credentials")
        conn.close()

    Button(login_win, text="Login", command=attempt_login).pack(pady=15)
