# Student Performance Tracker

## Project Title

**Student Performance Tracker**

---

## Project Description

Student Performance Tracker is a Python Flask based web application developed to help teachers manage student academic records.

The application allows teachers to add student details, assign subject-wise grades, view student performance, and calculate average marks.

The project uses Python concepts like Object-Oriented Programming (OOP), functions, loops, conditional statements, Flask framework, and SQLite database integration.

---

# Objectives

The main objectives of this project are:

- To store student information digitally.
- To manage subject-wise student grades.
- To calculate average performance of students.
- To provide a simple web interface for teachers.
- To learn Flask web development and database integration.

---

# Technologies Used

## Programming Language

- Python

## Framework

- Flask

## Database

- SQLite

## Frontend

- HTML
- CSS

## Deployment

- Render Cloud Platform

---

# Features

## 1. Add Students

Teachers can add new students with:

- Student Name
- Roll Number


Example:


Name:
Rahul Patel

Roll Number:
101


---

## 2. Add Grades

Teachers can add marks for different subjects.

Supported examples:

- Mathematics
- Science
- English


Example:


Roll Number:
101

Subject:
Math

Marks:
90


The application checks that marks are between 0 and 100.

---

## 3. View Student Details

Teachers can search students using their roll number.

The system displays:

- Student name
- Roll number
- Subject marks
- Average marks


Example:


Name: Rahul Patel

Math 90
Science 80
English 85

Average: 85


---

## 4. Class Average Report

The application calculates average marks of all students.

Example:


Name Roll Number Average

Rahul 101 85

Amit 102 75


---

# Project Structure


StudentPerformanceTracker/

│
├── app.py
│ Main Flask application
│
├── student.py
│ Student class implementation
│
├── tracker.py
│ Student management class
│
├── database.py
│ SQLite database functions
│
├── requirements.txt
│ Required Python packages
│
├── Procfile
│ Deployment configuration
│
├── README.md
│ Project documentation
│
├── students.db
│ SQLite database file
│
├── templates/
│
│ ├── index.html
│ ├── add_student.html
│ ├── add_grades.html
│ ├── view_student.html
│ └── average.html
│
└── static/

└── style.css

---

# Installation Guide

## Step 1: Download Project

Download or clone this project.

Open terminal inside the project folder.

---

## Step 2: Install Required Packages

Run:


pip install -r requirements.txt


---

## Step 3: Run Application

Start the Flask server:


python app.py


---

## Step 4: Open Website

Open browser and visit:


http://127.0.0.1:5000


---

# How To Use Application

## Add Student

1. Open the home page.
2. Click on "Add Student".
3. Enter student name and roll number.
4. Click submit.

The student will be stored in the database.

---

## Add Grades

1. Click "Add Grades".
2. Enter student roll number.
3. Enter subject name.
4. Enter marks between 0 and 100.
5. Submit the form.

---

## View Student Report

1. Open "View Student".
2. Enter roll number.
3. Click search.

The complete performance report will be displayed.

---

## View Average Report

1. Open "Class Average".
2. The system will display average marks of all students.

---

# Database Information

The project uses SQLite database.

Database name:


students.db


Two tables are created:

## Students Table

Stores:

- Student ID
- Name
- Roll Number


## Grades Table

Stores:

- Grade ID
- Roll Number
- Subject
- Marks

---

# Object-Oriented Design

## Student Class

The Student class contains:

Attributes:

- name
- roll_number
- grades


Methods:

- add_grade()
- calculate_average()
- display_info()


## StudentTracker Class

The StudentTracker class manages multiple students.

Methods:

- add_student()
- add_grades()
- view_student_details()
- calculate_average()

---

# Deployment

The application can be deployed using Render.

Deployment files included:


requirements.txt

Procfile


Start command:


python app.py


---

# Future Improvements

The following features can be added in future:

- Student login system
- Teacher login system
- Subject-wise topper calculation
- Export reports as PDF
- Email notifications
- Better user interface design
- MySQL database integration

---

# Conclusion

Student Performance Tracker provides an easy way to manage student academic records.

This project demonstrates the practical use of Python programming, Object-Oriented Programming, Flask web development, and database management.

---

# Author

BCA Student Mini Project

Project: Student Performance Tracker