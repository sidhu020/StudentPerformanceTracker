# Student Tracker Class
# This class manages all students

from student import Student


class StudentTracker:

    def __init__(self):

        # list to store student objects
        self.students = []

        # first i was using dictionary
        # but list is easy to understand

    # add new student
    def add_student(self, name, roll_number):

        # checking roll number already exists

        for student in self.students:

            if student.roll_number == roll_number:
                return False

        new_student = Student(name, roll_number)

        self.students.append(new_student)

        return True


    # find student using roll number
    def find_student(self, roll_number):

        for student in self.students:

            if student.roll_number == roll_number:
                return student

        return None


    # add marks to student
    def add_grades(self, roll_number, subject, marks):

        student = self.find_student(roll_number)

        if student != None:

            student.add_grade(subject, marks)

            return True

        else:
            return False



    # show student details
    def view_student_details(self, roll_number):

        student = self.find_student(roll_number)

        if student != None:

            student.display_info()

        else:

            print("Student not found")



    # calculate average of student
    def calculate_average(self, roll_number):

        student = self.find_student(roll_number)

        if student != None:

            return student.calculate_average()

        else:

            return -1



    # display all students
    def show_all_students(self):

        if len(self.students) == 0:

            print("No students available")

        else:

            for student in self.students:

                student.display_info()