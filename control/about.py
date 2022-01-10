from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import *




class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(570, 568)
        About.setWindowIcon(QIcon('简介.png'))

        self.plainTextEdit = QtWidgets.QPlainTextEdit(About)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 531, 541))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)#设置文本框只读

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "相关介绍"))
        self.plainTextEdit.setPlainText(_translate("About", "01  # 发货信息\n"
                                                           "\n"
                                                           "    ## 功能描述\n"
                                                           "\n"
                                                           "        可查询（SN、ip、ESN等）网关发货信息\n"
                                                           "        可添加单条网关发货信息\n"
                                                           "        可删除单条或多条网关发货信息\n"
                                                           "        可修改单条网关发货信息\n"
                                                           "        可导入/导出网关发货信息——支持一建导出Excel表\n"
                                                           "        可显示/隐藏网关维护表信息\n"
                                                           "        可查看单行数据的详细信息\n"
                                                           "\n"
                                                           "02  # 返修信息\n"
                                                           "\n"
                                                           "    ## 功能描述\n"
                                                           "\n"
                                                           "        可查询（SN、ip、ESN等）网关发货信息\n"
                                                           "        可添加单条网关返修信息\n"
                                                           "        可删除单条或多条网关返修信息\n"
                                                           "        可修改单条网关返修信息\n"
                                                           "        可导入/导出网关返修信息——支持一建导出Excel表\n"
                                                           "        可显示/隐藏网关维护表信息\n"
                                                           "        可查看单行数据的详细信息\n"
                                                           "\n"
                                                           "03 # 日志记录\n"
                                                           "\n"
                                                           "    ## 功能描述\n"
                                                           "        \n"
                                                           "        可查看用户登陆记录\n"
                                                           "        可查看添加、删除、修改等记录\n"
                                                           "\n"
                                                           "04 # 相关介绍\n"
                                                           "    \n"
                                                           "    ## 功能描述\n"
                                                           "    \n"
                                                           "        简单介绍各部分功能\n"
                                                           "    \n"
                                                           "\n"
                                                           "05 # 退出系统\n"
                                                           "    \n"
                                                           "    ## 功能描述\n"
                                                           "    \n"
                                                           "        退出程序\n"
                                                           "    \n"
                                                           "\n"
                                                           ""))

class about(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_About()
        self.UI.setupUi(self)