from tkinter import *
from tkinter import messagebox
import sqlite3
from admin_dashboard import open_admin_dashboard
from teacher_dashboard import open_teacher_dashboard
from student_dashboard import open_student_dashboard  # <- Added student dashboard

def open_login(main_root):
    login_win = Toplevel(main_root)
    login_win.title("Login")
    login_win.geometry("300x350")

    Label(login_win, text="Teacher/Admin Login", font=("Arial", 12)).pack(pady=10)

    Label(login_win, text="Email").pack()
    email_entry = Entry(login_win)
    email_entry.pack()

    Label(login_win, text="Password").pack()
    password_entry = Entry(login_win, show='*')
    password_entry.pack()

    def attempt_login():
        email = email_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM teachers WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            login_win.destroy()
            if email == "admin@admin.com":
                open_admin_dashboard(main_root)
            else:
                open_teacher_dashboard(main_root, result[1])
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    Button(login_win, text="Login as Admin/Teacher", command=attempt_login).pack(pady=10)

    # Student login section
    Label(login_win, text="-------------------------------").pack(pady=5)
    Label(login_win, text="Student Login", font=("Arial", 12)).pack(pady=10)
    Label(login_win, text="Enter Student ID").pack()
    sid_entry = Entry(login_win)
    sid_entry.pack()

    def student_login():
        sid = sid_entry.get()
        if not sid.isdigit():
            messagebox.showerror("Error", "Student ID must be a number.")
            return

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id=?", (sid,))
        result = cursor.fetchone()
        conn.close()

        if result:
            login_win.destroy()
            open_student_dashboard(main_root, int(sid))
        else:
            messagebox.showerror("Error", "Invalid Student ID")

    Button(login_win, text="Login as Student", command=student_login).pack(pady=10)
