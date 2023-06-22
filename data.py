import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

db_file = "students.db"

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def filter_by_matric_no():
    conn = create_connection(db_file)
    cursor = conn.cursor()

    query = "SELECT * FROM students ORDER BY matric_no"
    cursor.execute(query)
    rows = cursor.fetchall()

    display_results(rows)

    conn.close()


def sort_by_cgpa():
    conn = create_connection(db_file)
    cursor = conn.cursor()

    query = "SELECT * FROM students ORDER BY gpa DESC"
    cursor.execute(query)
    rows = cursor.fetchall()

    display_results(rows)

    conn.close()

def display_results(rows):
    result_tree.delete(*result_tree.get_children())  # Clear previous results

    for student in rows:
        result_tree.insert('', tk.END, values=student[1:])

# Create GUI
root = tk.Tk()
root.title("Student Results Filter")

# Filter by Matric No. Frame
matric_frame = tk.Frame(root)
matric_frame.pack()

label_start_matric = tk.Label(matric_frame, text="Start Matric No:")
label_start_matric.pack(side=tk.LEFT)
entry_start_matric = tk.Entry(matric_frame)
entry_start_matric.pack(side=tk.LEFT)

label_end_matric = tk.Label(matric_frame, text="End Matric No:")
label_end_matric.pack(side=tk.LEFT)
entry_end_matric = tk.Entry(matric_frame)
entry_end_matric.pack(side=tk.LEFT)

filter_matric_button = tk.Button(root, text="Filter by Matric No.", command=filter_by_matric_no)
filter_matric_button.pack()

# Sort by CGPA Button
sort_cgpa_button = tk.Button(root, text="Sort by CGPA", command=sort_by_cgpa)
sort_cgpa_button.pack()

# Results Table
columns = ("Name", "Matric No.", "Grade", "TCP", "TNU", "GPA", "Remarks")
result_tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    result_tree.heading(col, text=col)
    result_tree.column(col, width=100)

result_tree.pack()

root.mainloop()
