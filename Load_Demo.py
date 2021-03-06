# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Load_Demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
class Ui_Load_lineEdit(object):
    def setupUi(self, Load_lineEdit):
        Load_lineEdit.setObjectName("Load_lineEdit")
        Load_lineEdit.resize(1021, 766)
        self.label = QtWidgets.QLabel(Load_lineEdit)
        self.label.setGeometry(QtCore.QRect(0, 0, 1021, 771))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/load.png"))
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.lineEdit_user = QtWidgets.QLineEdit(Load_lineEdit)
        self.lineEdit_user.setGeometry(QtCore.QRect(395, 320, 271, 46))
        self.lineEdit_user.setMaximumSize(QtCore.QSize(16777215, 46))
        self.lineEdit_user.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_user.setTabletTracking(False)
        self.lineEdit_user.setStyleSheet("QLineEdit\n"
"{           \n"
"    font: 14pt \"3ds\";\n"
"    background:url(:/pic/images/account_2.jpg);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{           \n"
"    background:url(:/pic/images/account.jpg);\n"
"}\n"
"")
        self.lineEdit_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_user.setDragEnabled(True)
        self.lineEdit_user.setPlaceholderText("")
        self.lineEdit_user.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_user.setClearButtonEnabled(True)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(Load_lineEdit)
        self.lineEdit_password.setGeometry(QtCore.QRect(395, 388, 271, 46))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 46))
        self.lineEdit_password.setStyleSheet("QLineEdit\n"
"{           \n"
"    font: 14pt \"3ds\";\n"
"    background:url(:/pic/images/password_1.jpg);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{           \n"
"    background:url(:/pic/images/password.jpg);\n"
"}\n"
"")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_enter = QtWidgets.QPushButton(Load_lineEdit)
        self.pushButton_enter.setGeometry(QtCore.QRect(345, 460, 151, 46))
        self.pushButton_enter.setStyleSheet("QPushButton\n"
"{\n"
"    background:url(:/pic/images/load_1.jpg);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background:url(:/pic/images/load_2.jpg);\n"
"}\n"
"")
        self.pushButton_enter.setText("")
        self.pushButton_enter.setCheckable(False)
        self.pushButton_enter.setChecked(False)
        self.pushButton_enter.setAutoRepeat(False)
        self.pushButton_enter.setAutoExclusive(False)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_close = QtWidgets.QPushButton(Load_lineEdit)
        self.pushButton_close.setGeometry(QtCore.QRect(515, 460, 151, 46))
        self.pushButton_close.setStyleSheet("QPushButton\n"
"{\n"
"    background:url(:/pic/images/close_1.jpg);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background:url(:/pic/images/close_2.jpg);\n"
"}\n"
"")
        self.pushButton_close.setText("")
        self.pushButton_close.setCheckable(False)
        self.pushButton_close.setChecked(False)
        self.pushButton_close.setAutoRepeat(False)
        self.pushButton_close.setAutoExclusive(False)
        self.pushButton_close.setObjectName("pushButton_close")

        self.retranslateUi(Load_lineEdit)
        QtCore.QMetaObject.connectSlotsByName(Load_lineEdit)

    def retranslateUi(self, Load_lineEdit):
        _translate = QtCore.QCoreApplication.translate
        Load_lineEdit.setWindowTitle(_translate("Load_lineEdit", "Load"))
        self.lineEdit_user.setText(_translate("Load_lineEdit", "user"))
        self.lineEdit_password.setText(_translate("Load_lineEdit", "1234"))

import apprcc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setWindowIcon(QIcon('images/logo.ico'))
    ui = Ui_Load_lineEdit()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())