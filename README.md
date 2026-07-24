# 🎓 Student Performance Tracker

> A **Flask-based Student Performance Tracker** developed as an **MCA Mini Project** to help teachers manage student records, subject-wise grades, and academic performance efficiently.

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render)](https://studentperformancetracker-nqyc.onrender.com)

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/sidhu020/StudentPerformanceTracker)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![HTML](https://img.shields.io/badge/Frontend-HTML-orange?logo=html5)
![CSS](https://img.shields.io/badge/Style-CSS-blue?logo=css3)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Table of Contents

- 📌 Project Overview
- 🎯 Objectives
- ✨ Features
- 🛠️ Technologies Used
- 📂 Project Structure
- ⚙️ Installation Guide
- 🚀 Running the Application
- 💻 Usage
- 🗄️ Database Design
- 🏗️ Object-Oriented Design
- 🎥 Project Demonstration
- 🌐 Deployment
- 🔮 Future Enhancements
- 🤝 Contributing
- 👨‍💻 Author
- 📄 License

---

# 📌 Project Overview

**Student Performance Tracker** is a web application developed using **Python Flask** and **SQLite**. It allows teachers to digitally manage student information, assign subject-wise marks, and generate academic reports.

This project demonstrates the practical implementation of:

- 🐍 Python Programming
- 🧩 Object-Oriented Programming (OOP)
- 🌐 Flask Web Framework
- 🗄️ SQLite Database
- 🎨 HTML & CSS
- ☁️ Cloud Deployment (Render)

---

# 🎯 Objectives

The main objectives of this project are:

- ✅ Store student information digitally
- ✅ Manage subject-wise grades
- ✅ Calculate average marks automatically
- ✅ Generate performance reports
- ✅ Learn Flask web development
- ✅ Practice database integration using SQLite

---

# ✨ Features

## 👨‍🎓 Student Management

- Add new students
- Store student name
- Store roll number

Example:

| Name | Roll Number |
|------|-------------|
| Rahul Patel | 101 |

---

## 📝 Grade Management

Teachers can assign marks for multiple subjects.

Supported Subjects:

- Mathematics
- Science
- English
- Computer
- Any Custom Subject

Example:

| Roll No | Subject | Marks |
|---------|----------|-------|
|101|Math|90|

✔ Validation included

- Marks must be between **0–100**

---

## 📊 Student Performance Report

Search any student using Roll Number.

The report displays:

- Student Name
- Roll Number
- Subject-wise Marks
- Average Marks

Example

| Subject | Marks |
|---------|------|
|Math|90|
|Science|80|
|English|85|

Average

> **85%**

---

## 📈 Class Average Report

Displays average marks of all students.

Example

| Student | Roll No | Average |
|----------|---------|----------|
|Rahul|101|85|
|Amit|102|75|

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
|🐍 Python|Backend Programming|
|🌐 Flask|Web Framework|
|🗄 SQLite|Database|
|🎨 HTML5|Frontend|
|💙 CSS3|Styling|
|☁ Render|Deployment|

---

# 📂 Project Structure

```text
StudentPerformanceTracker/
│
├── app.py                  # Main Flask Application
├── student.py              # Student Class
├── tracker.py              # Student Management Logic
├── database.py             # SQLite Database Functions
├── students.db             # SQLite Database
├── requirements.txt        # Required Packages
├── Procfile                # Deployment Configuration
├── README.md               # Documentation
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── add_grades.html
│   ├── view_student.html
│   └── average.html
│
└── static/
    └── style.css
```

---

# ⚙️ Installation Guide

## Step 1️⃣ Clone Repository

```bash
git clone https://github.com/sidhu020/StudentPerformanceTracker.git
```

or download ZIP.

---

## Step 2️⃣ Navigate into Project

```bash
cd StudentPerformanceTracker
```

---

## Step 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4️⃣ Run Flask Application

```bash
python app.py
```

---

## Step 5️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

# 🚀 Usage Guide

## ➕ Add Student

- Open Home Page
- Click **Add Student**
- Enter Student Name
- Enter Roll Number
- Submit

Student is saved into the database.

---

## 📝 Add Grades

- Open Add Grades
- Enter Roll Number
- Enter Subject
- Enter Marks
- Submit

Validation:

```
Marks must be between 0 and 100.
```

---

## 🔍 View Student

- Open View Student
- Enter Roll Number
- Click Search

Displays:

- Student Details
- Subject Marks
- Average Marks

---

## 📈 View Class Average

Click

```
Class Average
```

Shows average marks of every student.

---

# 🗄️ Database Design

Database Name

```
students.db
```

## Students Table

| Field | Type |
|---------|------|
|id|INTEGER|
|name|TEXT|
|roll_number|INTEGER|

---

## Grades Table

| Field | Type |
|---------|------|
|id|INTEGER|
|roll_number|INTEGER|
|subject|TEXT|
|marks|INTEGER|

---

# 🏗️ Object-Oriented Design

## 📘 Student Class

### Attributes

- name
- roll_number
- grades

### Methods

```python
add_grade()
calculate_average()
display_info()
```

---

## 📗 StudentTracker Class

Responsible for managing all students.

Methods

```python
add_student()

add_grades()

view_student_details()

calculate_average()
```
---

# 🎥 Project Demonstration

## 📹 Demo Video

**Google Drive**

```
https://drive.google.com/file/d/1HtBsepgKJt01KGaWJFOC1dmz0QB_nZL5/view?usp=sharing
```

---

# 📄 Project Documentation

📘 Project Report (PDF)

```
docs/StudentPerformanceTracker_Report.pdf
```

📙 PPT Presentation

```
docs/Presentation.pptx
```

📑 UML Diagram

```
docs/UML_Diagram.pdf
```

📂 ER Diagram

```
docs/ER_Diagram.png
```

---

# 🌐 Deployment

The application is deployed on **Render Cloud Platform** and can be accessed online.

## 🚀 Live Application

https://studentperformancetracker-nqyc.onrender.com/

## 📂 Source Code

https://github.com/sidhu020/StudentPerformanceTracker

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
python app.py
```

---

# 🔮 Future Enhancements

- 🔐 Teacher Login
- 👨‍🎓 Student Login
- 📈 Subject-wise Topper
- 📥 Export PDF Reports
- 📧 Email Notifications
- 📊 Graphical Dashboard
- ☁ MySQL Integration
- 📱 Responsive UI
- 🌙 Dark Mode
- 📤 Excel Export

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Name:** *Siddharth*

🎓 MCA Student

🏫 *Department of Computer Science, Saurashtra University, Rajkot*

🔗 LinkedIn: https://www.linkedin.com/in/siddharthborisagar/

🐙 GitHub: https://github.com/sidhu020

---

# 🙏 Acknowledgements

Special thanks to:

- Flask Documentation
- Python Community
- SQLite Documentation
- Open Source Contributors

---

# 📄 License

This project is created for **academic and educational purposes**.

You are free to use and modify this project for learning.

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

## ❤️ Thank You

**Student Performance Tracker**

*A simple yet powerful academic management system built using Python Flask.*

**Made with ❤️ by an MCA Student**
