# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reddit_scraper_gui_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from notify_run import Notify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 29, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.plainTextEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit1.setGeometry(QtCore.QRect(140, 20, 111, 41))
        self.plainTextEdit1.setTabChangesFocus(True)
        self.plainTextEdit1.setOverwriteMode(False)
        self.plainTextEdit1.setObjectName("plainTextEdit1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit2.setGeometry(QtCore.QRect(140, 70, 181, 25))
        self.plainTextEdit2.setTabChangesFocus(True)
        self.plainTextEdit2.setOverwriteMode(False)
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 104, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setWordWrap(False)
        self.label3.setObjectName("label3")
        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit3.setGeometry(QtCore.QRect(140, 103, 181, 25))
        self.plainTextEdit3.setTabChangesFocus(True)
        self.plainTextEdit3.setOverwriteMode(False)
        self.plainTextEdit3.setObjectName("plainTextEdit3")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.button_press())
        self.pushButton1.setGeometry(QtCore.QRect(340, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(20, 137, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(200, 137, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setWordWrap(False)
        self.label4.setObjectName("label4")
        self.spinBox1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox1.setGeometry(QtCore.QRect(340, 137, 61, 22))
        self.spinBox1.setMaximum(999999)
        self.spinBox1.setProperty("value", 300)
        self.spinBox1.setObjectName("spinBox1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_pressed = False

    def closeEvent(self):
        super(QtGui.QMainWindow, self).closeEvent()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "r/buildapcsales Scraper"))
        self.label1.setText(_translate("MainWindow", "Preferred Tags:"))
        self.plainTextEdit1.setPlaceholderText(_translate("MainWindow", "eg. CPU, GPU, Motherboard"))
        self.label2.setText(_translate("MainWindow", "Include Keywords:"))
        self.plainTextEdit2.setPlaceholderText(_translate("MainWindow", "eg. 9900k, corsair k70"))
        self.label3.setText(_translate("MainWindow", "Exclude Keywords:"))
        self.plainTextEdit3.setPlaceholderText(_translate("MainWindow", "eg. intel, amd, msi"))
        self.pushButton1.setText(_translate("MainWindow", "Set Values"))
        self.radioButton1.setText(_translate("MainWindow", "Send Push Notifications"))
        self.label4.setText(_translate("MainWindow", "Refresh Interval (sec.):"))

    def button_press(self):
        self.button_pressed = True
        self.preferred_tags_list = [x.strip() for x in self.plainTextEdit1.toPlainText().split(",")]
        if self.plainTextEdit1.toPlainText() == "":
            self.preferred_tags_list = []
        self.preferred_tags_list = [x.lower() for x in self.preferred_tags_list]
        self.included_keywords = [x.strip() for x in self.plainTextEdit2.toPlainText().split(",")]
        if self.plainTextEdit2.toPlainText() == "":
            self.included_keywords = []
        self.included_keywords = [x.lower() for x in self.included_keywords]
        self.excluded_keywords = [x.strip() for x in self.plainTextEdit3.toPlainText().split(",")]
        if self.plainTextEdit3.toPlainText() == "":
            self.excluded_keywords = []
        self.excluded_keywords = [x.lower() for x in self.excluded_keywords]
        self.send_push = self.radioButton1.isChecked()
        self.interval = self.spinBox1.value()
        QtCore.QCoreApplication.exit()



def get_element_text(source, id, l_border, r_border):
    id_index = source.index(id)
    id_sub_str = source[id_index:]
    l_border_index = id_sub_str.index(l_border) + len(l_border)
    r_border_index = id_sub_str.index(r_border)
    return id_sub_str[l_border_index:r_border_index]

def get_element_text_list(source_lst, id, l_border, r_border):
    text_lst = []
    for source in source_lst:
        text_lst.append(get_element_text(source, id, l_border, r_border))
    return text_lst

def get_post_list(source, split_id):
    if split_id in source:
        return source.split(split_id)
    else:
        raise Exception("Split ID was not found.")

def clean_post_list(lst, id):
    for x, post in enumerate(lst):
        if id not in post:
            del lst[x]
    return lst

def get_recent_post_list(last_recent, content_lst, display_lst):
    recent_lst = []
    for i, x in enumerate(content_lst):
        if x != last_recent:
            recent_lst.append(display_lst[i])
        else:
            return recent_lst
    return recent_lst

def filter_list(display_lst, tag_lst, content_lst, pref_tags, inc_keywords, exc_keywords):
    filtered_lst = []
    contains_tag = False
    contains_inc = False
    contains_exc = False

    for i in range(len(display_lst)):
        if len(pref_tags) > 0:
            for x in pref_tags:
                if x == tag_lst[i].lower():
                    contains_tag = True
        else:
            contains_tag = True
        if len(exc_keywords) > 0:
            for x in exc_keywords:
                if x in content_lst[i].lower():
                    contains_exc = True
                    break
        else:
            contains_exc = False
        if len(inc_keywords) > 0:
            for x in inc_keywords:
                if x in content_lst[i].lower():
                    contains_inc = True
        else:
            contains_inc = True
        if contains_tag and contains_inc and not contains_exc:
            filtered_lst.append(display_lst[i])
        contains_tag = False
        contains_inc = False
        contains_exc = False
    return filtered_lst


def display_recent_posts(send_notif, recent_post_lst, notify, times_ran):
    print("Refresh at: " + datetime.now().strftime("%H:%M:%S") + "\n")
    if len(recent_post_lst) > 0:
        print("New Sales!")
        notif_string = ""
        for x in recent_post_lst:
            if notif_string == "":
                notif_string += x
            else:
                notif_string += "\n\n" + x
        print(notif_string)
        if times_ran > -1:
            if send_notif:
                print("Sending push...")
                notify.send(notif_string)


def main(ui):
    notify = Notify()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    post_id = "_1oQyIsiPHYt6nx7VOmd1sz _3xuFbFM3vrCqdGuKGhhhn0"
    tag_id = "_2X6EB3ZhEeXCh1eIVA64XM"
    content_id = "\"_eYtD2XCVieq6emjKBH3m\">"
    link_id = "_10wC0aXnrUKfdJ4Ssz-o14\"><a href=\""
    page_url = "https://www.reddit.com/r/buildapcsales/new"
    update_interval = ui.interval
    last_recent_post = ""
    times_ran = 0

    driver.get(page_url)

    while True:
        time.sleep(5)
        page_source = driver.page_source
        # this will create a list that separates the page source by a class id that exists once per post
        # this is so each title, tag, and link can be accessed uniquely
        post_html_list = get_post_list(page_source, post_id)
        # removes any non-post (possible Reddit advertisements that may be picked up)
        post_html_list = clean_post_list(post_html_list, content_id)
        # since the tag, content, and link lists all use the "post_html_list", they are parallel
        tag_list = get_element_text_list(post_html_list, tag_id, "<span>", "</span>")
        content_list = get_element_text_list(post_html_list, content_id, content_id, "</h3>")
        link_list = get_element_text_list(post_html_list, link_id, link_id, "\" class=\"")
        display_list = ["{}\n{}".format(x, y) for x, y in zip(content_list, link_list)]
        recent_display_list = get_recent_post_list(last_recent_post, content_list, display_list)
        filtered_recent_list = filter_list(recent_display_list, tag_list, content_list, ui.preferred_tags_list, ui.included_keywords, ui.excluded_keywords)
        last_recent_post = content_list[0]

        display_recent_posts(ui.send_push, filtered_recent_list, notify, times_ran)
        time.sleep(update_interval)
        driver.refresh()
        times_ran += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    if not ui.button_pressed:
        sys.exit()
    main(ui)

