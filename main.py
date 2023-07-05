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


def convert(file):
    rows = []
    for row in getAll(file):
        rows.append(row)
    return rows

def calculation(list, num):
    if num == 0:
        return list[0] + list[3]
    elif num == 1:
        return list[1] + list[4]
    elif num == 2:
        return round((list[0] + list[3]) / (list[1] + list[4]), 2)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.headerList = ['S/N', "Name", "Matric No.", "Grade", 'TCP', 'TNU', 'GPA', 'Remarks']
    
    def display(self, rows):   # First Table
        self.tableWidget.setColumnCount(len(self.headerList[:4]))
        self.tableWidget.horizontalHeader
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(self.headerList[:4])

        self.tableWidget4.setColumnCount(1)
        self.tableWidget4.horizontalHeader
        self.tableWidget4.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget4.setHorizontalHeaderLabels(self.headerList[7:])
        
        rowPosition = self.tableWidget.rowCount()

        row = ['', '', '', '']
        self.tableWidget.setRowCount(rowPosition + 1)
        self.tableWidget.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())
        self.tableWidget4.setRowCount(rowPosition + 1)
        self.tableWidget4.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        itemCount = 0
        for item in row:
            if itemCount == 0 and rowPosition == 0:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                self.tableWidget4.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.tableWidget4.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText('')

            self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
            self.qtablewidgetitem = self.tableWidget.item(rowPosition, itemCount)
            self.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1
        for row in rows:
            if (rowPosition > row[0]):
                continue            

            self.tableWidget.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            self.tableWidget4.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget4.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            
            itemCount = 0
            for item in row:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                
                if itemCount in [4, 5, 6, 7, 8, 9]:
                    itemCount += 1
                    continue
                
                elif itemCount == 10:
                    tw = self.tableWidget4
                    tw.setItem(rowPosition, 0, self.qtablewidgetitem)
                    self.qtablewidgetitem = tw.item(rowPosition, 0)
                    self.qtablewidgetitem.setText(str(item))
                    break
                
                self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setMinimumHeight(self.tableWidget.horizontalHeader().height() + (self.tableWidget.rowHeight(0) * self.tableWidget.rowCount()))
        self.tableWidget.setMaximumHeight(self.tableWidget.minimumHeight())

        self.tableWidget4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget4.setMinimumHeight(self.tableWidget.minimumHeight())
        self.tableWidget4.setMaximumHeight(self.tableWidget4.minimumHeight())

    def display_previous(self, rows): #Previous Scores Table
        tw = self.tableWidget1
        tw.setColumnCount(3)
        tw.horizontalHeader
        tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tw.setHorizontalHeaderLabels(self.headerList[4:7])

        rowPosition = tw.rowCount()

        tw.setRowCount(rowPosition + 1)
        tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        itemCount = 0
        for item in self.headerList[4:7]:
            self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
            self.qtablewidgetitem = tw.item(rowPosition, itemCount)
            self.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1

        for row in rows:
            row = row[4:7]

            tw.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            itemCount = 0
            for item in row:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = tw.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1

        tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
        tw.setMaximumHeight(tw.minimumHeight())

    def display_present(self, rows): #Present Scores Table
        tw = self.tableWidget2
        tw.setColumnCount(3)
        tw.horizontalHeader
        tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tw.setHorizontalHeaderLabels(self.headerList[4:7])

        rowPosition = tw.rowCount()

        tw.setRowCount(rowPosition + 1)
        tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        itemCount = 0
        for item in self.headerList[4:7]:
            self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
            self.qtablewidgetitem = tw.item(rowPosition, itemCount)
            self.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1

        for row in rows:
            row = row[7:10]

            tw.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            itemCount = 0
            for item in row:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = tw.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1

        tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
        tw.setMaximumHeight(tw.minimumHeight())

    def display_cummulative(self, rows):
        tw = self.tableWidget3
        tw.setColumnCount(3)
        tw.horizontalHeader
        tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tw.setHorizontalHeaderLabels(self.headerList[4:7])

        rowPosition = tw.rowCount()

        tw.setRowCount(rowPosition + 1)
        tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        itemCount = 0
        for item in self.headerList[4:7]:
            self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
            self.qtablewidgetitem = tw.item(rowPosition, itemCount)
            self.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1

        for row in rows:
            row = row[4:10]

            tw.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            itemCount = 0
            for item in row:
                if itemCount > 2:
                    break
                item = calculation(row, itemCount)
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = tw.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1

        tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
        tw.setMaximumHeight(tw.minimumHeight())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    rows = convert(dbFile)
    # print(rows)
    window.display(rows)
    window.display_previous(rows)
    window.display_present(rows)
    window.display_cummulative(rows)
    sys,exit(app.exec_())


