import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from teacher import open_teacher_interface
from student import open_student_interface

def login():
    role = role_var.get()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not role:
        messagebox.showerror("Error", "Please select a role")
        return
    if not username or (role == "Teacher" and not password):
        messagebox.showerror("Error", "Please enter required credentials")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # <-- Your MySQL password
            database="attendance_system2"
        )
        cursor = conn.cursor()

        if role == "Teacher":
            query = "SELECT id, username FROM teacher WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            if user:
                login_window.destroy()
                open_teacher_interface(user[0], user[1])
            else:
                messagebox.showerror("Login Failed", "Invalid teacher credentials.")

        elif role == "Student":
            # Student login has no password in this design
            query = "SELECT student_id, username FROM student WHERE username=%s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            if user:
                login_window.destroy()
                open_student_interface(user[0], user[1])
            else:
                messagebox.showerror("Login Failed", "Student username not found.")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cursor.close()
        conn.close()

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x250")

tk.Label(login_window, text="Select Role:").pack(pady=5)
role_var = tk.StringVar()
role_combo = ttk.Combobox(login_window, textvariable=role_var, state="readonly")
role_combo['values'] = ("Teacher", "Student")
role_combo.pack()

tk.Label(login_window, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password (Teachers only):").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_btn = tk.Button(login_window, text="Login", command=login)
login_btn.pack(pady=20)

login_window.mainloop()
