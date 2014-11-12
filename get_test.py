#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.88.100/serial"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.88.100/redmine/login?back_url=http%3A%2F%2F192.168.88.100%2Fredmine%2F")
        self.assertEqual(u"鼎甲项目管理系统", driver.title)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("wangsx")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("wangsx123")
        driver.find_element_by_name("login").click()
        time.sleep(2)
        select = driver.find_element_by_tag_name("select")
        project = select.find_elements_by_tag_name("option")
        for option in project:
            tmp = option.get_attribute("value")
            if tmp == '/redmine/projects/wddps?jump=welcome':
                option.click()
                break
        time.sleep(2)
        driver.find_element_by_link_text(u"问题").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"QA_Test").click()
        time.sleep(5)
        driver.find_elements_by_tag_name("legend")[0].click()
        select1 = driver.find_element_by_id("add_filter_select")
        time.sleep(2)
        send = select1.find_elements_by_tag_name("option")
        for option1 in send:
            tmp = option1.get_attribute("value")
            if tmp == 'status_id':
                option1.click()
            if tmp == 'assigned_to_id':
                option1.click()
                break
        time.sleep(2)
        driver.find_element_by_css_selector("legend").click()
        driver.find_element_by_link_text(u"应用").click()
        time.sleep(2)
        list = driver.find_elements_by_xpath("//*[@id='content']/form[2]/div[2]/table/tbody/tr")
        i = 0
        z_name = "/home/irene/Documents/Work_Documents/Reports/"+time.strftime('%Y-%m-%d')+"job_report.txt"
        zhoubao = open(z_name, 'a')
        zhoubao.write("*********************************Test For Me*********************************************"+"\n")
        zhoubao.write(('{0:10}    {1:15}    {2:18}    {3:40}'.format('作者','状态','编号','主题')) + "\n")
        print "*********************************Test For Me*********************************************"
        print ('{0:10}    {1:15}    {2:18}    {3:40}'.format("作者","状态","编号","主题"))
        while i < len(list):
            subject_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[6]/a"
            subject = driver.find_element_by_xpath(subject_path).text.encode('utf-8')
            id_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[2]/a"
            id0 = driver.find_element_by_xpath(id_path).text.encode('utf-8')
            author_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[7]/a"
            author = driver.find_element_by_xpath(author_path).text.encode('utf-8')
            status_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[4]"
            status = driver.find_element_by_xpath(status_path).text.encode('utf-8')
            x=author
            xx=status
            xxx=" Test #" + id0 
            xxxx=subject
            zhoubao_o =  ('{0:10}    {1:15}    {2:18}    {3:40}'.format(x,xx,xxx,xxxx))
            zhoubao.write(zhoubao_o+"\n")
            print ('{0:10}    {1:15}    {2:18}    {3:40}'.format(x,xx,xxx,xxxx))
            i +=1
        zhoubao.close() 
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

