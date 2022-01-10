from PyQt5 import QtCore, QtSql
from design_admingateway import Ui_admingatewaySystemMain
from helpS import Helps
from PyQt5.QtWidgets import *
from wglogging  import LogSystem
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DetailSystem import detail
from loggingfiles  import Logs
from Five_provinces  import Five_window
from ExPort import  ExportSystem
from about_test import  About
from import3 import Import3System


class adminwanggSystem(QDialog):
    signal_2 = QtCore.pyqtSignal(list)#自定义信号

    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_admingatewaySystemMain()
        self.UI.setupUi(self)
        self.Logs = LogSystem()

        '''
        clicked 一般指点击、按下:一般用于 ui->pushButton
        triggered 一般是QAction等被触发:一般用于 QAction *object 触发
        用法没什么区别，应用场合不同
        '''
        self.UI.b_view_data.triggered.connect(lambda:self.show_table())#在PyQt5中调用槽函数，进行传值的时候，使用lambda表达式可以实现,lambda表达式返回一个值，即一个新的函数
        self.UI.b_close_data.triggered.connect(lambda: self.sql_close())
        self.UI.b_add_row.triggered.connect(lambda:self.addCgateway())
        self.UI.b_delete_row.triggered.connect(lambda:self.delgateway())
        self.UI.b_import.triggered.connect(lambda: self.importgateway())
        self.UI.b_export.triggered.connect(lambda: self.exportgateway())
        self.UI.b_part.triggered.connect(lambda: self.show_table())
        self.UI.b_alls.triggered.connect(lambda: self.showall_table())
        self.UI.b_help.triggered.connect(lambda: self.helpsys())
        self.UI.b_logs.triggered.connect(lambda: self.logSystem())
        self.UI.b_save.triggered.connect(lambda: self.SaveAlls())
        self.UI.b_recover.triggered.connect(lambda: self.RecoverAlls())
        self.UI.exitButton.triggered.connect(self.Exitshow)
        self.UI.b_refresh.triggered.connect(self.show_table)
        self.UI.b_Five_provinces.triggered.connect(self.FiveProvinces)
        self.UI.b_about.triggered.connect(self.About)

        self.UI.b_searchgateway.clicked.connect(lambda: self.searchgateway())

        # 允许右键产生菜单
        self.UI.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        self.UI.tableView.customContextMenuRequested.connect(self.generateMenu)


    #显示表格部分信息
    def show_table(self):
        try:
            # 连接数据库
            try:
                self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                self.db.setDatabaseName('wanggmanage.db')
                self.db.open()

            except Exception as e:
                print(e)

            # 实例化一个可编辑数据模型
            self.model = QtSql.QSqlTableModel()
            self.UI.tableView.setModel(self.model)

            self.model.setTable('sendgateways')  # 设置数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改,保存后生效
            self.model.select()  # 查询所有数据(显示)
            # 设置表格头
            model = QStandardItemModel(0, 33)
            #model.setHorizontalHeaderLabels(['序号', '送货单编号', '合同编号', '项目编号', '项目名称', '建设单位（地/市）', '建设单位（县/区）', '收货单位',
                                             # '收货地址', '收货人', '收货电话', '出库时间', '供货通知人', '发货人', '出库人', '产品名称', '规格型号', 'SN编号',
                                             # '核心板ESN', 'SIM卡ID', 'IP', '快递单号', '送货单回执','验收单编号', '完成时间', '负责人', '是否移交商务组',
                                             # '是否退货', '是否换货', '是否维修', '处理人','时间','备注'])
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, '序号')
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, '送货单编号')
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, '合同编号')
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, '项目编号')
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, '项目名称')
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, '建设单位（地/市）')
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, '建设单位（县/区）')
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, '收货单位')
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, '收货地址')
            self.model.setHeaderData(9, QtCore.Qt.Horizontal, '收货人')
            self.model.setHeaderData(10, QtCore.Qt.Horizontal, '收货电话')
            self.model.setHeaderData(11, QtCore.Qt.Horizontal, '出库时间')
            self.model.setHeaderData(12, QtCore.Qt.Horizontal, '供货通知人')
            self.model.setHeaderData(13, QtCore.Qt.Horizontal, '发货人')
            self.model.setHeaderData(14, QtCore.Qt.Horizontal, '出库人')
            self.model.setHeaderData(15, QtCore.Qt.Horizontal, '产品名称')
            self.model.setHeaderData(16, QtCore.Qt.Horizontal, '规格型号')
            self.model.setHeaderData(17, QtCore.Qt.Horizontal, 'SN编号')
            self.model.setHeaderData(18, QtCore.Qt.Horizontal, '核心板ESN')
            self.model.setHeaderData(19, QtCore.Qt.Horizontal, 'SIM卡ID')
            self.model.setHeaderData(20, QtCore.Qt.Horizontal, 'IP')
            self.model.setHeaderData(21, QtCore.Qt.Horizontal, '快递单号')
            self.model.setHeaderData(22, QtCore.Qt.Horizontal, '送货单回执')
            self.model.setHeaderData(23, QtCore.Qt.Horizontal, '验收单编号')
            self.model.setHeaderData(24, QtCore.Qt.Horizontal, '完成时间')
            self.model.setHeaderData(25, QtCore.Qt.Horizontal, '负责人')
            self.model.setHeaderData(26, QtCore.Qt.Horizontal, '是否移交商务组')
            self.model.setHeaderData(27, QtCore.Qt.Horizontal, '是否退货')
            self.model.setHeaderData(28, QtCore.Qt.Horizontal, '是否换货')
            self.model.setHeaderData(29, QtCore.Qt.Horizontal, '是否维修')
            self.model.setHeaderData(30, QtCore.Qt.Horizontal, '处理人')
            self.model.setHeaderData(31, QtCore.Qt.Horizontal, '时间')
            self.model.setHeaderData(32, QtCore.Qt.Horizontal, '备注')

            # #隐藏列
            self.UI.tableView.setColumnHidden(0, True)
            self.UI.tableView.setColumnHidden(1, True)
            self.UI.tableView.setColumnHidden(6, True)
            self.UI.tableView.setColumnHidden(8, True)
            self.UI.tableView.setColumnHidden(9, True)
            self.UI.tableView.setColumnHidden(10, True)
            self.UI.tableView.setColumnHidden(12, True)
            self.UI.tableView.setColumnHidden(14, True)
            self.UI.tableView.setColumnHidden(15, True)
            self.UI.tableView.setColumnHidden(16, True)
            self.UI.tableView.setColumnHidden(21, True)
            self.UI.tableView.setColumnHidden(22, True)
            self.UI.tableView.setColumnHidden(23, True)
            self.UI.tableView.setColumnHidden(24, True)
            self.UI.tableView.setColumnHidden(25, True)
            self.UI.tableView.setColumnHidden(26, True)
            self.UI.tableView.setColumnHidden(27, True)
            self.UI.tableView.setColumnHidden(28, True)
            self.UI.tableView.setColumnHidden(29, True)
            self.UI.tableView.setColumnHidden(30, True)
            self.UI.tableView.setColumnHidden(31, True)
            #隐藏行
            self.UI.tableView.setRowHidden(0, True)

            # 设置列宽
            #self.UI.tableView.setColumnWidth(0, 40)
            self.UI.tableView.setColumnWidth(2, 180)
            self.UI.tableView.setColumnWidth(3, 160)
            self.UI.tableView.setColumnWidth(4, 180)
            self.UI.tableView.setColumnWidth(7, 180)
            self.UI.tableView.setColumnWidth(11, 80)
            self.UI.tableView.setColumnWidth(13, 50)
            self.UI.tableView.setColumnWidth(17, 140)
            self.UI.tableView.setColumnWidth(20, 90)

        except Exception as e:
            print(e)

        # finally:
        #     self.db.close()

    #在当前行添加
    def addCgateway(self):
        try:
            # 如果存在实例化的数据模型对象
            if self.model:
                # row = self.UI.tableView.currentIndex().row()
                # self.model.insertRows(row, 1)#在当前行前面添加
                self.model.insertRow(self.UI.tableView.currentIndex().row()+1)#在当前行后面添加
                #self.model.insertRow(self.model.rowCount())  # 在末尾添加
                # if self.SaveAlls():
                #     self.Logs.logger.info('Succeeded in adding a message')
            else:
                print("添加失败")

        except Exception as e:
            print(e)
            QMessageBox.warning(self, '提示', '添加异常,%s' % (e), QMessageBox.Ok)
            return

    #在末尾添加
    def addFgateway(self):
        try:
            # 如果存在实例化的数据模型对象
            if self.model:
                self.model.insertRows(self.model.rowCount(), 1)#遍历表数据，在末尾添加

            else:
                print("添加失败")

        except Exception as e:
            print(e)
            QMessageBox.warning(self, '提示', '添加异常,%s' % (e), QMessageBox.Ok)
            return

    #添加一列
    def add_column(self):
        try:
            # 如果存在实例化的数据模型对象
            if self.model:
                Column = self.UI.tableView.currentIndex().column()
                self.model.insertColumns(Column, 1)#在当前行前面添加

            else:
                print("添加失败")

        except Exception as e:
            print(e)
            QMessageBox.warning(self, '提示', '添加异常,%s' % (e), QMessageBox.Ok)
            return

    #删除
    def delgateway(self):
        try:
            if self.model:
                list = self.UI.tableView.selectionModel().selectedRows()
                count = 0
                for index in list:
                    count = count + 1
                    self.model.removeRow(index.row())#删除选中行

                reply = QMessageBox.question(self, '提示', "是否确认删除?", QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.model.submitAll()

                    if count:
                        self.Logs.logger.warning('%d record has been deleted successfully from the sendgateways', count)
                        QMessageBox.information(self, '提示', '已成功删除%d个记录' % (count), QMessageBox.Yes)

                else:
                    self.model.revertAll()#撤销

            else:
                print("删除失败")

        except Exception as e:
            print(e)
            QMessageBox.warning(self, '提示', '删除异常:%s' % (e), QMessageBox.Ok)
            return

    #导入
    def importgateway(self):
        '''sqlite3只支持一写多读.
            读与读可以同时进行
            读与写不可同时进行
            写与写不可同时进行'''
        import_int = Import3System()
        import_int.exec_()
        # try:
        #     conn = sqlite3.connect('./wanggmanage.db')
        #     cur = conn.cursor()  # 获取游标
        #
        #     file, ok= QFileDialog.getOpenFileName(self, '请选择要打开的文件', 'C:\\', 'All Files (*);;Excel 97-2003 工作簿(*.xls)')
        #     if file != '':
        #         if 'xls' in file:
        #             workbook = xlrd.open_workbook(file)
        #             sheet = workbook.sheet_by_name('sheet1')  # execl里面的worksheet1
        #
        #             row_num = sheet.nrows#获取行数
        #             report_num = sheet.ncols  # 获取列数
        #             print(row_num)
        #             QMessageBox.information(self, '提示', '需要导入%s行数据信息，请耐心等待！' % (row_num), QMessageBox.Ok)
        #
        #             for i in range(0, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        #
        #                 row_data = sheet.row_values(i)#获取行数据
        #                 value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5],
        #                          row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11],
        #                          row_data[12],row_data[13], row_data[14], row_data[15], row_data[16], row_data[17],
        #                          row_data[18], row_data[19], row_data[20], row_data[21], row_data[22], row_data[23],
        #                          row_data[24], row_data[25], row_data[26], row_data[27], row_data[28], row_data[29],
        #                          row_data[30], row_data[31], row_data[32] )
        #                 print(i)
        #
        #                 # for a in tqdm(range(i)):
        #                 #     time.sleep(0.05)
        #
        #                 #print(value)
        #                 sql = "insert into sendgateways(num,delivery,contract,item_number,project_name,development1,development2,consigneeD," \
        #                       "address,consignee,phone,time,supplier,consigner,delivery_man,product_name," \
        #                       "specifications,SN,ESN,SIMID,IP,ExpressNumber,receipt1,receipt2,finish,principal,commercial,return,exchange,maintain," \
        #                       "conductor,processing_time,remarks) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        #
        #                 # sql = "insert into sendgateway(序号,送货单编号,合同编号,项目编号,项目名称,建设单位（地/市）,建设单位（县/区）,收货单位," \
        #                 #           "收货地址,收货人,收货电话,出库时间,供货通知人,发货人,出库人,产品名称," \
        #                 #       "规格型号,SN编号,核心板ESN,SIM卡 ID,IP,快递单号,送货单回执是否收到,验收单编号,完成时间,负责人,是否移交商务组,是否退货,是否换货,是否维修," \
        #                 #       "处理人,时间,备注) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        #
        #                 cur.execute(sql, value)  # 执行sql语句
        #                 conn.commit()
        #                 #cur.close()
        #                 # columns = str(sheet.ncols)
        #                 # rows = str(sheet.nrows)
        #                 #print("导入 " + columns + " 列 " + rows + " 行数据到数据库!")
        #
        #         print("导入成功！")
        #         self.Logs.logger.info('%s rows of data are successfully imported from the sendgateways' % row_num)
        #         QMessageBox.information(self, '提示', '导入成功，共导入了%s行数据信息' % (row_num), QMessageBox.Ok)
        #         return
        # except Exception as e:
        #     print(e)
        #     print("导入失败！")
        #     QMessageBox.warning(self, '提示', '导入失败：%s' % (e), QMessageBox.Ok)
        #     return

    #导出
    def exportgateway(self):
        export_int = ExportSystem()
        export_int.exec_()
        # # 连接数据库
        # conn = sqlite3.connect('./wanggmanage.db')
        # cur = conn.cursor()  # 获取游标
        #
        # file, ok = QFileDialog.getSaveFileName(self, '文件保存', 'C:\\', 'All Files (*);;Excel 97-2003 工作簿(*.xls)')
        # if file != '':
        #     if 'xls' or 'csv' in file:
        #         workbook = xlwt.Workbook()
        #         worksheet = workbook.add_sheet('sheet1')
        #         cur.execute("select * from sendgateways")
        #         row = cur.fetchone()
        #         j = 0
        #         while row:
        #             n = len(row)
        #             for i in range(0, n):
        #                 worksheet.write(j, i, str(row[i]))
        #             j += 1
        #             row = cur.fetchone()
        #
        #         workbook.save(file)
        #         print('导出成功，文件已保存至%s' % file)
        #         self.Logs.logger.info('The file was successfully exported from the sendgateways ')
        #         QMessageBox.information(self, '提示', '导出成功，文件已保存至%s' % (file), QMessageBox.Ok)
        #         return

    #查找
    def searchgateway(self):
        try:
            index = self.UI.comboBox.currentIndex()
            searchText = self.UI.line_context.text()
            if len(searchText) is 0:
                QMessageBox.information(self, '提示', '查找内容不能为空，请输入想要查找的内容！', QMessageBox.Yes)
                return

            if index == 0:
                QMessageBox.information(self, '提示', '请选择查找方式！', QMessageBox.Yes)

            if index == 1:
                self.model.setFilter(("SN = '%s'" % (searchText)))#通过SN查询
                self.model.select()#查询所有数据

                s = self.model.rowCount()#遍历表数据
                print(s)
                #判断是否为空
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 2:
                self.model.setFilter(("IP = '%s'" % (searchText)))
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 3:
                self.model.setFilter(("contract = '%s'" % (searchText)))#合同编号
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 4:
                self.model.setFilter(("item_number = '%s'" % (searchText)))#项目编号
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 5:
                self.model.setFilter(("project_name = '%s'" % (searchText)))#项目名称
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 6:
                self.model.setFilter(("development1 = '%s'" % (searchText)))#建设单位
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 7:
                self.model.setFilter(("time = '%s'" % (searchText)))#出库时间
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 8:
                self.model.setFilter(("consigner = '%s'" % (searchText)))#发货人
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 9:
                self.model.setFilter(("ESN = '%s'" % (searchText)))
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

            if index == 10:
                self.model.setFilter(("SIMID = '%s'" % (searchText)))
                self.model.select()
                s = self.model.rowCount()
                if s == 0:
                    QMessageBox.information(self, '提示', '抱歉，没有查找到相关内容！', QMessageBox.Yes)

        except Exception as e:
            print(e)

    #帮助
    def helpsys(self):
        wanggSystemMain = Helps()
        wanggSystemMain.exec_()

    #日志
    def logSystem(self):
        wanggSystemMain = Logs()
        wanggSystemMain.exec_()

    #保存
    def SaveAlls(self):
        print("save")
        self.model.submitAll()#提交所有更改

    #撤销
    def RecoverAlls(self):
        print("Recovers")
        self.model.revertAll()

    #右键菜单
    def generateMenu(self, pos):
        try:
            menu = QMenu()
            item1 = menu.addAction(QIcon("刷新.png"),u'刷新')

            second = menu.addMenu(QIcon("插入.png"),u"插入")
            third = second.addMenu(QIcon("插入行.png"),u'插入一行')
            item2 = third.addAction(QIcon("插入行.png"),u'在当前位置插入')
            item6 = third.addAction(QIcon("插入行.png"), u'在表末尾插入')
            item7 = second.addAction(QIcon("插入列.png"),u'插入一列')

            item3 = menu.addAction(QIcon("删除.png"),u'删除')
            item5 = menu.addAction(QIcon("追踪.png"),u'订单追踪')
            item4 = menu.addAction(QIcon("详细信息.png"), u'显示该行详情信息')

            action = menu.exec_(self.UI.tableView.mapToGlobal(pos))
            # 显示选中行的数据文本
            if action == item1:
                self.show_table()

            if action == item2:
                self.addCgateway()

            if action == item3:
                self.delgateway()

            if action == item4:
                rows = self.UI.tableView.currentIndex().row()
                # # for i in range(33):
                # #     list = self.model.index(rows, i)  # 遍历当前行所以列内容
                # #     vaule = self.model.data(list)   #获取数据
                listgateway = []
                for i in range(33):
                    listgateway.append(self.model.data(self.model.index(rows, i)))
                    # with open('detail.txt', mode='a+', encoding='utf-8') as f:
                    #     f.writelines(listgateway[i])#写入文件
                    #     if listgateway[i] == '':
                    #         f.write("空")
                    #     f.write("\n")
                    #     if i == 0:
                    #         f.truncate(0)#清空文件内容
                # with open('detail.txt', mode='a+', encoding='utf-8') as f:
                #     f.truncate(0)
                #     f.write("序号：")
                #     f.writelines(listgateway[0])  # 写入文件
                #     f.write("\n")
                #     f.write("送货单编号：")
                #     f.writelines(listgateway[1])  # 写入文件
                #     f.write("\n")
                print(listgateway)
                #1、通过文本形式显示
                # details = Details()
                # details.exec_()
                #2、通过列表显示
                checkga = detail()
                self.signal_2.connect(checkga.getInformation)
                self.signal_2.emit(listgateway)
                checkga.exec_()

            if action == item5:
                print("订单追踪")

            if action == item6:
                self.addFgateway()

            if action == item7:
                self.add_column()

        except Exception as e:
            print(e)

    #显示完整表格
    def showall_table(self):
        try:
            # 连接数据库
            try:
                db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('wanggmanage.db')
                db.open()

            except Exception as e:
                print(e)

            # 实例化一个可编辑数据模型
            self.model = QtSql.QSqlTableModel()
            self.UI.tableView.setModel(self.model)

            self.model.setTable('sendgateways')  # 设置数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改,保存后生效
            self.model.select()  # 查询所有数据(显示)
            # 设置表格头
            #self.model = QStandardItemModel(0, 33)
            # model.setHorizontalHeaderLabels(['序号', '送货单编号', '合同编号', '项目编号', '项目名称', '建设单位（地/市）', '建设单位（县/区）', '收货单位',
            # '收货地址', '收货人', '收货电话', '出库时间', '供货通知人', '发货人', '出库人', '产品名称', '规格型号', 'SN编号',
            # '核心板ESN', 'SIM卡ID', 'IP', '快递单号', '送货单回执','验收单编号', '完成时间', '负责人', '是否移交商务组',
            # '是否退货', '是否换货', '是否维修', '处理人','时间','备注'])
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, '序号')
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, '送货单编号')
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, '合同编号')
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, '项目编号')
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, '项目名称')
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, '建设单位（地/市）')
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, '建设单位（县/区）')
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, '收货单位')
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, '收货地址')
            self.model.setHeaderData(9, QtCore.Qt.Horizontal, '收货人')
            self.model.setHeaderData(10, QtCore.Qt.Horizontal, '收货电话')
            self.model.setHeaderData(11, QtCore.Qt.Horizontal, '出库时间')
            self.model.setHeaderData(12, QtCore.Qt.Horizontal, '供货通知人')
            self.model.setHeaderData(13, QtCore.Qt.Horizontal, '发货人')
            self.model.setHeaderData(14, QtCore.Qt.Horizontal, '出库人')
            self.model.setHeaderData(15, QtCore.Qt.Horizontal, '产品名称')
            self.model.setHeaderData(16, QtCore.Qt.Horizontal, '规格型号')
            self.model.setHeaderData(17, QtCore.Qt.Horizontal, 'SN编号')
            self.model.setHeaderData(18, QtCore.Qt.Horizontal, '核心板ESN')
            self.model.setHeaderData(19, QtCore.Qt.Horizontal, 'SIM卡ID')
            self.model.setHeaderData(20, QtCore.Qt.Horizontal, 'IP')
            self.model.setHeaderData(21, QtCore.Qt.Horizontal, '快递单号')
            self.model.setHeaderData(22, QtCore.Qt.Horizontal, '送货单回执')
            self.model.setHeaderData(23, QtCore.Qt.Horizontal, '验收单编号')
            self.model.setHeaderData(24, QtCore.Qt.Horizontal, '完成时间')
            self.model.setHeaderData(25, QtCore.Qt.Horizontal, '负责人')
            self.model.setHeaderData(26, QtCore.Qt.Horizontal, '是否移交商务组')
            self.model.setHeaderData(27, QtCore.Qt.Horizontal, '是否退货')
            self.model.setHeaderData(28, QtCore.Qt.Horizontal, '是否换货')
            self.model.setHeaderData(29, QtCore.Qt.Horizontal, '是否维修')
            self.model.setHeaderData(30, QtCore.Qt.Horizontal, '处理人')
            self.model.setHeaderData(31, QtCore.Qt.Horizontal, '时间')
            self.model.setHeaderData(32, QtCore.Qt.Horizontal, '备注')
            # 设置列宽
            self.UI.tableView.setColumnWidth(0, 40)
            self.UI.tableView.setColumnWidth(2, 180)
            self.UI.tableView.setColumnWidth(3, 160)
            self.UI.tableView.setColumnWidth(4, 180)
            self.UI.tableView.setColumnWidth(7, 180)
            self.UI.tableView.setColumnWidth(11, 80)
            self.UI.tableView.setColumnWidth(13, 50)
            self.UI.tableView.setColumnWidth(17, 140)
            self.UI.tableView.setColumnWidth(20, 90)

            self.UI.tableView.setRowHidden(0, True)

        except Exception as e:
            print(e)

    #关闭数据库连接
    def sql_close(self):
        try:
            self.show_table()
            self.db.close()#关闭数据库连接才能导入
            self.model.clear()#清空数据模型
            QMessageBox.information(self, '提示', '已关闭数据库连接', QMessageBox.Ok)
            return

        except Exception as e:
            print(e)

    def returnSystem(self):
        print("return")
        # wanggSystemMain = main_System()
        # self.close()
        # wanggSystemMain.exec_()

    #退出
    def Exitshow(self):
        self.Logs.logger.info('exit send_gateway System!')
        self.close()

    def FiveProvinces(self):
        Five_provinces = Five_window()
        Five_provinces.exec_()

    def About(self):
        des_about = About()
        des_about.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = adminwanggSystem()
    mainWindow.show()
    sys.exit(app.exec_())