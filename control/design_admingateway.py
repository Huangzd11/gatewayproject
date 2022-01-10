from PyQt5 import QtGui,QtCore,QtWidgets,QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Ui_admingatewaySystemMain(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("wanggSystemMain")
        #MainWindow.resize(1200, 800)
        MainWindow.setFixedSize(1200, 650)#不能改变大小

        #开启大小窗口
        #MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setWindowIcon(QIcon('logo.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #表格视图控件QTableView
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 30, 1160, 621))
        self.tableView.setObjectName("tableView")

        # self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 1160, 741))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        # self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_3.setObjectName("verticalLayout_3")
        #
        # #表格视图控件QTableView
        # self.tableView = QtWidgets.QTableView(MainWindow)
        # self.tableView.setGeometry(QtCore.QRect(20, 30, 1160, 741))
        # self.tableView.setObjectName("tableView")
        #
        # self.verticalLayout_3.addWidget(self.tableView)
        # self.verticalLayoutWidget.setStretch(0, 1)
        # self.verticalLayoutWidget.setStretch(1, 6)

        self.b_searchgateway = QtWidgets.QPushButton(self.centralwidget)
        self.b_searchgateway.setGeometry(QtCore.QRect(1100, 0, 80, 23))
        self.b_searchgateway.setObjectName("b_searchgateway")
        self.b_searchgateway.setStyleSheet(
            "QPushButton{background-color:white; color: black; border-radius:10px; border:2px groove gray; border-style: outset;}"
            "QPushButton:hover{background-color:white; color: blue;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255);\
                                          border-style: inset;}")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(750, 0, 130, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("请选择查找的方式")
        self.comboBox.addItem("SN编号")
        self.comboBox.addItem("IP地址")
        self.comboBox.addItem("合同编号")
        self.comboBox.addItem("项目编号")
        self.comboBox.addItem("项目名称")
        self.comboBox.addItem("建设单位(地/市)")
        self.comboBox.addItem("出库时间")
        self.comboBox.addItem("发货人")
        self.comboBox.addItem("核心板ESN")
        self.comboBox.addItem("SIM卡 ID")
        self.comboBox.setStyleSheet("border-radius:10px; border:2px groove gray;")


        self.line_context = QtWidgets.QLineEdit(self.centralwidget)
        self.line_context.setGeometry(QtCore.QRect(890, 0, 200, 23))
        self.line_context.setStyleSheet("border-radius:10px; border-style: outset")


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")


        fileMenu = self.menubar.addMenu('文件')
        editMenu = self.menubar.addMenu('编辑')
        viewMenu = self.menubar.addMenu('视图')
        toolsMenu = self.menubar.addMenu('工具')
        helpMenu = self.menubar.addMenu('帮助')

        # MainWindow.setMenuBar(self.menubar)
        # 创建一个action(行为)，标题为"exti"， self 为parent
        self.exitButton = QAction(QIcon("退出系统.png"),'Exit', MainWindow)
        # exitButton = QAction(self)
        # 设置设置该action为分离器 也就是分隔符,当为true时 QIcon会无效
        # 0或非0有效
        # exitButton.setSeparator(0)
        # 设置action的快捷键
        self.exitButton.setShortcut('Ctrl+Q')
        # 设置action的状态栏说明
        # self.exitButton.setStatusTip('退出当前应用')
        # 更改action的title
        self.exitButton.setText("退出系统")

        self.b_view_data = QAction(QIcon("打开连接.png"),'View', MainWindow)
        self.b_view_data.setText("打开连接")

        self.b_close_data = QAction(QIcon("关闭连接.png"),'Close', MainWindow)
        self.b_close_data.setText("关闭连接")

        self.b_add_row = QAction(QIcon("插入.png"),'Add', MainWindow)
        self.b_add_row.setText("插入")
        self.b_add_row.setShortcut('Ctrl+Alt+A')

        self.b_delete_row = QAction(QIcon("删除.png"),'Del', MainWindow)
        self.b_delete_row.setText("删除")
        self.b_delete_row.setShortcut('Delete')

        self.b_refresh = QAction(QIcon("刷新.png"),'Refresh', MainWindow)
        self.b_refresh.setText("刷新")
        self.b_refresh.setShortcut('F5')

        self.b_import = QAction(QIcon("导入.png"),'Import', MainWindow)
        self.b_import.setText("导入连接")

        self.b_export = QAction(QIcon("导出.png"),'Export', MainWindow)
        self.b_export.setText("导出连接")

        self.b_save = QAction(QIcon("保存.png"),'Save', MainWindow)
        self.b_save.setText("保存")
        self.b_save.setShortcut('Ctrl+S')

        self.b_recover = QAction(QIcon("撤销.png"),'Recover', MainWindow)
        self.b_recover.setText("撤销")
        self.b_recover.setShortcut('Ctrl+Z')

        self.b_logs = QAction(QIcon("日志.png"),'Log', MainWindow)
        self.b_logs.setText("历史日志")

        self.b_help = QAction(QIcon("帮助.png"),'Help', MainWindow)
        self.b_help.setText("帮助文档")
        self.b_help.setShortcut('F1')

        self.b_about = QAction('About', MainWindow)
        self.b_about.setText("关于")

        self.b_alls = QAction(QIcon("显示.png"),'All', MainWindow)
        self.b_alls.setText("显示完整表格信息")
        self.b_alls.setShortcut('F12')

        self.b_part = QAction(QIcon("隐藏.png"),'Part', MainWindow)
        self.b_part.setText("隐藏部分表格信息")
        self.b_part.setShortcut('F11')

        self.b_Five_provinces = QAction('Five_provinces', MainWindow)
        self.b_Five_provinces.setText("五省网关发货统计图")


        # 可以将单个action按钮添加到菜单中：
        fileMenu.addAction(self.b_view_data)
        fileMenu.addAction(self.b_import)
        fileMenu.addAction(self.b_export)
        fileMenu.addAction(self.b_close_data)
        fileMenu.addAction(self.exitButton)

        editMenu.addAction(self.b_refresh)
        editMenu.addAction(self.b_add_row)
        editMenu.addAction(self.b_delete_row)
        editMenu.addAction(self.b_recover)
        editMenu.addAction(self.b_save)

        viewMenu.addAction(self.b_alls)
        viewMenu.addAction(self.b_part)
        viewMenu.addAction(self.b_Five_provinces)

        toolsMenu.addAction(self.b_logs)

        helpMenu.addAction(self.b_help)
        helpMenu.addAction(self.b_about)

        # QStatusBar窗口状态栏,窗口底部的一个小条形图
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网关发货维护表"))
        self.b_searchgateway.setText(_translate("MainWindow", "查找"))
        self.line_context.setPlaceholderText(_translate("MainWindow", "请输入查找内容"))  # setPlaceholderText在输入内容之前，给予用户一些提示信息