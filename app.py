# Main Flask Application
# Student Performance Tracker
# Simple BCA project


from flask import Flask, render_template, request

import database


app = Flask(__name__)


# creating database tables when program starts

database.create_tables()



# Home page

@app.route("/")
def home():

    students = database.get_all_students_db()

    return render_template(
        "index.html",
        students=students
    )





# Add Student Page

@app.route("/add_student", methods=["GET","POST"])
def add_student():

    message = ""


    if request.method == "POST":

        name = request.form["name"]

        roll = request.form["roll"]


        result = database.add_student_db(
            name,
            roll
        )


        if result:

            message = "Student Added Successfully"

        else:

            message = "Roll Number Already Exists"



    return render_template(
        "add_student.html",
        message=message
    )







# Add Grades Page

@app.route("/add_grades", methods=["GET","POST"])
def add_grades():


    message = ""


    if request.method == "POST":


        roll = request.form["roll"]

        subject = request.form["subject"]

        marks = request.form["marks"]



        # converting marks into number

        try:

            marks = int(marks)


            if marks < 0 or marks > 100:

                message = "Marks should be between 0 and 100"


            else:


                student = database.get_student_db(roll)


                if student:

                    database.add_grade_db(
                        roll,
                        subject,
                        marks
                    )

                    message = "Grade Added"


                else:

                    message = "Student Not Found"



        except:

            message = "Invalid Marks"



    return render_template(
        "add_grades.html",
        message=message
    )







# View Student Details

@app.route("/view_student", methods=["GET","POST"])
def view_student():


    student = None

    grades = []

    average = 0



    if request.method == "POST":


        roll = request.form["roll"]



        student = database.get_student_db(roll)



        if student:


            grades = database.get_grades_db(roll)



            if len(grades) > 0:


                total = 0


                for g in grades:

                    total = total + g[1]


                average = total / len(grades)



    return render_template(
        "view_student.html",
        student=student,
        grades=grades,
        average=average
    )








# Average Page

@app.route("/average")

def average():


    students = database.get_all_students_db()


    result = []


    for s in students:


        grades = database.get_grades_db(
            s[2]
        )


        total = 0


        for g in grades:

            total = total + g[1]



        if len(grades) > 0:

            avg = total / len(grades)

        else:

            avg = 0



        result.append(
            (
                s[1],
                s[2],
                avg
            )
        )



    return render_template(
        "average.html",
        result=result
    )






# Start program

if __name__ == "__main__":


    app.run(
        host="0.0.0.0",
        port=5000
    )