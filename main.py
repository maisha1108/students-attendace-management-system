from tkinter import *
from login import open_login
from db import init_db

init_db()

root = Tk()
root.title("Student Attendance Management System")
root.geometry("400x300")

Label(root, text="Welcome to Attendance System", font=("Arial", 16)).pack(pady=20)

Button(root, text="Login", width=20, command=lambda: open_login(root)).pack(pady=10)

root.mainloop()
