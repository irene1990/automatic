#-*-coding=utf-8
#change driver.find_element_by_id("usr").send_keys("用户名")&driver.find_element_by_id("contract").send_keys(u"用户名") to an available name
#change driver.find_element_by_id("psw").send_keys("密码") to an available password
#change driver.find_element_by_id("code").send_keys("序列号") to your Application code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "http://192.168.88.100/serial"
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.88.100:8889/")
        driver.find_element_by_id("usr").clear()
        driver.find_element_by_id("usr").send_keys("wangsx")
        driver.find_element_by_id("psw").clear()
        driver.find_element_by_id("psw").send_keys("wangsx123")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element_by_id("contract").clear()
        driver.find_element_by_id("contract").send_keys(u"王水仙")
        driver.find_element_by_id("customer").clear()
        driver.find_element_by_id("customer").send_keys(u"测试部")
        driver.find_element_by_id("note").clear()
        driver.find_element_by_id("note").send_keys(u"迪备测试")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("useday").clear()
        driver.find_element_by_id("useday").send_keys("120")
        driver.find_element_by_id("code").clear()
        driver.find_element_by_id("code").send_keys("8rMllxTnvlZLhTytP6tMxan2IuhT5fG6mAy5sQ/0qf8=")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        select = driver.find_element_by_id("productList");
        allOptions = select.find_elements_by_tag_name("option")
        for option in allOptions:
            tmp = option.get_attribute("value")
            if tmp == 'dbackup5':
                option.click()
        time.sleep(2)
        select1 = driver.find_element_by_id("limitSelect");
        allOptions1 = select1.find_elements_by_tag_name("option")
        for option1 in allOptions1:
            tmp1 = option1.get_attribute("value")
            if tmp1 == '3':
                option1.click()
        time.sleep(2)
        driver.find_element_by_id("clientnumNum").clear()
        driver.find_element_by_id("clientnumNum").send_keys("10")
        driver.find_element_by_id("authosdbNum").clear()
        driver.find_element_by_id("authosdbNum").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[2]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[3]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[3]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[4]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[4]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[5]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[5]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[6]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[6]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[7]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[8]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[8]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[9]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[9]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[10]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[10]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[11]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[11]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[12]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[12]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[13]").clear()
        driver.find_element_by_xpath("(//input[@id='authosdbNum'])[13]").send_keys("10")
        driver.find_element_by_id("standbyosdbNum").clear()
        driver.find_element_by_id("standbyosdbNum").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[2]").send_keys("10")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[3]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[3]").send_keys("5")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[4]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[4]").send_keys("5")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[5]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[5]").send_keys("5")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[6]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[6]").send_keys("5")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[7]").send_keys("5")
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[8]").clear()
        driver.find_element_by_xpath("(//input[@id='standbyosdbNum'])[8]").send_keys("5")
        driver.find_element_by_id("submit").click()
        license = driver.find_element_by_id('output_license').text
        print "************************************************license*************************************"
        print license
        print "************************************************license*************************************"
        driver.quit()

if __name__ == "__main__":
    unittest.main()
