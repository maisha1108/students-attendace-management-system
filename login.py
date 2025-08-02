import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db_config import get_db_connection


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        tk.Label(root, text="Username:").pack()
        self.username = tk.Entry(root)
        self.username.pack()

        tk.Label(root, text="Password:").pack()
        self.password = tk.Entry(root, show="*")
        self.password.pack()

        tk.Button(root, text="Login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                               (self.username.get(), self.password.get()))
                user = cursor.fetchone()

                if user:
                    self.root.destroy()
                    role = user[3]  # Assuming role is at index 3
                    if role == "admin":
                        import admin
                        admin.main()
                    elif role == "teacher":
                        import teacher
                        teacher.main()
                    else:
                        import student
                        student.main()
                else:
                    messagebox.showerror("Error", "Invalid credentials")
            finally:
                conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()