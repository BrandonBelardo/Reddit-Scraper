from notify_run import Notify
notify = Notify()

post = "_1oQyIsiPHYt6nx7VOmd1sz _3xuFbFM3vrCqdGuKGhhhn0"
class_code = "_1poyrkZ7g36PawDueRza-J _2uazWzYzM0Qndpz5tFu3EX"
tag = "_2X6EB3ZhEeXCh1eIVA64XM"
content = "\"_eYtD2XCVieq6emjKBH3m\">"
link = "_10wC0aXnrUKfdJ4Ssz-o14\"><a href=\""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
tag_list = []
content_list = []
link_list = []
preferred_tag = ""
preferred_string = ""
preferred_index_list = []
first_old = ""
wait_time_sec = 60
while True:
    driver.get("https://www.reddit.com/r/buildapcsales/new/")
    text = driver.page_source


    post_list = text.split(post)
    i = 0

    # print(text)
    # quit()
    #print(len(post_list))
    for x in post_list:
        if i > 0:
            # finds index of the tag class code
            tag_result = x.index(tag)
            # creates a substring starting from that index
            tag_sub_str = x[tag_result:]

            content_result = x.index(content)
            content_sub_str = x[content_result:]

            link_result = x.index(link)
            link_sub_str = x[link_result:]


            # finds index at the end of <span>
            if "<span>" in tag_sub_str:


                content_border1 = content_sub_str.index(content) + len(content)
                content_border2 = content_sub_str.index("</h3>")
                content_text = content_sub_str[content_border1:content_border2]
                if content_text == first_old:
                    break
                content_list.append(content_text)

                tag_border1 = tag_sub_str.index("<span>") + 6
                # finds index at the beginning of </span>
                tag_border2 = tag_sub_str.index("</span>")
                # substring of the two borders (final text)
                tag_text = tag_sub_str[tag_border1:tag_border2]
                tag_list.append(tag_text)
                if tag_text == preferred_tag:
                    preferred_index_list.append(i - 1)

                link_border1 = link_sub_str.index(link) + len(link)
                link_border2 = link_sub_str.index("\" class=\"")
                link_text = link_sub_str[link_border1:link_border2]
                #(link_text)
                #print("")
                link_list.append(link_text)
        i += 1

        notif_string = ""
        print("Refresh at: " + datetime.now().strftime("%H:%M:%S"))
    if len(content_list) > 0:
        if preferred_tag == "":
            notif_string = "New Sales!\n"
        else:
            notif_string = "New " + preferred_tag + " Sales!\n"
        for x in range(len(tag_list)):
            if preferred_tag == "":
                notif_string += content_list[x] + "\n" + link_list[x] + "\n\n"

            elif len(preferred_index_list) > 0:
                if x in preferred_index_list:
                    notif_string += content_list[x] + "\n" + link_list[x] + "\n\n"
        print(notif_string)
        # notify.send(notif_string)
        first_old = content_list[0]
    tag_list.clear()
    content_list.clear()
    link_list.clear()
    preferred_index_list.clear()
    time.sleep(wait_time_sec)

    def main():
        pass

    if __name__ == "__main__":
        main()








