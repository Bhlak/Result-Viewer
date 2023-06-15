import os.path
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic



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


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.headerList = ['S/N', "Name", "Matric No.", "Grade", 'TCP', 'TNU', 'GPA', 'Remarks']
    
    def display(self, rows):
        self.tableWidget.setColumnCount(len(self.headerList))
        self.tableWidget.horizontalHeader
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for row in rows:
            rowPosition = self.tableWidget.rowCount()

            if rowPosition > row[0]:
                continue

            itemCount = 0
            self.tableWidget.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            self.tableWidget.setHorizontalHeaderLabels(self.headerList)

            for item in row:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.display(getAll(dbFile))
    sys,exit(app.exec_())


