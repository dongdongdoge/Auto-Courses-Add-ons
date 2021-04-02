from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
from bs4 import BeautifulSoup
import time

def video(browser,urls):
    with open("play.js","r",encoding="utf-8") as f:
        js = f.read()
    for url in urls:
        browser.get(url)
        browser.execute_script(js)
        browser.find_element_by_id("auto_play").click()
        while True:
            rate = browser.execute_script("""var video = $("iframe").contents().find("iframe").contents();return video.find("#video > div.vjs-control-bar > div.vjs-progress-control.vjs-control > div").attr("aria-valuenow");""")
            if "100.00" == str(rate):
                break
            else:
                time.sleep(120)


def course(browser):
    urls = []
    browser.get("https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=216430320&clazzid=36512648&enc=c3b4dbcb651e9b58bdff9eee9aea61d4&cpi=174197011&vc=1") 
    h3 = browser.find_elements_by_class_name("clearfix")
    for i in h3:
        try:
            if i.find_element_by_class_name("orange"):
                if "1" == i.find_element_by_class_name("orange").text:
                    urls.append(i.find_element_by_tag_name("a").get_attribute('href'))
        except Exception as e:
            pass
    return urls

def login(browser):
    browser.get("http://i.mooc.chaoxing.com/space/index?t=1617101385349") 
    time.sleep(3)
    browser.find_element_by_id("unameId").send_keys('19520420491') 
    browser.find_element_by_id("passwordId").send_keys('FOREVER0330ZJ') 
    time.sleep(3)
    verify_code = input()
    browser.find_element_by_id('numcode').send_keys(verify_code)
    time.sleep(3)
    browser.find_element_by_class_name("zl_btn_right").click()

def main():
    googleOptions = webdriver.ChromeOptions()
    browser = webdriver.Chrome("/usr/local/bin/chromedriver")
    login(browser)
    time.sleep(5)
    urls = course(browser)
    #print(urls)
    video(browser,urls)

if __name__ == '__main__':
    main()