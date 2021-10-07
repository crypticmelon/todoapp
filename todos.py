# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 875)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.052, y1:1, x2:0.763, y2:0.494, stop:0 rgba(204, 43, 94, 255), stop:1 rgba(117, 58, 136, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 191, 101))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.showdb)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QtCore.QRect(0, 290, 541, 381))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(340, 750, 111, 41))
        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    cleared = False
    def showdb(self):
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        str = ''
        str2 = ''
        self.tableWidget.setRowCount(50)
        tableindex = 0
        amount = len(cur.execute('SELECT * FROM task').fetchall())
        if amount > 0:
            for x in cur.execute('SELECT * FROM task'):
                str = ''.join(x[0])
                str2 = ''.join(x[1])
                self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str))
                self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(str2))
                tableindex += 1
        else:
            pass
    def clear(self):
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE task')
        cur.execute("""CREATE TABLE IF NOT EXISTS task
                     (title text, desc text);
                   """)
        conn.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoS"))
        self.label.setText(_translate("MainWindow", "Todos:"))
        self.pushButton.setText(_translate("MainWindow", u"Click to view your todos"))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(_translate("MainWindow", u"Title", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(_translate("MainWindow", u"Desc"))
        self.pushButton_2.setText(_translate("MainWindow", u"Clear "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
