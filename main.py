from tkinter import *
import login

root = Tk()
root.title("Student Attendance Management System")
root.geometry("300x200")

login.show_login(root)

root.mainloop()
