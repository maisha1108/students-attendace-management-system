from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date

def open_teacher_dashboard(root, teacher_name):
    win = Toplevel(root)
    win.title("Teacher Dashboard")
    win.geometry("500x400")

    Label(win, text=f"Welcome {teacher_name}", font=("Arial", 18)).pack(pady=10)

    def mark_attendance():
        top = Toplevel(win)
        top.title("Mark Attendance")
        top.geometry("400x400")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        entries = []

        for student in students:
            var = StringVar(value="Present")
            Label(top, text=student[1]).pack(anchor="w")
            OptionMenu(top, var, "Present", "Absent").pack(anchor="w")
            entries.append((student[0], var))

        def submit_attendance():
            today = date.today().strftime("%Y-%m-%d")
            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()
            for sid, status_var in entries:
                cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                               (sid, today, status_var.get()))
            conn.commit()
            conn.close()
            top.destroy()
            messagebox.showinfo("Success", "Attendance marked successfully")

        Button(top, text="Submit", command=submit_attendance).pack(pady=10)

    def view_attendance():
        top = Toplevel(win)
        top.title("Attendance Records")
        top.geometry("500x300")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT students.name, attendance.date, attendance.status
            FROM attendance
            JOIN students ON attendance.student_id = students.student_id
            ORDER BY date DESC
        ''')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            Label(top, text=f"{row[0]} | {row[1]} | {row[2]}").pack(anchor="w")

    Button(win, text="Mark Attendance", command=mark_attendance, width=20).pack(pady=10)
    Button(win, text="View Attendance", command=view_attendance, width=20).pack(pady=10)
