from tkinter import *
import mysql_connection
from datetime import date
from tkinter import messagebox

def teacher_interface(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame = Frame(root)
    frame.pack()

    Label(frame, text="Add Student", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)

    Label(frame, text="Name").grid(row=1, column=0)
    name_entry = Entry(frame)
    name_entry.grid(row=1, column=1)

    Label(frame, text="Roll").grid(row=2, column=0)
    roll_entry = Entry(frame)
    roll_entry.grid(row=2, column=1)

    Label(frame, text="Class").grid(row=3, column=0)
    class_entry = Entry(frame)
    class_entry.grid(row=3, column=1)

    def add_student():
        name = name_entry.get().strip()
        roll = roll_entry.get().strip()
        class_name = class_entry.get().strip()

        if not name or not roll or not class_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        db = mysql_connection.connect()
        cursor = db.cursor()

        try:
            # Insert into students table
            cursor.execute("INSERT INTO students (name, roll, class) VALUES (%s, %s, %s)",
                           (name, roll, class_name))
            db.commit()

            # Insert into users table for student login (roll as username, blank password)
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                           (roll, '', 'student'))
            db.commit()

            messagebox.showinfo("Success", f"Student {name} added and login created with roll: {roll}")
            name_entry.delete(0, END)
            roll_entry.delete(0, END)
            class_entry.delete(0, END)

        except Exception as e:
            db.rollback()
            messagebox.showerror("Database Error", str(e))
        finally:
            db.close()

    Button(frame, text="Add Student", command=add_student, bg="lightblue").grid(row=4, column=0, columnspan=2, pady=10)

    def mark_attendance():
        for widget in frame.winfo_children():
            widget.destroy()

        Label(frame, text="Mark Attendance", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        db = mysql_connection.connect()
        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM students")
        students = cursor.fetchall()

        attendance_vars = {}

        for i, (sid, name) in enumerate(students):
            Label(frame, text=name).grid(row=i+1, column=0)
            var = StringVar(value="Present")
            OptionMenu(frame, var, "Present", "Absent").grid(row=i+1, column=1)
            attendance_vars[sid] = var

        def save_all():
            today = date.today()
            try:
                for sid, var in attendance_vars.items():
                    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)",
                                   (sid, today, var.get()))
                db.commit()
                messagebox.showinfo("Success", "Attendance saved successfully!")
                view_attendance()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", str(e))

        Button(frame, text="Save Attendance", command=save_all, bg="lightgreen").grid(row=len(students)+1, columnspan=2, pady=10)
        Button(frame, text="Back", command=lambda: teacher_interface(root)).grid(row=len(students)+2, columnspan=2)

    def view_attendance():
        for widget in frame.winfo_children():
            widget.destroy()

        Label(frame, text="All Attendance Records", font=("Arial", 14, "bold")).grid(row=0, columnspan=3, pady=10)

        db = mysql_connection.connect()
        cursor = db.cursor()
        cursor.execute("""
            SELECT students.name, students.roll, attendance.date, attendance.status 
            FROM attendance 
            JOIN students ON attendance.student_id = students.id
            ORDER BY attendance.date DESC
        """)
        records = cursor.fetchall()
        db.close()

        for i, (name, roll, att_date, status) in enumerate(records):
            Label(frame, text=f"{att_date}").grid(row=i+1, column=0)
            Label(frame, text=f"{name} ({roll})").grid(row=i+1, column=1)
            Label(frame, text=status).grid(row=i+1, column=2)

        Button(frame, text="Back", command=lambda: teacher_interface(root)).grid(row=len(records)+2, columnspan=3, pady=10)

    Button(frame, text="Mark Attendance", command=mark_attendance).grid(row=5, column=0, columnspan=2)
    Button(frame, text="View Attendance Sheet", command=view_attendance).grid(row=6, column=0, columnspan=2)
