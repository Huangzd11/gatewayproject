# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vlayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTime
from PyQt5.QtWidgets import *
import sys
import xlrd
import sqlite3
from PyQt5.QtGui import *
from wglogging  import LogSystem





#界面设计
class Ui_Import(object):
    def setupUi(self, Import):
        Import.setObjectName("Import")
        Import.setFixedSize(589, 242)
        Import.setWindowIcon(QIcon('logo.png'))
        Import.setStyleSheet("background-image:url(test.jpg)")

        self.label_time = QtWidgets.QLabel(Import)
        self.label_time.setGeometry(QtCore.QRect(70, 220, 401, 16))
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")

        self.label_filename = QtWidgets.QLabel(Import)
        self.label_filename.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label_filename.setObjectName("label_filename")

        self.label_sheetname = QtWidgets.QLabel(Import)
        self.label_sheetname.setGeometry(QtCore.QRect(30, 50, 54, 12))
        self.label_sheetname.setObjectName("label_sheetname")

        self.lineEdit = QtWidgets.QLineEdit(Import)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 401, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.listWidget = QtWidgets.QListWidget(Import)
        self.listWidget.setGeometry(QtCore.QRect(70, 50, 401, 131))
        self.listWidget.setObjectName("listWidget")

        self.pushButton_open = QtWidgets.QPushButton(Import)
        self.pushButton_open.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.pushButton_open.setObjectName("pushButton_open")

        self.pushButton_import = QtWidgets.QPushButton(Import)
        self.pushButton_import.setGeometry(QtCore.QRect(500, 50, 75, 23))
        self.pushButton_import.setObjectName("pushButton_import")

        self.progressBar = QtWidgets.QProgressBar(Import)
        self.progressBar.setGeometry(QtCore.QRect(70, 190, 431, 23))
        self.progressBar.setProperty("value", 0)#初始值
        # self.progressBar.setMinimum(0)#最小值
        # self.progressBar.setMaximum(100)#最大值
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Import)
        QtCore.QMetaObject.connectSlotsByName(Import)

    def retranslateUi(self, Import):
        _translate = QtCore.QCoreApplication.translate
        Import.setWindowTitle(_translate("Import", "导入向导"))
        self.label_filename.setText(_translate("Import", "文件路径"))
        self.label_sheetname.setText(_translate("Import", "表名"))
        self.pushButton_open.setText(_translate("Import", "打开文件"))
        self.pushButton_import.setText(_translate("Import", "开始导入"))


class ImportSystem(QDialog):
    signal_1 = QtCore.pyqtSignal(int)  # 自定义信号
    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_Import()
        self.UI.setupUi(self)
        self.Logs = LogSystem()

        self.UI.pushButton_open.clicked.connect(lambda: self.Open())
        self.UI.pushButton_import.clicked.connect(lambda: self.import_sql())
        self.UI.listWidget.clicked.connect(lambda: self.set_tobtn())

        # self.UI.pushButton.setEnabled(False)
        self.UI.pushButton_import.setEnabled(False)#默认"开始导入"按钮不能点击

    def Open(self):
        self.UI.pushButton_import.setEnabled(False)
        self.UI.listWidget.clear()

        #选择导入文件
        file, ok = QFileDialog.getOpenFileName(self, '请选择要打开的文件', 'C:\\', 'All Files (*);;Excel 97-2003 工作簿(*.xls)')
        self.UI.lineEdit.setText(file)

        try:
            self.rdfile = xlrd.open_workbook(file)#xlrd只支持.xls文件
            self.sheets = self.rdfile.sheet_names()#获取打开工作簿的所有工作表
            self.UI.listWidget.addItems(self.sheets)#添加到listWidget

        except Exception as e:
            print("打开失败",e)
            QMessageBox.warning(self, '提示', '打开文件失败：%s' % (e), QMessageBox.Ok)
            return

    #当表名列集合被点击了，就执行set_tobtn函数，然后将"开始导入"按钮设置为可用
    def set_tobtn(self):
        self.UI.label_time.setText("")
        self.UI.pushButton_import.setEnabled(True)

    def show_text(self,a):
        global text#变量定义为全局变量,以便后面函数调用
        text = a
        print(text)

    #导入函数
    def import_sql(self):
        try:
            # sheet = self.rdfile.sheet_by_name(self.UI.listWidget.currentItem().text())  # 获取选中的工作表
            # row_num = sheet.nrows  # 获取行数
            # print(row_num)
            # # row_data = sheet.row_values(0)
            # import1 = Import2System()
            # # self.signal_1.connect(import1.import_2)
            # # self.signal_1.emit(row_num)
            # import1.exec_()
            # print("开始导入")
            # print("123")
        # try:
            #连接数据库
            conn = sqlite3.connect('./wanggmanage.db')
            cur = conn.cursor()  # 获取游标

            sheet = self.rdfile.sheet_by_name(self.UI.listWidget.currentItem().text())#获取选中的工作表
            row_num = sheet.nrows  # 获取行数
            col_num = sheet.ncols  # 获取列数

            QMessageBox.information(self, '提示', '需要导入%s行数据信息，请耐心等待！' % (row_num), QMessageBox.Ok)
            start_time = QTime.currentTime()  # 获取当前时间

            global text
            # print(text)
            for i in range(text, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
                row_data = sheet.row_values(i)  # 获取行数据
                value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5],
                         row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11],
                         row_data[12], row_data[13], row_data[14], row_data[15], row_data[16], row_data[17],
                         row_data[18], row_data[19], row_data[20], row_data[21], row_data[22], row_data[23],
                         row_data[24], row_data[25], row_data[26], row_data[27], row_data[28], row_data[29],
                         row_data[30], row_data[31], row_data[32])
                # print(i)
                # print(value)
                self.UI.progressBar.setRange(0, row_num-1)#设置进度条范围
                self.UI.progressBar.setValue(i)

                sql = "insert into sendgateways(num,delivery,contract,item_number,project_name,development1,development2,consigneeD," \
                      "address,consignee,phone,time,supplier,consigner,delivery_man,product_name," \
                      "specifications,SN,ESN,SIMID,IP,ExpressNumber,receipt1,receipt2,finish,principal,commercial,return,exchange,maintain," \
                      "conductor,processing_time,remarks) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

                # sql = "insert into sendgateway(序号,送货单编号,合同编号,项目编号,项目名称,建设单位（地/市）,建设单位（县/区）,收货单位," \
                #           "收货地址,收货人,收货电话,出库时间,供货通知人,发货人,出库人,产品名称," \
                #       "规格型号,SN编号,核心板ESN,SIM卡 ID,IP,快递单号,送货单回执是否收到,验收单编号,完成时间,负责人,是否移交商务组,是否退货,是否换货,是否维修," \
                #       "处理人,时间,备注) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

                cur.execute(sql, value)  # 执行sql语句
                conn.commit()

            print("导入成功！")
            self.Logs.logger.info('%s rows of data are successfully imported from the sendgateways' % row_num)
            end_time = QTime.currentTime()
            time = QTime.msecsTo(start_time,end_time)/1000#计算时间，msecsTo返回从当前时间到t的毫秒数。如果t比这个时间早，返回的毫秒数为负。

            s = "成功导入：" + str(row_num)  + "条数据," + "用时：" + str(time) + "秒"
            self.UI.label_time.setText(s)

            self.UI.pushButton_import.setEnabled(False)

        except Exception as e:
            print(e)
            print("导入失败:",e)
            QMessageBox.warning(self, '提示', '导入失败：%s' % (e), QMessageBox.Ok)
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ImportSystem()
    mainWindow.show()
    sys.exit(app.exec_())