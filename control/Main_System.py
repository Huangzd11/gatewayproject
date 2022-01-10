# -*- coding: utf-8 -*-
import matplotlib
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas#封装一个FigureCanvasQTAgg类，画图的时候调用这个类，FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。渲染器是使物体显示在屏幕上
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QPushButton
import matplotlib.pyplot as plt
#import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from Repgateway  import RegatewaySystem
from about  import about
from loggingfiles  import Logs
from wglogging  import LogSystem
from PyQt5.QtGui import QIcon
import sqlite3
import sys
from admingatewaySystem import adminwanggSystem




#主界面
class main_System(QDialog):

    def __init__(self):
        #super().__init__()
        QDialog.__init__(self)
        self.resize(800, 500)
        # 设置最小化、最大化和关闭
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("网关管理主界面")
        self.setWindowIcon(QIcon('主界面.png'))
        self.setStyleSheet("background-image:url(test.jpg)")
        #self.setStyleSheet("background-image:url(1.jpg)")

        self.logShow = LogSystem()

        self.figure = plt.figure()#(facecolor='#FFD7C4')  # 可选参数,facecolor为背景颜色，plt.figure()绘画
        self.canvas = FigureCanvas(self.figure)#画布

        #添加按键
        #self.btn_segateway = QPushButton("发货信息")
        '''  正常状态：黑底（背景色），白字（前景色），圆角，向外凸起
            鼠标停留：背景和前景反色
            鼠标按下：背景色变为淡蓝色，向内凹陷'''
        self.btn_segateway = QtWidgets.QPushButton("发货信息")
        self.btn_segateway.setFixedSize(160, 25)
        self.btn_segateway.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:steelblue; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        self.btn_regateway = QPushButton("返修信息")
        self.btn_regateway.setFixedSize(160, 25)
        self.btn_regateway.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:steelblue; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        self.btn_logs = QPushButton("日志记录")
        self.btn_logs.setFixedSize(160, 25)
        self.btn_logs.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:steelblue; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        self.btn_about = QPushButton("相关介绍")
        self.btn_about.setFixedSize(160, 25)
        self.btn_about.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:steelblue; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        self.btn_exit = QPushButton("退出系统")
        self.btn_exit.setFixedSize(160, 25)
        self.btn_exit.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:steelblue; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        #连接事件
        self.btn_segateway.clicked.connect(lambda: self.segateway())
        self.btn_regateway.clicked.connect(lambda: self.regateway())
        self.btn_logs.clicked.connect(lambda: self.logs())
        self.btn_about.clicked.connect(lambda: self.about())
        self.btn_exit.clicked.connect(lambda: self.exitSystem())

        #设计布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # layout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.btn_segateway)
        self.verticalLayout.addWidget(self.btn_regateway)
        self.verticalLayout.addWidget(self.btn_logs)
        self.verticalLayout.addWidget(self.btn_about)
        self.verticalLayout.addWidget(self.btn_exit)
        self.horizontalLayout.addWidget(self.canvas)

        self.horizontalLayout_2.addLayout(self.verticalLayout)#
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.CanvasShow()

    #网关数量统计柱状图
    def CanvasShow(self):
        # 连接数据库获取数据
        conn = sqlite3.connect('./wanggmanage.db')
        cur = conn.cursor()  # 获取游标
        sql = "select content,quantity from wgateway"
        cur.execute(sql)
        result = cur.fetchall()  # result为元组

        # 将元组数据存进列表中
        content = []
        quantity = []
        for x in result:
            content.append(x[0])
            quantity.append(x[1])

        # 将gateway中的数据转化为int类型
        quantity = list(map(int, quantity))
        # 设置柱状图
        plt.bar(range(len(quantity)), quantity, color='steelblue', width=0.3, tick_label=content)

        # 在柱体上显示数据
        for x, y in enumerate(quantity):
            plt.text(x, y, '%d' % y, ha='center', va='bottom')

        matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 设置字体为楷体

        # 设置标题
        plt.title("网关统计")
        plt.xlabel("内容")
        plt.ylabel("数量")


    #发货网关
    def segateway(self):
        wanggSystemMain = adminwanggSystem()
        # wanggSystemMain = Gateway_window()
        self.logShow.logger.info('View the shipping statistics of gateways in five provinces')
        wanggSystemMain.exec_()

    #返修网关
    def regateway(self):
        wanggSystemMain = RegatewaySystem()
        self.logShow.logger.info('Login repair gateway maintenance table')
        wanggSystemMain.exec_()

    #日志
    def logs(self):
        wanggSystemMain = Logs()
        wanggSystemMain.exec_()
        #print("logs")

    def about(self):
        wanggSystemMain = about()
        wanggSystemMain.exec_()
        #print("about")

    #退出
    def exitSystem(self):
        self.logShow.logger.info('exitSystem!')
        self.close()


# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_System()
    main_window.show()
    app.exec()



