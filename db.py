<<<<<<< HEAD
import sqlite3

def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_class TEXT,
            contact TEXT
        )
    ''')

    # Teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Attendance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT
        )
    ''')

    # Requests table for student issues
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            issue TEXT
        )
    ''')

    # Add default admin (if not exists)
    cursor.execute("SELECT * FROM teachers WHERE email='admin@admin.com'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO teachers (name, email, password) VALUES (?, ?, ?)",
                       ('Admin', 'admin@admin.com', 'admin123'))

    conn.commit()
    conn.close()
=======
import sqlite3
def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_class TEXT,
            contact TEXT
        )
    ''')

    # Create Teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Check if admin exists
    cursor.execute("SELECT * FROM teachers WHERE email='admin@admin.com'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO teachers (name, email, password) VALUES (?, ?, ?)",
                       ('Admin', 'admin@admin.com', 'admin123'))

    conn.commit()
    conn.close()
>>>>>>> 6a6cee2d7872b6b63def9724b276ce29d927e8cd
