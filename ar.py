#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.88.100/serial"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.88.185/dbackup/")
        handle = driver.window_handles
        driver.switch_to_frame(0)
        driver.find_element_by_id("serialRadio").click()
        driver.find_element_by_id("trialRadio").click()
        print driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/label").text
        driver.find_element_by_xpath("//div[3]/label").click()
        driver.find_element_by_id("continue").click()
        driver.switch_to_window(handle)
        driver.find_element_by_id("UserNameID").clear()
        driver.find_element_by_id("UserNameID").send_keys("admin")
        driver.find_element_by_id("PWID").clear()
        driver.find_element_by_id("PWID").send_keys("admin")
        driver.find_element_by_id("LoginButton").click()
        action_chains = ActionChains(driver)
        action_chains.move_to_element(driver.find_element_by_xpath('//*[@id="navigate"]/ul/li[3]/a')).perform()
        action_chains.click(driver.find_element_by_link_text("注册用户")).perform()
        driver.find_element_by_id("confirmpassword").clear()
        driver.find_element_by_id("confirmpassword").send_keys("dingjia123")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("156895@qq.com")
        driver.find_element_by_id("telephone").clear()
        driver.find_element_by_id("telephone").send_keys("16448556")
        driver.find_element_by_id("ftpSpace").clear()
        driver.find_element_by_id("ftpSpace").send_keys("10")
        driver.find_element_by_id("ftpDay").clear()
        driver.find_element_by_id("ftpDay").send_keys("1")
        driver.find_element_by_name("strPrivilegeName[]").click()
        driver.find_element_by_id("RegisterBut").click()
        self.assertEqual(u"提交成功", self.close_alert_and_get_its_text())
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_link_text(u"用户组").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_css_selector("button.ms-choice").click()
        driver.find_element_by_name("selectAll").click()
        driver.find_element_by_css_selector("label").click()
        driver.find_element_by_css_selector("button.ms-choice").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

