import matplotlib
# 使用 matplotlib中的FigureCanvas (在使用 Qt5 Backends中 FigureCanvas继承自QtWidgets.QWidget)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas#封装一个FigureCanvasQTAgg类，画图的时候调用这个类，FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。渲染器是使物体显示在屏幕上
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sqlite3



class Five_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.resize(800, 500)
        # 设置最小化、最大化和关闭
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("五省网关发货统计")
        self.setWindowIcon(QIcon('logo.png'))

        self.figure = plt.figure(facecolor='#FFFFFF')# 可选参数facecolor为背景颜色，plt.figure()绘画
        self.canvas = FigureCanvas(self.figure)#画布

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)#addWidget将FigureCanvasQTAgg类对象添加到布局

        self.setLayout(layout)

        self.FcanvasShow()

    #五省网关发货统计
    def FcanvasShow(self):
        #连接数据库获取数据
        conn = sqlite3.connect('./wanggmanage.db')
        cur = conn.cursor()  # 获取游标
        sql = "select province,gateway from province"
        cur.execute(sql)
        result = cur.fetchall()  # result为元组

        # 将元组数据存进列表中
        provinces = []
        gateway = []
        for x in result:
            provinces.append(x[0])
            gateway.append(x[1])

        # 将gateway中的数据转化为int类型
        gateway = list(map(int, gateway))
        # 设置柱状图
        plt.bar(range(len(gateway)), gateway, color='green', width=0.3, tick_label=provinces)

        for x, y in enumerate(gateway):
            plt.text(x , y, '%d' % y, ha='center', va='bottom')

        matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 设置字体为楷体

        # 设置标题
        plt.title("五省网关发货数量统计")
        plt.xlabel("省份")
        plt.ylabel("数量")

#运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Five_window()
    main_window.show()
    app.exec()



