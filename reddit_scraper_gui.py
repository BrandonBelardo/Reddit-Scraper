# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reddit_scraper_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(140, 29, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.plainTextEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit1.setGeometry(QtCore.QRect(260, 20, 111, 41))
        self.plainTextEdit1.setTabChangesFocus(True)
        self.plainTextEdit1.setOverwriteMode(False)
        self.plainTextEdit1.setObjectName("plainTextEdit1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(140, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit2.setGeometry(QtCore.QRect(260, 70, 181, 25))
        self.plainTextEdit2.setTabChangesFocus(True)
        self.plainTextEdit2.setOverwriteMode(False)
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(140, 104, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setWordWrap(False)
        self.label3.setObjectName("label3")
        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit3.setGeometry(QtCore.QRect(260, 103, 181, 25))
        self.plainTextEdit3.setTabChangesFocus(True)
        self.plainTextEdit3.setOverwriteMode(False)
        self.plainTextEdit3.setObjectName("plainTextEdit3")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(460, 50, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(120, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label6.setFont(font)
        self.label6.setWordWrap(False)
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(430, 200, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label7.setFont(font)
        self.label7.setWordWrap(False)
        self.label7.setObjectName("label7")
        self.plainTextEdit4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit4.setGeometry(QtCore.QRect(20, 230, 301, 141))
        self.plainTextEdit4.setReadOnly(True)
        self.plainTextEdit4.setObjectName("plainTextEdit4")
        self.plainTextEdit5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit5.setGeometry(QtCore.QRect(340, 230, 301, 141))
        self.plainTextEdit5.setReadOnly(True)
        self.plainTextEdit5.setObjectName("plainTextEdit5")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(140, 137, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(20, 372, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label5.setFont(font)
        self.label5.setWordWrap(False)
        self.label5.setObjectName("label5")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(320, 137, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setWordWrap(False)
        self.label4.setObjectName("label4")
        self.spinBox1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox1.setGeometry(QtCore.QRect(460, 137, 61, 22))
        self.spinBox1.setMaximum(999999)
        self.spinBox1.setProperty("value", 300)
        self.spinBox1.setObjectName("spinBox1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "r/buildapcsales Scraper"))
        self.label1.setText(_translate("MainWindow", "Preferred Tags:"))
        self.plainTextEdit1.setPlaceholderText(_translate("MainWindow", "eg. CPU, GPU, Motherboard"))
        self.label2.setText(_translate("MainWindow", "Include Keywords:"))
        self.plainTextEdit2.setPlaceholderText(_translate("MainWindow", "eg. 9900k, corsair k70"))
        self.label3.setText(_translate("MainWindow", "Exclude Keywords:"))
        self.plainTextEdit3.setPlaceholderText(_translate("MainWindow", "eg. intel, amd, msi"))
        self.pushButton1.setText(_translate("MainWindow", "Apply"))
        self.label6.setText(_translate("MainWindow", "New Posts"))
        self.label7.setText(_translate("MainWindow", "Recent Posts"))
        self.radioButton1.setText(_translate("MainWindow", "Send Push Notifications"))
        self.label5.setText(_translate("MainWindow", "Last update:"))
        self.label4.setText(_translate("MainWindow", "Refresh Interval (sec.):"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
