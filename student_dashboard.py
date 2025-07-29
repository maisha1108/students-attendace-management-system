from tkinter import *
import sqlite3
from tkinter import messagebox

def open_student_dashboard(root, student_id):
    win = Toplevel(root)
    win.title("Student Dashboard")
    win.geometry("500x400")

    Label(win, text=f"Student Dashboard - ID {student_id}", font=("Arial", 16)).pack(pady=10)

    def view_attendance():
        top = Toplevel(win)
        top.title("My Attendance")
        top.geometry("400x300")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT date, status FROM attendance WHERE student_id = ?", (student_id,))
        records = cursor.fetchall()
        conn.close()

        if not records:
            Label(top, text="No attendance records found.").pack()
        else:
            for row in records:
                Label(top, text=f"{row[0]} - {row[1]}").pack(anchor="w")

    def submit_request():
        top = Toplevel(win)
        top.title("Request Correction")
        top.geometry("350x200")

        Label(top, text="Describe the issue:").pack(pady=5)
        issue_entry = Text(top, height=5, width=40)
        issue_entry.pack()

        def send_request():
            issue = issue_entry.get("1.0", END).strip()
            if issue:
                conn = sqlite3.connect("attendance.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO requests (student_id, issue) VALUES (?, ?)", (student_id, issue))
                conn.commit()
                conn.close()
                top.destroy()
                messagebox.showinfo("Success", "Request submitted.")
            else:
                messagebox.showerror("Error", "Please enter your issue.")

        Button(top, text="Submit", command=send_request).pack(pady=10)

    Button(win, text="View Attendance", command=view_attendance, width=25).pack(pady=10)
    Button(win, text="Report Mismatch", command=submit_request, width=25).pack(pady=10)
