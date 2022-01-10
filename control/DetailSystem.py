from PyQt5.QtWidgets import QDialog

from designDetal import Ui_detail

class detail(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.UI = Ui_detail()
        self.UI.setupUi(self)


    def getInformation(self,list):

        self.UI.line_1.setText(list[0])
        self.UI.line_2.setText(list[1])
        self.UI.line_3.setText(list[2])
        self.UI.line_4.setText(list[3])
        self.UI.line_5.setText(list[4])
        self.UI.line_6.setText(list[5])
        self.UI.line_7.setText(list[6])
        self.UI.line_8.setText(list[7])
        self.UI.line_9.setText(list[8])
        self.UI.line_10.setText(list[9])
        self.UI.line_11.setText(list[10])
        self.UI.line_12.setText(list[11])
        self.UI.line_13.setText(list[12])
        self.UI.line_14.setText(list[13])
        self.UI.line_15.setText(list[14])
        self.UI.line_16.setText(list[15])
        self.UI.line_17.setText(list[16])
        self.UI.line_18.setText(list[17])
        self.UI.line_19.setText(list[18])
        self.UI.line_20.setText(list[19])
        self.UI.line_21.setText(list[20])
        self.UI.line_22.setText(list[21])
        self.UI.line_23.setText(list[22])
        self.UI.line_24.setText(list[23])
        self.UI.line_25.setText(list[24])
        self.UI.line_26.setText(list[25])
        self.UI.line_27.setText(list[26])
        self.UI.line_28.setText(list[27])
        self.UI.line_29.setText(list[28])
        self.UI.line_30.setText(list[29])
        self.UI.line_31.setText(list[30])
        self.UI.line_32.setText(list[31])
        self.UI.line_33.setText(list[32])


