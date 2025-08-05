from tkinter import *
import mysql_connection

def student_interface(root, roll):
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    frame = Frame(root)
    frame.pack()

    db = mysql_connection.connect()
    cursor = db.cursor()

    # Find student by roll number
    cursor.execute("SELECT id, name FROM students WHERE roll = %s", (roll,))
    student = cursor.fetchone()

    if not student:
        Label(frame, text=f"❌ Student record not found for roll '{roll}'", fg="red").pack()
        db.close()
        return

    student_id, name = student

    Label(frame, text=f"Welcome {name} (Roll: {roll})", font=("Arial", 14, "bold")).pack(pady=10)
    Label(frame, text="Attendance Records:", font=("Arial", 12, "underline")).pack(pady=5)

    cursor.execute("SELECT date, status FROM attendance WHERE student_id = %s ORDER BY date DESC", (student_id,))
    records = cursor.fetchall()

    if not records:
        Label(frame, text="No attendance records found.").pack()
    else:
        for date, status in records:
            Label(frame, text=f"{date} ➤ {status}").pack(anchor="w")

    Label(frame, text="").pack()  # spacer
    Label(frame, text="Request Attendance Correction", font=("Arial", 12, "bold")).pack()

    Label(frame, text="Date (YYYY-MM-DD):").pack()
    date_entry = Entry(frame, width=30)
    date_entry.pack()

    Label(frame, text="Reason:").pack()
    reason_entry = Entry(frame, width=50)
    reason_entry.pack()

    status_label = Label(frame, text="", fg="green")
    status_label.pack()

    def submit_request():
        date = date_entry.get().strip()
        reason = reason_entry.get().strip()
        if not date or not reason:
            status_label.config(text="Please fill in all fields.", fg="red")
            return
        try:
            cursor.execute("INSERT INTO requests (student_id, date, reason) VALUES (%s, %s, %s)",
                           (student_id, date, reason))
            db.commit()
            status_label.config(text="Request submitted successfully!", fg="green")
            date_entry.delete(0, END)
            reason_entry.delete(0, END)
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")

    Button(frame, text="Submit Request", command=submit_request, bg="lightblue").pack(pady=5)

    # Don't close DB here because it's used in submit_request
    # Instead, close when app is exited or window is destroyed
