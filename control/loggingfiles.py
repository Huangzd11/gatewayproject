from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Loggings(object):
    def setupUi(self, Loggings):
        Loggings.setObjectName("Loggings")
        Loggings.resize(611, 400)
        Loggings.setWindowIcon(QIcon('日志.png'))

        self.textEdit = QtWidgets.QTextEdit(Loggings)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 571, 380))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)#设置文本框只读

        #打开日志文件
        with open('info.log', 'r') as f:
            msg = f.read()
            self.textEdit.setPlainText(msg)#setPlainText设置纯文本

        self.retranslateUi(Loggings)
        QtCore.QMetaObject.connectSlotsByName(Loggings)

    def retranslateUi(self, Loggings):
        _translate = QtCore.QCoreApplication.translate
        Loggings.setWindowTitle(_translate("Loggings", "日志文件"))

class Logs(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_Loggings()
        self.UI.setupUi(self)
