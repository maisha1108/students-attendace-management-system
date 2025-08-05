from tkinter import *
from tkinter import messagebox
import mysql_connection
import teacher_module, student_module, admin_module

def show_login(root):
    def login_action():
        username = user_entry.get().strip()
        password = pass_entry.get().strip()

        db = mysql_connection.connect()
        cursor = db.cursor()

        # First check if username exists and get role
        cursor.execute("SELECT role FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()

        if not result:
            messagebox.showerror("Login Failed", "Invalid username")
            db.close()
            return

        role = result[0]

        if role == 'student':
            # For students, check if roll exists in students table (password ignored)
            cursor.execute("SELECT id FROM students WHERE roll=%s", (username,))
            student_exist = cursor.fetchone()
            if student_exist:
                login_frame.destroy()
                db.close()
                student_module.student_interface(root, username)
            else:
                messagebox.showerror("Login Failed", "Invalid roll number")
                db.close()
        else:
            # For admin and teacher, verify username and password
            cursor.execute("SELECT role FROM users WHERE username=%s AND password=%s", (username, password))
            auth = cursor.fetchone()
            db.close()
            if auth:
                login_frame.destroy()
                if role == 'admin':
                    admin_module.admin_interface(root)
                elif role == 'teacher':
                    teacher_module.teacher_interface(root)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

    login_frame = Frame(root)
    login_frame.pack()

    Label(login_frame, text="Username / Roll").grid(row=0, column=0)
    user_entry = Entry(login_frame)
    user_entry.grid(row=0, column=1)

    Label(login_frame, text="Password (leave blank if student)").grid(row=1, column=0)
    pass_entry = Entry(login_frame, show="*")
    pass_entry.grid(row=1, column=1)

    Button(login_frame, text="Login", command=login_action).grid(row=2, column=0, columnspan=2)

