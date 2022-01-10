from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Ui_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 150)# 禁止拉伸窗口大小

        MainWindow.setWindowIcon(QIcon('../image/logo.png'))
        MainWindow.setStyleSheet("background-image:url(../image/1.jpg)")

        self.centralWidget = QtWidgets.QWidget(MainWindow)#中心窗口部件
        self.centralWidget.setObjectName("centralWidget")

        self.line_Id = QtWidgets.QLineEdit(self.centralWidget)
        self.line_Id.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.line_Id.setText("")
        self.line_Id.setObjectName("line_Id")

        self.line_password = QtWidgets.QLineEdit(self.centralWidget)
        self.line_password.setGeometry(QtCore.QRect(250, 50, 100, 20))
        self.line_password.setText("")
        self.line_password.setObjectName("line_password")
        self.line_password.setEchoMode(QLineEdit.Password)#设置输入密码为圆点

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 12))
        self.label_2.setObjectName("label_2")

        self.btn_login = QtWidgets.QPushButton(self.centralWidget)
        self.btn_login.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.btn_login.setObjectName("btn_login")

        self.btn_register = QtWidgets.QPushButton(self.centralWidget)
        self.btn_register.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.btn_register.setObjectName("btn_register")

        MainWindow.setCentralWidget(self.centralWidget)

        # QStatusBar窗口状态栏,窗口底部的一个小条形图
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Message in Login.')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网关管理系统"))
        self.line_Id.setPlaceholderText(_translate("MainWindow", "请输入帐号"))#setPlaceholderText在输入内容之前，给予用户一些提示信息
        self.line_password.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))#setText设置文本信息
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.btn_login.setText(_translate("MainWindow", "登陆"))
        # self.btn_register.setText(_translate("MainWindow", "注册"))
        self.btn_register.setText(_translate("MainWindow", "取消"))
