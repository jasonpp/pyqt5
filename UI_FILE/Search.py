# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Get.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import time
import _thread
import urllib.request
from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox

from UI_FILE.Utils.Net import getRealUrl


class Ui_MainWindow(object):

    url_link = None
    input_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 775)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 130, 821, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 25, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("TradeGothic LT")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("TradeGothic LT")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("TradeGothic LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("TradeGothic LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("TradeGothic LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Setup the signal
        self.pushButton.clicked.connect(self.downloadVideo)
        self.pushButton_2.clicked.connect(self.getUrlAndCopy)
        self.pushButton_3.clicked.connect(self.choosePath)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">万能视频解析下载</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "请输入网络视频地址:"))
        self.label_2.setText(_translate("MainWindow", "视频下载地址:"))
        self.pushButton_3.setText(_translate("MainWindow", "下载路径选择"))
        self.pushButton.setText(_translate("MainWindow", "下载视频"))
        self.pushButton_2.setText(_translate("MainWindow", "获取下载地址并复制到剪贴板"))


    def getUrlAndCopy(self):
        if self.textEdit.toPlainText() == "":
            self.msg()
        else:
          str = self.textEdit.toPlainText()
          self.url_link = getRealUrl(str)
          print(self.url_link)
          self.textEdit_2.setText(self.url_link)
          self.textEdit_2.selectAll()
          self.textEdit_2.copy()



    def downloadVideo(self):

        if  self.textEdit.toPlainText() == "":
            self.msg()
        elif self.input_path != None:
            content = self.textEdit.toPlainText()
            self.url_link = getRealUrl(content)
            urllib.request.urlretrieve(self.url_link,self.input_path +'/'+str(round(time.time()))+'.mp4')
        else:
            content = self.textEdit.toPlainText()
            self.url_link = getRealUrl(content)

            _thread.start_new_thread(self.runn)


    def choosePath(self):
       self.input_path = QFileDialog.getExistingDirectory(None,'请选择文件夹',expanduser("~"))
       print(self.input_path)

    def msg(self):
        infoBox = QMessageBox()  ##Message Box that doesn't run
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("地址栏不能为空")
        infoBox.setWindowTitle("警告")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()

    def runn(self):
        try:
            urllib.request.urlretrieve(self.url_link, 'D:/' + str(round(time.time())) + '.mp4')
        except Exception as e:
            print(e)


if __name__ == '__main__':

    app  = QApplication(sys.argv)

    window = QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())