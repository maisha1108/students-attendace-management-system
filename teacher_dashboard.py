from tkinter import *

def open_teacher_dashboard(main_root, teacher_name):
    win = Toplevel(main_root)
    win.title("Teacher Dashboard")
    win.geometry("400x300")

    Label(win, text=f"Welcome {teacher_name}", font=("Arial", 16)).pack(pady=20)
