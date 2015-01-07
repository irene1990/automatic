#-*-coding=utf-8
from selenium import webdriver
import time
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com/")
    #driver.find_element_by_link_text(u'贴吧').click()
    driver.find_element_by_partial_link_text(u'贴').click()
    time.sleep(3)
    driver.quit()