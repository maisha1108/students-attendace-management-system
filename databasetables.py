import mysql_connection

def setup():
    db = mysql_connection.connect()
    cursor = db.cursor()

    cursor.execute("USE students_attendance6")
    # Add your SQL creation commands here, same as above if needed

    db.commit()
    db.close()
