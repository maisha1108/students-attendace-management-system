<<<<<<< HEAD
from tkinter import *
import sqlite3
from tkinter import messagebox

def open_admin_dashboard(root):
    win = Toplevel(root)
    win.title("Admin Dashboard")
    win.geometry("500x400")

    Label(win, text="Admin Dashboard", font=("Arial", 18)).pack(pady=10)

    def add_student():
        def save_student():
            name = name_entry.get()
            sclass = class_entry.get()
            contact = contact_entry.get()

            if not name:
                messagebox.showerror("Error", "Name required")
                return

            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (name, student_class, contact) VALUES (?, ?, ?)", (name, sclass, contact))
            conn.commit()
            conn.close()
            top.destroy()
            messagebox.showinfo("Success", "Student added successfully")

        top = Toplevel(win)
        top.title("Add Student")
        top.geometry("300x250")

        Label(top, text="Name").pack()
        name_entry = Entry(top)
        name_entry.pack()

        Label(top, text="Class").pack()
        class_entry = Entry(top)
        class_entry.pack()

        Label(top, text="Contact").pack()
        contact_entry = Entry(top)
        contact_entry.pack()

        Button(top, text="Save", command=save_student).pack(pady=10)

    def view_students():
        top = Toplevel(win)
        top.title("All Students")
        top.geometry("400x300")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            Label(top, text=f"ID: {row[0]} | Name: {row[1]} | Class: {row[2]}").pack(anchor="w")

    Button(win, text="Add Student", command=add_student, width=20).pack(pady=10)
    Button(win, text="View Students", command=view_students, width=20).pack(pady=10)
=======
from tkinter import *

def open_admin_dashboard(main_root):
    win = Toplevel(main_root)
    win.title("Admin Dashboard")
    win.geometry("400x300")

    Label(win, text="Welcome Admin", font=("Arial", 16)).pack(pady=20)
>>>>>>> 6a6cee2d7872b6b63def9724b276ce29d927e8cd
