#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,datetime

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
        time.sleep(1)
        select = driver.find_element_by_tag_name("select")
        project = select.find_elements_by_tag_name("option")
        for option in project:
            tmp = option.get_attribute("value")
            if tmp == '/redmine/projects/wddps?jump=welcome':
                option.click()
                break
        time.sleep(1)
        driver.find_element_by_link_text(u"问题").click()
        time.sleep(2)
        select1 = driver.find_element_by_id("operators_status_id")
        time.sleep(2)
        project1 = select1.find_elements_by_tag_name("option")
        for option1 in project1:
            tmp1 = option1.get_attribute("value")
            if tmp1 == "=":
                option1.click()
                break
        time.sleep(2)
        select2 = driver.find_element_by_id("values_status_id_1")
        project2 = select2.find_elements_by_tag_name("option")
        for option2 in project2:
            tmp2 = option2.get_attribute("value")
            if tmp2 == '16':
                option2.click()
                break
        time.sleep(1)
        select3 = driver.find_element_by_id("add_filter_select")
        time.sleep(1)
        project3 = select3.find_elements_by_tag_name("option")
        for option3 in project3:
            tmp3 = option3.get_attribute("value")
            if tmp3 == 'author_id':
                option3.click()
                break
        time.sleep(1)
        #driver.find_element_by_id("cb_status_id").click()
        #driver.find_elements_by_tag_name("legend")[1].click()
        driver.find_element_by_link_text(u"应用").click()
        time.sleep(1)
        list = driver.find_elements_by_xpath("//*[@id='content']/form[2]/div[2]/table/tbody/tr")
        i = 0
        z_name = "/home/irene/Documents/Work_Documents/Reports/"+time.strftime('%Y-%m-%d')+"job_report.txt"
        zhoubao = open(z_name, 'a')
        zhoubao.write("*********************************"+time.strftime('%Y-%m-%d')+"*********************************************"+"\n")
        zhoubao.write("*********************************My Verified Bugs in One Week*********************************************"+"\n")
        print "*********************************My Verified Bugs in One Week*********************************************"
        while i < len(list):
            created_on_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[9]"
            created_on = driver.find_element_by_xpath(created_on_path).text.encode('utf-8')[:10]
            a = int(created_on[:4])
            b = int(created_on[5:7])
            c = int(created_on[8:10])
            #timeb = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            #print (datetime.datetime.now()-datetime.datetime(a,b,c)).days
            if (datetime.datetime.now()-datetime.datetime(a,b,c)).days < 6:
                subject_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[6]/a"
                subject = driver.find_element_by_xpath(subject_path).text.encode('utf-8')
                id_path = "//*[@id='content']/form[2]/div[2]/table/tbody/tr["+str(i+1)+"]/td[2]/a"
                id0 = driver.find_element_by_xpath(id_path).text.encode('utf-8')
                zhoubao_o = "(" + str(i+1) + ") Verified #" + id0 + " : " +subject
                zhoubao.write(zhoubao_o+"\n")
                print "(" + str(i+1) + ") Verified : Bug #" + id0 + " : " +subject
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

