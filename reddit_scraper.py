from notify_run import Notify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
from PyQt5 import QtWidgets, QtCore
import sys
from reddit_scraper_gui import Ui_MainWindow

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    notify = Notify()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    #driver = webdriver.Firefox()
    post_id = "_1oQyIsiPHYt6nx7VOmd1sz _3xuFbFM3vrCqdGuKGhhhn0"
    tag_id = "_2X6EB3ZhEeXCh1eIVA64XM"
    content_id = "\"_eYtD2XCVieq6emjKBH3m\">"
    link_id = "_10wC0aXnrUKfdJ4Ssz-o14\"><a href=\""
    preferred_tag = ""
    preferred_content = ""
    page_url = "https://www.reddit.com/r/buildapcsales/new"
    update_interval = 300
    print("test")

    driver.get(page_url)
    while True:
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
        print("{}\n{}\n{}\n".format(tag_list, content_list, link_list))
        time.sleep(update_interval)
        driver.refresh()





if __name__ == "__main__":
    main()
