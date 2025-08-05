from tkinter import *
import mysql_connection

def admin_interface(root):
    frame = Frame(root)
    frame.pack()

    db = mysql_connection.connect()
    cursor = db.cursor()

    Label(frame, text="All Attendance Records").pack()

    cursor.execute("""
        SELECT students.name, students.roll, attendance.date, attendance.status 
        FROM attendance 
        JOIN students ON attendance.student_id = students.id
    """)
    records = cursor.fetchall()
    for rec in records:
        Label(frame, text=f"{rec[0]} ({rec[1]}) - {rec[2]} - {rec[3]}").pack()

    Label(frame, text="Pending Change Requests").pack()
    cursor.execute("""
        SELECT r.id, s.name, r.date, r.reason 
        FROM requests r
        JOIN students s ON r.student_id = s.id
        WHERE r.status = 'Pending'
    """)
    requests = cursor.fetchall()
    for rid, name, rdate, reason in requests:
        Label(frame, text=f"{name} | {rdate} | {reason}").pack()
