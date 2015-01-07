#-*-coding=utf-8
#对百度搜索输入框进行定位
from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()
    
    driver.get("http://www.baidu.com.")
    driver.implicitly_wait(5)
    
    #通过标签属性id定位
    search_ipt = driver.find_element_by_id('kw')
    search_ipt.send_keys(u'授客')
    time.sleep(1)
    search_ipt.clear()
    time.sleep(1)
    
    #通过标签属性name定位
    search_ipt = driver.find_element_by_name('wd')
    search_ipt.send_keys(u'授客')
    time.sleep(1)
    search_ipt.clear()
    time.sleep(1)
    
    #通过标签名tag name定位
    #search_ipt = driver.find_element_by_tag_name('input')
    #search_ipt.send_keys(u'授客')
    #time.sleep(1)
    #search_ipt.clear()
    #time.sleep(1)
    
    #通过css selector定位
    search_ipt = driver.find_element_by_css_selector('#kw')
    search_ipt.send_keys(u'授客')
    time.sleep(1)
    search_ipt.clear()
    time.sleep(1)
    
    #通过xpath定位
    search_ipt = driver.find_element_by_xpath('//input[@id="kw"')
    search_ipt.send_keys(u'授客')
    
    #通过标签属性className方式定位(this.className))
    search_btn = driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()