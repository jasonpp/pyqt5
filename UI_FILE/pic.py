# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import concurrent.futures
import asyncio
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_FILE.Utils.Selenium_Tutorial_0522 import search_2
from UI_FILE.Utils.Selenium_Tutorial_0523 import search_1
from UI_FILE.Utils.Selenium_Tutorial_0523_1 import search_3

now = lambda :time.time()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 933)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 30, 171, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/maoyan.png"))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 220, 871, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.listView = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.listView_2 = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout.addWidget(self.listView_2, 1, 1, 1, 1)
        self.listView_3 = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout.addWidget(self.listView_3, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 800, 171, 71))
        self.pushButton.setStyleSheet("image: url(:/button.png);\n"
"background-color: transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        # Setup the signal
        self.pushButton.clicked.connect(self.onClick)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "即将上映电影"))
        self.label_4.setText(_translate("MainWindow", "电影100强"))
        self.label_2.setText(_translate("MainWindow", "最新电影"))


    # Setup the slot
    def onClick(self):

        self.fetch1()
        self.fetch2()
        self.fetch3()


    def fetch1(self):
        # 1. Initial list string model
        slm1 = QStringListModel()
        # 2. Setup the list
        resultList_1 = search_1()
        slm1.setStringList(resultList_1)
        # 3. Fill data with list data
        self.listView.setModel(slm1)


    def fetch2(self):
        slm2 = QStringListModel()

        resultList_2 = search_2()

        slm2.setStringList(resultList_2)

        self.listView_2.setModel(slm2)

    def fetch3(self):
        slm3 = QStringListModel()

        resultList_3 = search_3()

        slm3.setStringList(resultList_3)

        self.listView_3.setModel(slm3)



    # def initialCoroutine(self):
    #     loop = asyncio.get_event_loop()
    #     futus = [
    #         asyncio.ensure_future(self.fetch1()),
    #         asyncio.ensure_future(self.fetch2()),
    #         asyncio.ensure_future(self.fetch3())
    #     ]
    #     loop.run_until_complete(asyncio.gather(*futus))



from UI_FILE import pic_rc

if __name__ == '__main__':

    app  = QApplication(sys.argv)

    window = QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(window)

    window.show()

    app.exec(app.exec())

