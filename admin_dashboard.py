from tkinter import *

def open_admin_dashboard(main_root):
    win = Toplevel(main_root)
    win.title("Admin Dashboard")
    win.geometry("400x300")

    Label(win, text="Welcome Admin", font=("Arial", 16)).pack(pady=20)
