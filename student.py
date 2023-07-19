import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Step 1: Install Required Libraries

# Step 2: Design the GUI
# Implement your GUI design here using PyQt5

# Step 3: Set Up the Database
connection = sqlite3.connect(r"C:\Users\Ayokanmi\Downloads\Compressed\Result-Viewer-Ibk_1\Summary\main.db")
cursor = connection.cursor()

# Step 8: Senate Summary
def display_senate_summary(matric_no):
    # Fetch data from the "registration" table
    cursor.execute("SELECT CourseCodes FROM Registration WHERE MatricNo=(?)", (matric_no,))
    registration_data = cursor.fetchall()

    # Create a table to display the senate summary
    table_widget = QtWidgets.QTableWidget()
    table_widget.setColumnCount(3)  # Adjust the number of columns as per your requirement
    table_widget.setHorizontalHeaderLabels(["CourseCdoe", "Course Details", "Units"])

    # Create a dictionary to store course details for each course
    student_courses = {}

    # Process registration data
    courseCode = [i.split(',') for i in registration_data[0]][0]

    # Fetch course details for the course code
    for i in courseCode:
        cursor.execute("SELECT CourseCode, CourseName, CourseUnits FROM o_Courses WHERE CourseCode=(?)", (i,))
        course_data = [i for i in cursor.fetchall()[0]]

        code = course_data[0]
        details = course_data[1:]


        if code not in student_courses:
            student_courses[code] = []
        student_courses[code].extend(details)
    


    # Populate the table with student course details
    row = table_widget.rowCount()

    for code, details in student_courses.items():
        table_widget.setRowCount(row + 1)

        code_item = QtWidgets.QTableWidgetItem(code)
        table_widget.setItem(row, 0, code_item)

        for i in range(1, 3):
            course_details_item = QtWidgets.QTableWidgetItem()
            course_details_item.setText(str(details[i - 1]))
            table_widget.setItem(row, i, course_details_item)

        row += 1

    # Show the table in the GUI
    layout.addWidget(table_widget)

# Step 2: Design the GUI (continued)
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# Create the main layout
layout = QtWidgets.QVBoxLayout()

# Call the function to display the senate summary
display_senate_summary('EU180303-1628')

# Create the central widget and set the layout
central_widget = QtWidgets.QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())

# Step 9: Database Operations
connection.close()
