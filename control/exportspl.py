import sys
from PyQt5 import QtSql, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import xlwt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlQuery
import sqlite3

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("exportSystemMain")
        self.setFixedSize(400, 150)  # 禁止拉伸窗口大小

        # #连接到数据库
        # self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')  # SQLite3
        # self.db.setDatabaseName('./wanggmanage.db')
        # self.db.open()



        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.save_file = QtWidgets.QPushButton(self.centralWidget)
        self.save_file.setGeometry(QtCore.QRect(10, 30, 100, 50))
        self.save_file.setObjectName("save_file")
        self.save_file.setText('保存至')

        self.setCentralWidget(self.centralWidget)

        self.save_file.clicked.connect(self.saveFile)

    def saveFile(self):
        #连接数据库
        conn = sqlite3.connect('./wanggmanage.db')
        cur = conn.cursor()#获取游标

        # workbook = xlwt.Workbook()
        # worksheet = workbook.add_sheet('sheet1')
        # cur.execute("select * from wangg")
        # row = cur.fetchone()
        # j = 0
        # while row:
        #     n = len(row)
        #     for i in range(0, n):
        #         worksheet.write(j, i, str(row[i]))
        #     j += 1
        #     row = cur.fetchone()
        #
        # workbook.save('date.xls')
        # print("123465")

        file, ok = QFileDialog.getSaveFileName(self, '文件保存', 'C:\\', 'All Files (*);;Excel 97-2003 工作簿(*.xls)')

        if file != '':
            if 'xls' in file:
                workbook = xlwt.Workbook()
                worksheet = workbook.add_sheet('sheet')
                cur.execute("select * from wangg")
                row = cur.fetchone()
                j = 0
                while row:
                    n = len(row)
                    for i in range(0, n):
                        worksheet.write(j, i, str(row[i]))
                    j += 1
                    row = cur.fetchone()
                #workbook.save('date.xls')
                workbook.save(file)
                print('文件已保存至%s' % file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())