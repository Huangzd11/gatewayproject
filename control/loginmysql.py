import sys

from PyQt5 import QtSql, QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from design.login import Ui_login
import qdarkstyle
import pymysql

class Login(QMainWindow):
    #定义一个信号
    signal_1 = QtCore.pyqtSignal(QtSql.QSqlDatabase)#QSqlDatabase：建立数据库的连接

    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_login()
        # self.setWindowIcon(QIcon('logo.png'))
        # self.setStyleSheet("background-image:url(1.jpg)")
        self.UI.setupUi(self)
        self.UI.btn_login.clicked.connect(lambda :self.login())
        self.UI.btn_register.clicked.connect(lambda :self.register())

        self.connectMysql()
        self.createDb()

    #连接数据库
    def connectMysql(self):
        db = pymysql.connect(host="172.21.9.94", user="root", password="123456", database="testdb")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql = """CREATE TABLE if not exists people(
                    id CHAR(255) PRIMARY KEY,
                    peopleName CHAR(255),
                    telephone CHAR(255),
                    PASSWORD CHAR(255),
                    REPASSWORD CHAR(255))"""


        sql2 = """CREATE TABLE if not exists wangg(
                    num INT,"
                    hetongbianhao CHAR(255),
                    xiangmumingc CHAR(255),
                    SN CHAR(255),
                    ESN CHAR(255),
                    SIMID CHAR(255),
                    IP CHAR(32))"""

        sql3 = """CREATE TABLE if not exists regateway(
                    num INT
                    time CHAR(255),
                    SN CHAR(255),
                    IP CHAR(32),
                    problem_phenomenon CHAR(255),
                    detail CHAR(255),
                    analysis CHAR(255),
                    solution CHAR(255),
                    repair CHAR(10),
                    resend CHAR(255),
                    remarks CHAR(255))"""

        cursor.execute(sql)
        cursor.execute(sql2)
        cursor.execute(sql3)

    #登录
    def login(self):
        query = QSqlQuery()#QSqlQuery实现数据库的交互，执行SQL语句
        peopleId = self.UI.line_Id.text()
        PASSWORD = self.UI.line_password.text()
        if len(peopleId) is 0 or len(PASSWORD) is 0:
            QMessageBox.information(self, '提示','账号或密码不能为空！',QMessageBox.Yes)
            return

        searchPeople = "select * from people where id=? and PASSWORD = ?"
        query.prepare(searchPeople)
        query.bindValue(0,peopleId)#根据位置绑定
        query.bindValue(1,PASSWORD)
        query.exec_()#执行exec_()函数，所做的操作才能被真正执行

        #管理员
        if peopleId == 'admin' and PASSWORD == '123@456':

            if query.next():# 逐条查询信息
                # wanggSystemMain=adminwanggSystem()
                # self.signal_1.connect(wanggSystemMain.getDatabase)
                # self.signal_1.emit(self.db)
                self.close()

                # wanggSystemMain.exec_()

        #普通用户
        elif peopleId == 'user' and PASSWORD == '123456':

            if query.next():
                #wanggSystemMain = wanggSystem()
                # wanggSystemMain = main_System()
                # self.signal_1.connect(wanggSystemMain.getDatabase)
                # self.signal_1.emit(self.db)
                self.close()

                # wanggSystemMain.exec_()

        else:
            QMessageBox.information(self, '提示', '账号或密码错误，请检查！', QMessageBox.Yes)
            print("账号或密码错误，请检查！")
            return

    #注册
    def register(self):

        # registerPeople=register()
        # self.signal_1.connect(registerPeople.getDatabase)
        # self.signal_1.emit(self.db)
        # registerPeople.exec_()
        QMessageBox.information(self, '提示', '暂不支持此操作！', QMessageBox.Yes)
        print("暂不支持此操作！")
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())#设置背景颜色
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())