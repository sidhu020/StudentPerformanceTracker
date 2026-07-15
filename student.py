# Student Class
# stores one student information

class Student:

    # constructor
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

        # grades will be stored like
        # {"Math":90,"Science":80}
        self.grades = {}

    # add subject marks
    def add_grade(self, subject, marks):

        # first i was thinking list
        # dictionary is easier

        self.grades[subject] = marks

    # calculate average marks
    def calculate_average(self):

        if len(self.grades) == 0:
            return 0

        total = 0

        for mark in self.grades.values():
            total = total + mark

        average = total / len(self.grades)

        return average

    # display student information
    def display_info(self):

        print("----------------------------")
        print("Name :", self.name)
        print("Roll :", self.roll_number)

        print("Grades:")

        if len(self.grades) == 0:
            print("No grades added.")

        else:
            for subject, marks in self.grades.items():
                print(subject, ":", marks)

        print("Average :", self.calculate_average())
        print("----------------------------")