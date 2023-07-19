import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Step 1: Install Required Libraries

# Step 2: Design the GUI
# Implement your GUI design here using PyQt5

# Step 3: Set Up the Database
connection = sqlite3.connect(r"C:\Users\Ayokanmi\Downloads\Compressed\Result-Viewer-Ibk_1\Summary\main.db")
cursor = connection.cursor()

# Step 6: Display Departmental Summary
def display_departmental_summary():
    # Fetch data from the "registration" table
    cursor.execute("SELECT * FROM Registration")
    student_data = cursor.fetchall()

    # Create a table to display the departmental summary
    table_widget = QtWidgets.QTableWidget()
    table_widget.setColumnCount(3)  # Adjust the number of columns as per your requirement
    table_widget.setHorizontalHeaderLabels(["Matric No", "Course Code", "Grade"])

    # Populate the table with student data
    row = 0
    for student_row in student_data:
        matric_no = student_row[1]
        courses = student_row[2:]

        for i in range(len(courses) // 2):
            course_code = courses[i * 2]
            grade = courses[(i * 2) + 1]

            # Insert data into the table
            table_widget.insertRow(row)
            table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(matric_no))
            table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(course_code))
            table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(grade))

            row += 1

    # Show the table in the GUI
    layout.addWidget(table_widget)

# Step 2: Design the GUI (continued)
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# Create the main layout
layout = QtWidgets.QVBoxLayout()

# Call the function to display the departmental summary
display_departmental_summary()

# Create the central widget and set the layout
central_widget = QtWidgets.QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())

# Step 9: Database Operations
connection.close()
