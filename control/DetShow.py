from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_DetailSys(object):
    def setupUi(self, DetailSys):
        DetailSys.setObjectName("DetailSys")
        DetailSys.resize(1000, 500)
        DetailSys.setWindowIcon(QIcon('日志.png'))

        self.textEdit = QtWidgets.QTextEdit(DetailSys)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 950, 480))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)#设置文本框只读

        #打开日志文件
        with open('detail.txt', mode='r', encoding='utf-8') as f:
            msg = f.read()
            self.textEdit.setPlainText(msg)#setPlainText设置纯文本

        self.retranslateUi(DetailSys)
        QtCore.QMetaObject.connectSlotsByName(DetailSys)

    def retranslateUi(self, DetailSys):
        _translate = QtCore.QCoreApplication.translate
        DetailSys.setWindowTitle(_translate("DetailSys", "详细信息"))

class Details(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_DetailSys()
        self.UI.setupUi(self)
