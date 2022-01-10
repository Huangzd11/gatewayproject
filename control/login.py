import sys
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from Main_System import main_System
from wglogging  import LogSystem
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Ui_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 150)# 禁止拉伸窗口大小

        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.setStyleSheet("background-image:url(1.jpg)")

        self.centralWidget = QtWidgets.QWidget(MainWindow)#中心窗口部件
        self.centralWidget.setObjectName("centralWidget")

        self.line_Id = QtWidgets.QLineEdit(self.centralWidget)
        self.line_Id.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.line_Id.setText("")
        self.line_Id.setObjectName("line_Id")

        self.line_password = QtWidgets.QLineEdit(self.centralWidget)
        self.line_password.setGeometry(QtCore.QRect(250, 50, 100, 20))
        self.line_password.setText("")
        self.line_password.setObjectName("line_password")
        self.line_password.setEchoMode(QLineEdit.Password)#设置输入密码为圆点

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 12))
        self.label_2.setObjectName("label_2")

        self.btn_login = QtWidgets.QPushButton(self.centralWidget)
        self.btn_login.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.btn_login.setObjectName("btn_login")

        self.btn_register = QtWidgets.QPushButton(self.centralWidget)
        self.btn_register.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.btn_register.setObjectName("btn_register")

        MainWindow.setCentralWidget(self.centralWidget)

        # QStatusBar窗口状态栏,窗口底部的一个小条形图
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Message in Login.')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网关管理系统"))
        self.line_Id.setPlaceholderText(_translate("MainWindow", "请输入帐号"))#setPlaceholderText在输入内容之前，给予用户一些提示信息
        self.line_password.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))#setText设置文本信息
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.btn_login.setText(_translate("MainWindow", "登陆"))
        # self.btn_register.setText(_translate("MainWindow", "注册"))
        self.btn_register.setText(_translate("MainWindow", "取消"))


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_login()
        self.UI.setupUi(self)
        self.UI.btn_login.clicked.connect(lambda :self.login())#调用槽函数，进行传值的时候，使用lambda表达式,不传参是可以不使用
        self.UI.btn_register.clicked.connect(lambda :self.register())

        self.logshow = LogSystem()

        self.connectSqlite()
        self.createDb()

    #连接数据库
    def connectSqlite(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('wanggmanage.db')
        self.db.open()#判断是否连接数据库成功 返回布尔值
        print(self.db.open())

    #创建表
    def createDb(self):
        query = QSqlQuery()
        #账户密码数据表
        query.exec_("CREATE TABLE if not exists people("
                    "id VARCHAR(255) PRIMARY KEY,"
                    "peopleName VARCHAR(255),"
                    "telephone VARCHAR(255),"
                    "PASSWORD VARCHAR(255),"
                    "REPASSWORD VARCHAR(255))")

        # 网关发货数据表
        query.exec_("CREATE TABLE if not exists sendgateways("
                    "num VARCHAR(255),"
                    "delivery VARCHAR(255),"
                    "contract VARCHAR(255),"
                    "item_number VARCHAR(255),"
                    "project_name VARCHAR(255),"
                    "development1 VARCHAR(255),"
                    "development2 VARCHAR(255),"
                    "consigneeD VARCHAR(255),"
                    "address VARCHAR(255),"
                    "consignee VARCHAR(255),"
                    "phone VARCHAR(255),"
                    "time  VARCHAR(255),"
                    "supplier VARCHAR(255),"
                    "consigner VARCHAR(255),"
                    "delivery_man VARCHAR(255),"
                    "product_name VARCHAR(255),"
                    "specifications VARCHAR(255),"
                    "SN VARCHAR(255) ,"
                    "ESN VARCHAR(255),"
                    "SIMID VARCHAR(255),"
                    "IP VARCHAR(32),"
                    "ExpressNumber VARCHAR(255),"
                    "receipt1 VARCHAR(255),"
                    "receipt2 VARCHAR(255),"
                    "finish VARCHAR(255),"
                    "principal VARCHAR(255),"
                    "commercial VARCHAR(255),"
                    "return VARCHAR(255),"
                    "exchange VARCHAR(255),"
                    "maintain VARCHAR(32),"
                    "conductor VARCHAR(255),"
                    "processing_time VARCHAR(255),"
                    "remarks VARCHAR(255))")

        #网关返修数据表
        query.exec_("CREATE TABLE if not exists regateway("
                    "num INT,"
                    "time VARCHAR(255),"
                    "SN VARCHAR(255) PRIMARY KEY,"
                    "IP VARCHAR(32),"
                    "problem_phenomenon VARCHAR(255),"
                    "detail VARCHAR(255),"
                    "analysis VARCHAR(255),"
                    "solution VARCHAR(255),"
                    "repair VARCHAR(10),"
                    "resend VARCHAR(255),"
                    "remarks VARCHAR(255))")

        #五省网关发货统计表
        query.exec_("CREATE TABLE if not exists province("
                    "province VARCHAR(255),"
                    "gateway VARCHAR(255))")

        #网关数量统计表
        query.exec_("CREATE TABLE if not exists wgateway("
                    "content VARCHAR(255),"
                    "quantity VARCHAR(255))")

    #登录
    def login(self):
        #self.connectSqlite()
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
        if peopleId == 'admin' and PASSWORD == '123456':
            if query.next():# 逐条查询信息
                self.db.close()#关闭数据库连接

                wanggSystemMain = main_System()
                self.logshow.logger.info('Login successfully!')
                self.logshow.logger.info('Welcome to login the gateway system!')
                self.close()#
                wanggSystemMain.exec_()

        #普通用户
        elif peopleId == 'user' and PASSWORD == '123456':
            print("123")

        else:
            self.logshow.logger.info('The account or password is incorrect, login failed!')
            QMessageBox.information(self, '提示', '账号或密码错误，请检查！', QMessageBox.Yes)
            print("账号或密码错误，请检查！")
            return

    #注册
    def register(self):
        self.close()
        # registerPeople=register()
        # self.signal_1.connect(registerPeople.getDatabase)
        # self.signal_1.emit(self.db)
        # registerPeople.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())