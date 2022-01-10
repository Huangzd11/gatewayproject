from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_detail(object):
    def setupUi(self, detail):
        detail.setObjectName("detail")
        detail.setFixedSize(480, 680)

        # detail.setWindowFlags(
        #     QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        detail.setWindowIcon(QIcon('../image/logo.png'))


        self.centralWidget = QtWidgets.QWidget(detail)
        self.centralWidget.setObjectName("centralWidget")

        self.line_1 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_1.setGeometry(QtCore.QRect(70, 5, 380, 20))
        self.line_1.setText("")
        self.line_1.setObjectName("line_1")

        self.line_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(80, 25, 370, 20))
        self.line_2.setText("")
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(70, 45, 380, 20))
        self.line_3.setText("")
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(70, 65, 380, 20))
        self.line_4.setText("")
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(70, 85, 380, 20))
        self.line_5.setText("")
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_6.setGeometry(QtCore.QRect(120, 105, 330, 20))
        self.line_6.setText("")
        self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_7.setGeometry(QtCore.QRect(120, 125, 330, 20))
        self.line_7.setText("")
        self.line_7.setObjectName("line_7")

        self.line_8 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_8.setGeometry(QtCore.QRect(70, 145, 380, 20))
        self.line_8.setText("")
        self.line_8.setObjectName("line_8")

        self.line_9 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_9.setGeometry(QtCore.QRect(70, 165, 380, 20))
        self.line_9.setText("")
        self.line_9.setObjectName("line_9")

        self.line_10 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_10.setGeometry(QtCore.QRect(70, 185, 380, 20))
        self.line_10.setText("")
        self.line_10.setObjectName("line_10")

        self.line_11 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_11.setGeometry(QtCore.QRect(70, 205, 380, 20))
        self.line_11.setText("")
        self.line_11.setObjectName("line_11")

        self.line_12 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_12.setGeometry(QtCore.QRect(70, 225, 380, 20))
        self.line_12.setText("")
        self.line_12.setObjectName("line_12")

        self.line_13 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_13.setGeometry(QtCore.QRect(80, 245, 370, 20))
        self.line_13.setText("")
        self.line_13.setObjectName("line_13")

        self.line_14 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_14.setGeometry(QtCore.QRect(70, 265, 380, 20))
        self.line_14.setText("")
        self.line_14.setObjectName("line_14")

        self.line_15 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_15.setGeometry(QtCore.QRect(70, 285, 380, 20))
        self.line_15.setText("")
        self.line_15.setObjectName("line_15")

        self.line_16 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_16.setGeometry(QtCore.QRect(70, 305, 380, 20))
        self.line_16.setText("")
        self.line_16.setObjectName("line_16")

        self.line_17 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_17.setGeometry(QtCore.QRect(70, 325, 380, 20))
        self.line_17.setText("")
        self.line_17.setObjectName("line_17")

        self.line_18 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_18.setGeometry(QtCore.QRect(70, 345, 380, 20))
        self.line_18.setText("")
        self.line_18.setObjectName("line_18")

        self.line_19 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_19.setGeometry(QtCore.QRect(70, 365, 380, 20))
        self.line_19.setText("")
        self.line_19.setObjectName("line_19")

        self.line_20 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_20.setGeometry(QtCore.QRect(70, 385, 380, 20))
        self.line_20.setText("")
        self.line_20.setObjectName("line_20")

        self.line_21 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_21.setGeometry(QtCore.QRect(70, 405, 380, 20))
        self.line_21.setText("")
        self.line_21.setObjectName("line_21")

        self.line_22 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_22.setGeometry(QtCore.QRect(70, 425, 380, 20))
        self.line_22.setText("")
        self.line_22.setObjectName("line_22")

        self.line_23 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_23.setGeometry(QtCore.QRect(80, 445, 370, 20))
        self.line_23.setText("")
        self.line_23.setObjectName("line_23")

        self.line_24 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_24.setGeometry(QtCore.QRect(80, 465, 370, 20))
        self.line_24.setText("")
        self.line_24.setObjectName("line_24")

        self.line_25 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_25.setGeometry(QtCore.QRect(70, 485, 380, 20))
        self.line_25.setText("")
        self.line_25.setObjectName("line_25")

        self.line_26 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_26.setGeometry(QtCore.QRect(70, 505, 380, 20))
        self.line_26.setText("")
        self.line_26.setObjectName("line_26")

        self.line_27 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_27.setGeometry(QtCore.QRect(110, 525, 340, 20))
        self.line_27.setText("")
        self.line_27.setObjectName("line_5")

        self.line_28 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_28.setGeometry(QtCore.QRect(70, 545, 380, 20))
        self.line_28.setText("")
        self.line_28.setObjectName("line_6")

        self.line_29 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_29.setGeometry(QtCore.QRect(70, 565, 380, 20))
        self.line_29.setText("")
        self.line_29.setObjectName("line_29")

        self.line_30 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_30.setGeometry(QtCore.QRect(70, 585, 380, 20))
        self.line_30.setText("")
        self.line_30.setObjectName("line_30")

        self.line_31 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_31.setGeometry(QtCore.QRect(70, 605, 380, 20))
        self.line_31.setText("")
        self.line_31.setObjectName("line_31")

        self.line_32 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_32.setGeometry(QtCore.QRect(70, 625, 380, 20))
        self.line_32.setText("")
        self.line_32.setObjectName("line_32")

        self.line_33 = QtWidgets.QLineEdit(self.centralWidget)
        self.line_33.setGeometry(QtCore.QRect(70, 645, 380, 20))
        self.line_33.setText("")
        self.line_33.setObjectName("line_33")



        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 9, 58, 12))
        #self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 29, 65, 12))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 49, 58, 12))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 69, 58, 12))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 89, 58, 12))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 109, 105, 12))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(10, 129, 105, 12))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(10, 149, 58, 12))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(10, 169, 58, 12))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(10, 189, 58, 12))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(10, 209, 58, 12))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(10, 229, 58, 12))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(10, 249, 65, 12))
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(10, 269, 58, 12))
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(10, 289, 58, 12))
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(10, 309, 58, 12))
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(10, 329, 58, 12))
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(10, 349, 58, 12))
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(10, 369, 58, 12))
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(10, 389, 58, 12))
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(10, 409, 58, 12))
        self.label_21.setObjectName("label_21")

        self.label_22 = QtWidgets.QLabel(self.centralWidget)
        self.label_22.setGeometry(QtCore.QRect(10, 429, 58, 12))
        self.label_22.setObjectName("label_22")

        self.label_23 = QtWidgets.QLabel(self.centralWidget)
        self.label_23.setGeometry(QtCore.QRect(10, 449, 65, 12))
        self.label_23.setObjectName("label_23")

        self.label_24 = QtWidgets.QLabel(self.centralWidget)
        self.label_24.setGeometry(QtCore.QRect(10, 469, 65, 12))
        self.label_24.setObjectName("label_24")

        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setGeometry(QtCore.QRect(10, 489, 58, 12))
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setGeometry(QtCore.QRect(10, 509, 58, 12))
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setGeometry(QtCore.QRect(10, 529, 105, 12))
        self.label_27.setObjectName("label_27")

        self.label_28 = QtWidgets.QLabel(self.centralWidget)
        self.label_28.setGeometry(QtCore.QRect(10, 549, 58, 12))
        self.label_28.setObjectName("label_28")

        self.label_29 = QtWidgets.QLabel(self.centralWidget)
        self.label_29.setGeometry(QtCore.QRect(10, 569, 58, 12))
        self.label_29.setObjectName("label_29")

        self.label_30 = QtWidgets.QLabel(self.centralWidget)
        self.label_30.setGeometry(QtCore.QRect(10, 589, 58, 12))
        self.label_30.setObjectName("label_30")

        self.label_31 = QtWidgets.QLabel(self.centralWidget)
        self.label_31.setGeometry(QtCore.QRect(10, 609, 58, 12))
        self.label_31.setObjectName("label_31")

        self.label_32 = QtWidgets.QLabel(self.centralWidget)
        self.label_32.setGeometry(QtCore.QRect(10, 629, 58, 12))
        self.label_32.setObjectName("label_32")

        self.label_33 = QtWidgets.QLabel(self.centralWidget)
        self.label_33.setGeometry(QtCore.QRect(10, 649, 58, 12))
        self.label_33.setObjectName("label_33")


        self.retranslateUi(detail)
        QtCore.QMetaObject.connectSlotsByName(detail)

    def retranslateUi(self, detail):
        _translate = QtCore.QCoreApplication.translate
        detail.setWindowTitle(_translate("detail", "详细信息"))
        self.label.setText(_translate("detail", "序号："))
        self.label_2.setText(_translate("detail", "送货单编号："))
        self.label_3.setText(_translate("detail", "合同编号："))
        self.label_4.setText(_translate("detail", "项目编号："))
        self.label_5.setText(_translate("detail", "项目名称："))
        self.label_6.setText(_translate("detail", "建设单位（地/市）："))
        self.label_7.setText(_translate("detail", "建设单位（县/区）："))
        self.label_8.setText(_translate("detail", "收货单位："))
        self.label_9.setText(_translate("detail", "收货地址："))
        self.label_10.setText(_translate("detail", "收货人："))
        self.label_11.setText(_translate("detail", "收货电话："))
        self.label_12.setText(_translate("detail", "出库时间："))
        self.label_13.setText(_translate("detail", "供货通知人："))
        self.label_14.setText(_translate("detail", "发货人："))
        self.label_15.setText(_translate("detail", "出库人："))
        self.label_16.setText(_translate("detail", "产品名称："))
        self.label_17.setText(_translate("detail", "规格型号："))
        self.label_18.setText(_translate("detail", "SN编号："))
        self.label_19.setText(_translate("detail", "核心板ESN："))
        self.label_20.setText(_translate("detail", "SIM卡ID："))
        self.label_21.setText(_translate("detail", "IP："))
        self.label_22.setText(_translate("detail", "快递单号："))
        self.label_23.setText(_translate("detail", "送货单回执："))
        self.label_24.setText(_translate("detail", "验收单编号："))
        self.label_25.setText(_translate("detail", "完成时间："))
        self.label_26.setText(_translate("detail", "负责人："))
        self.label_27.setText(_translate("detail", "是否移交商务组："))
        self.label_28.setText(_translate("detail", "是否退货："))
        self.label_29.setText(_translate("detail", "是否换货："))
        self.label_30.setText(_translate("detail", "是否维修："))
        self.label_31.setText(_translate("detail", "处理人："))
        self.label_32.setText(_translate("detail", "时间："))
        self.label_33.setText(_translate("detail", "备注："))

