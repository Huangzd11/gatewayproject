from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_registerPeople(object):
    def setupUi(self, registerPeople):
        registerPeople.setObjectName("registerPeople")
        registerPeople.setFixedSize(200, 200)

        registerPeople.setWindowIcon(QIcon('logo.png'))

        self.centralWidget = QtWidgets.QWidget(registerPeople)
        self.centralWidget.setObjectName("centralWidget")

        self.line_id = QtWidgets.QLineEdit(self.centralWidget)
        self.line_id.setGeometry(QtCore.QRect(60, 20, 120, 20))
        self.line_id.setText("")
        self.line_id.setObjectName("line_id")

        self.line_name = QtWidgets.QLineEdit(self.centralWidget)
        self.line_name.setGeometry(QtCore.QRect(60, 50, 120, 20))
        self.line_name.setText("")
        self.line_name.setObjectName("line_name")

        self.line_phone = QtWidgets.QLineEdit(self.centralWidget)
        self.line_phone.setGeometry(QtCore.QRect(60, 80, 120, 20))
        self.line_phone.setText("")
        self.line_phone.setObjectName("line_phone")

        self.line_password = QtWidgets.QLineEdit(self.centralWidget)
        self.line_password.setGeometry(QtCore.QRect(60, 110, 120, 20))
        self.line_password.setText("")
        self.line_password.setObjectName("line_password")

        self.re_line_password = QtWidgets.QLineEdit(self.centralWidget)
        self.re_line_password.setGeometry(QtCore.QRect(60, 140, 120, 20))
        self.re_line_password.setText("")
        self.re_line_password.setObjectName("re_line_password")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 54, 24, 12))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 84, 24, 12))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 114, 24, 12))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 144, 48, 12))
        self.label_5.setObjectName("label_5")

        self.btn_register = QtWidgets.QPushButton(self.centralWidget)
        self.btn_register.setGeometry(QtCore.QRect(80, 174, 75, 23))
        self.btn_register.setObjectName("btn_register")

        self.retranslateUi(registerPeople)
        QtCore.QMetaObject.connectSlotsByName(registerPeople)

    def retranslateUi(self, registerPeople):
        _translate = QtCore.QCoreApplication.translate
        registerPeople.setWindowTitle(_translate("registerPeople", "注册管理员账号"))
        self.label.setText(_translate("registerPeople", "账号："))
        self.label_2.setText(_translate("registerPeople", "姓名："))
        self.label_3.setText(_translate("registerPeople", "电话："))
        self.label_4.setText(_translate("registerPeople", "密码："))
        self.label_5.setText(_translate("registerPeople", "确认密码："))
        self.btn_register.setText(_translate("registerPeople", "注册"))
