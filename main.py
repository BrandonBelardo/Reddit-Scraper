from notify_run import Notify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time


def get_element_text(source: str, id: str, l_border: str, r_border: str):
    id_index = source.index(id)
    id_sub_str = source[id_index:]
    l_border_index = id_sub_str.index(l_border) + len(l_border)
    r_border_index = id_sub_str.index(r_border)
    return id_sub_str[l_border_index:r_border_index]

def get_post_list(source, split_id):
    if split_id in source:
        return source.split(split_id)
    else:
        raise Exception("Split ID was not found.")


def clean_post_list(lst, id):
    for x, post in enumerate(lst):
        if id not in post:
            del lst[x]


def main():
    notify = Notify()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    post_id = "_1oQyIsiPHYt6nx7VOmd1sz _3xuFbFM3vrCqdGuKGhhhn0"
    tag_id = "_2X6EB3ZhEeXCh1eIVA64XM"
    content_id = "\"_eYtD2XCVieq6emjKBH3m\">"
    link_id = "_10wC0aXnrUKfdJ4Ssz-o14\"><a href=\""
    preferred_tag = ""
    preferred_content = ""
    page_url = "https://www.reddit.com/r/buildapcsales/new"
    driver.get(page_url)
    page_source = driver.page_source
    post_list = get_post_list(page_source, post_id)
    clean_post_list(post_list, content_id)





if __name__ == "__main__":
    main()
