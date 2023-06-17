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
        self.tableWidget.setHorizontalHeaderLabels(self.headerList)
        rowPosition = self.tableWidget.rowCount()
        for row in rows:
            print(f'Row Data: {row}')
        

            if (rowPosition > row[0]):
                continue
            # elif rowPosition == 0:
            #     rowPosition += 1
            

            self.tableWidget.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            if rowPosition == 0:
                itemCount = 0
                for item in row:
                    if itemCount != 4 and itemCount != 5 and itemCount != 6:
                        self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                        # self.qtablewidgetitem = self.tableWidget.item(rowPosition, itemCount)
                        # self.qtablewidgetitem.setText("Test")
                        itemCount += 1
                        continue
                    self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                    print(f"ItemCount: {itemCount}, RowPositon: {rowPosition}")
                    self.qtablewidgetitem = self.tableWidget.item(rowPosition, itemCount)
                    print("Item put: ",self.qtablewidgetitem)
                    self.qtablewidgetitem.setText(str(item))

                    itemCount += 1
                rowPosition += 1
                continue
                
            itemCount = 0
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


