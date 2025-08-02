# Database configuration - import this in all files
import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='students_attendance3'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None