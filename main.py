import os.path
import sqlite3
from graphics import Ui_MainWindow
from PyQt5 import QtWidgets
import sys





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
window = Ui_MainWindow()
window.setupUi(MainWindow)
MainWindow.show()

dbFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'students.db'))


def create_connection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Exception as e:
        print(e)

    return conn

def getAll(dbFile):
    conn = create_connection(dbFile)

    get_all = "SELECT * FROM students"

    try:

        c = conn.cursor()
        c.execute(get_all)
        return c
    except Exception as e:
        print(e)


window.display(getAll(dbFile))

sys.exit(app.exec_())
