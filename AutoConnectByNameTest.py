import sys
from PyQt4 import QtGui, QtCore

class CustomButton(QtGui.QPushButton):
    custom_clicked = QtCore.pyqtSignal(str, name='customClicked')
    def mousePressEvent(self, event):
        self.custom_clicked.emit("Clicked!")

class SignalsAndSlots(QtGui.QWidget):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        layout = QtGui.QHBoxLayout(self)
        self.custom_button = CustomButton("Press Me", self)
        self.custom_button.setObjectName('customButton')
        self.label = QtGui.QLabel("Nothing...", parent=self)
        layout.addWidget(self.custom_button)
        layout.addWidget(self.label)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot(str, name='on_customButton_customClicked')
    def autoSlot(self, msg):
        self.label.setText(msg)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = SignalsAndSlots()
    gui.show()
    app.exec_()