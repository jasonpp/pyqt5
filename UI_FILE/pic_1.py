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
        self.pushButton.clicked.connect(self.runIt)


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

    # def listAllItems(self):
    #
    #     self.fetch1()
    #     #################################
    #
    #     self.fetch2()
    #
    #     #################################
    #
    #     self.fetch3()



    async def fetch1(self):
        start = now()
        # 1. Initial list string model
        # slm1 = QStringListModel()
        # 2. Setup the list
        await time.sleep(4)
        # slm1.setStringList(resultList_1)
        # 3. Fill data with list data
        # self.listView.setModel(slm1)
        print(now()-start)

    async def fetch2(self):
        start = now()
        # 1. Initial list string model
        # slm1 = QStringListModel()
        # 2. Setup the list
        await time.sleep(3)
        # slm1.setStringList(resultList_1)
        # 3. Fill data with list data
        # self.listView.setModel(slm1)
        print(now() - start)

    async def fetch3(self):
        start = now()
        # 1. Initial list string model
        # slm1 = QStringListModel()
        # 2. Setup the list
        await time.sleep(2)
        # slm1.setStringList(resultList_1)
        # 3. Fill data with list data
        # self.listView.setModel(slm1)
        print(now() - start)



        # coroutine1 = self.fetch1()
        # coroutine2 = self.fetch2()
        # coroutine3 = self.fetch3()
        # tasks = [
        #     asyncio.ensure_future(coroutine1),
        #     asyncio.ensure_future(coroutine2),
        #     asyncio.ensure_future(coroutine3)
        # ]
        # dones, pending = await asyncio.wait(tasks)

    async def main(self):
        await asyncio.gather(
            self.fetch1(),
            self.fetch2(),
            self.fetch3()
        )
    def runIt(self):
        start = now()
        asyncio.run(self.main())
        print(now() - start)






from UI_FILE import pic_rc

if __name__ == '__main__':

    app  = QApplication(sys.argv)

    window = QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(window)

    window.show()

    app.exec(app.exec())

