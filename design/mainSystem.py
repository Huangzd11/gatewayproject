from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout,QHBoxLayout



#主界面设计
class Ui_mainSystemMain(object):
    def setupUi(self, Ui_mainSystemMain):

        # Ui_mainSystemMain.setWindowOpacity(0.95)  # 设置窗口透明度
        #Ui_mainSystemMain.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #Ui_mainSystemMain.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        Ui_mainSystemMain.setObjectName("Ui_mainSystemMain")
        #Ui_mainSystemMain.setFixedSize(800, 500)  # 禁止拉伸窗口大小
        Ui_mainSystemMain.resize(800, 500)

        #设置最小化、最大化和关闭
        Ui_mainSystemMain.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)

        Ui_mainSystemMain.setWindowIcon(QIcon('logo.png'))
        #Ui_mainSystemMain.setStyleSheet("background-image:url(R-C.jpg)")
        #Ui_mainSystemMain.setStyleSheet("background-image:url(test.jpg)")

        # self.verticalLayout = QtWidgets.QVBoxLayout(Ui_mainSystemMain)
        # self.verticalLayout.setObjectName("verticalLayout")

        self.centralWidget = QtWidgets.QWidget(Ui_mainSystemMain)
        self.centralWidget.setObjectName("centralWidget")

        # self.btn_segateway = QtWidgets.QPushButton(Ui_mainSystemMain)
        # self.btn_segateway.setFixedSize(100, 50)
        # self.btn_segateway.setObjectName("btn_segateway")
        # self.verticalLayout.addWidget(self.btn_segateway)
        #
        # self.btn_regateway = QtWidgets.QPushButton(Ui_mainSystemMain)
        # self.btn_regateway.setFixedSize(100, 50)
        # self.btn_regateway.setObjectName("btn_regateway")
        # self.verticalLayout.addWidget(self.btn_regateway)



        self.btn_segateway = QtWidgets.QPushButton(self.centralWidget)
        self.btn_segateway.setGeometry(QtCore.QRect(10, 30, 100, 50))
        self.btn_segateway.setObjectName("btn_segateway")

        self.btn_regateway = QtWidgets.QPushButton(self.centralWidget)
        self.btn_regateway.setGeometry(QtCore.QRect(10, 130, 100, 50))
        self.btn_regateway.setObjectName("btn_regateway")

        self.btn_logs = QtWidgets.QPushButton(self.centralWidget)
        self.btn_logs.setGeometry(QtCore.QRect(10, 230, 100, 50))
        self.btn_logs.setObjectName("btn_logs")

        self.btn_about = QtWidgets.QPushButton(self.centralWidget)
        self.btn_about.setGeometry(QtCore.QRect(10, 330, 100, 50))
        self.btn_about.setObjectName("btn_about")

        self.btn_exit = QtWidgets.QPushButton(self.centralWidget)
        self.btn_exit.setGeometry(QtCore.QRect(10, 430, 100, 50))
        self.btn_exit.setObjectName("btn_exit")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(350, 0, 200, 50))
        self.label.setObjectName("label")

        self.retranslateUi(Ui_mainSystemMain)
        QtCore.QMetaObject.connectSlotsByName(Ui_mainSystemMain)


    def retranslateUi(self, Ui_mainSystemMain):
        _translate = QtCore.QCoreApplication.translate
        Ui_mainSystemMain.setWindowTitle(_translate("wanggSystemMain", "网关管理主界面"))
        self.btn_segateway.setText(_translate("wanggSystemMain", "发货信息"))
        self.btn_regateway.setText(_translate("wanggSystemMain", "返修信息"))
        self.btn_logs.setText(_translate("wanggSystemMain", "日志记录"))
        self.btn_about.setText(_translate("wanggSystemMain", "相关简介"))
        self.btn_exit.setText(_translate("wanggSystemMain", "退出系统"))
        self.label.setText(_translate("wanggSystemMain", "欢迎使用网关管理系统"))

