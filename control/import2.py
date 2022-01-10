# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from ImPort import  ImportSystem


class Ui_Import2(object):
    def setupUi(self, Import2):
        Import2.setObjectName("Import2")
        Import2.setFixedSize(500, 180)
        Import2.setWindowIcon(QIcon('logo.png'))
        Import2.setStyleSheet("background-image:url(test.jpg)")

        self.label = QtWidgets.QLabel(Import2)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Import2)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 91, 21))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Import2)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Import2)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Import2)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Import2)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Import2)
        QtCore.QMetaObject.connectSlotsByName(Import2)

    def retranslateUi(self, Import2):
        _translate = QtCore.QCoreApplication.translate
        Import2.setWindowTitle(_translate("Import2", "导入向导"))
        self.label.setText(_translate("Import2", "字段名行："))
        self.label_2.setText(_translate("Import2", "最后一个数据行："))
        self.lineEdit.setPlaceholderText(_translate("Import2", "必填"))
        self.lineEdit_2.setPlaceholderText(_translate("Import2", "选填"))
        self.pushButton.setText(_translate("Import2", "下一步"))
        self.pushButton_2.setText(_translate("Import2", "取消"))
# import test_rc


class Import2System(QDialog):
    signal_1 = QtCore.pyqtSignal(int)  # 自定义信号
    signal_2 = QtCore.pyqtSignal(object)
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_Import2()
        self.UI.setupUi(self)

        self.UI.pushButton.clicked.connect(lambda: self.import_2())

    def import_2(self):
        try:
            searchText = self.UI.lineEdit.text()
            if len(searchText) is 0:
                QMessageBox.information(self, '提示', '字段行号不能为空，请输入字段行号！', QMessageBox.Yes)
                return
            text1 = int(searchText)
            # print(text1)
            import2 = ImportSystem()
            self.signal_1.connect(import2.show_text)
            self.signal_1.emit(text1)
            self.close()
            import2.exec_()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Import2System()
    mainWindow.show()
    sys.exit(app.exec_())