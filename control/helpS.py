# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wangg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtGui,QtCore,QtWidgets,QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_HelpSystem(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(570, 568)
        Help.setWindowIcon(QIcon('帮助.png'))

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Help)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 531, 541))
        self.plainTextEdit.setObjectName("plainTextEdit")
        #self.plainTextEdit.setReadOnly(True)  # 设置文本框只读

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "帮助文档"))
        self.plainTextEdit.setPlainText(_translate("Help", "一、文件\n"
                                                           "    1、打开连接：打开网关维护表，默认只显示部分重要信息\n"
                                                           "    2、导入连接：必须关闭数据库连接才可导入，支持一键导入Excel表，当前仅支持导入.xls\n"
                                                           "    3、导出连接：支持一键导出Excel表\n"
                                                           "    4、关闭连接：关闭当前数据库连接\n"
                                                           "    5、退出系统：退出当前界面\n"
                                                           "\n"
                                                           "二、编辑\n"
                                                           "    1、刷新：刷新网关维护表\n"
                                                           "    2、插入：在表格添加一行，保存后生效\n"
                                                           "    3、删除：删除选中的行数，确认删除自动保存\n"
                                                           "    4、撤销：撤销保存前的所有修改\n"
                                                           "    5、保存：保存数据信息\n"
                                                           "\n"
                                                           "三、视图\n"
                                                           "    1、显示完整表格信息：可查看完整的网关维护表数据信息\n"
                                                           "    2、隐藏部分表格信息：可把部分不是特别重要的信息隐藏起来，默认\n"
                                                           "    3、五省网关发货统计图：查看五省网关发货情况\n"
                                                           "\n"
                                                           "四、工具\n"
                                                           "    1、历史日志：进行操作的相关日志记录\n"
                                                           "\n"
                                                           "五、帮助\n"
                                                           "    1、帮助文档：查看使用说明\n"
                                                           "    2、关于：查看版本信息\n"
                                                           "\n"
                                                           "六、查找\n"
                                                           "    1、可按SN、IP、ESN、建设单位等查找，查找内容不可为空\n"
                                                           "\n"
                                                           "七、右键菜单\n"
                                                           "    1、显示该行详细信息：点击查看选中行的完整的表格信息\n"
                                                           "    2、订单追踪：点击查看网关订单记录"))

class Helps(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_HelpSystem()
        self.UI.setupUi(self)