# Database File
# Using SQLite because it comes with Python
# No extra installation required


import sqlite3


DATABASE = "students.db"


# create connection
def get_connection():

    conn = sqlite3.connect(DATABASE)

    return conn



# create tables
def create_tables():

    conn = get_connection()

    cursor = conn.cursor()


    # student table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll_number INTEGER UNIQUE
    )
    """)


    # grades table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_number INTEGER,
        subject TEXT,
        marks INTEGER
    )
    """)


    conn.commit()

    conn.close()



# add student into database

def add_student_db(name, roll_number):

    try:

        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            "INSERT INTO students(name,roll_number) VALUES(?,?)",
            (name, roll_number)
        )


        conn.commit()

        conn.close()


        return True


    except:

        # duplicate roll number error comes here

        return False





# add grades into database

def add_grade_db(roll_number, subject, marks):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO grades(roll_number,subject,marks)
        VALUES(?,?,?)
        """,
        (roll_number, subject, marks)
    )


    conn.commit()

    conn.close()




# get one student information

def get_student_db(roll_number):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM students WHERE roll_number=?",
        (roll_number,)
    )


    student = cursor.fetchone()


    conn.close()


    return student





# get student grades

def get_grades_db(roll_number):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT subject,marks FROM grades WHERE roll_number=?",
        (roll_number,)
    )


    grades = cursor.fetchall()


    conn.close()


    return grades





# get all students

def get_all_students_db():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM students"
    )


    data = cursor.fetchall()


    conn.close()


    return data