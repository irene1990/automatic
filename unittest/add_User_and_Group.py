#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time, re

driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "http://192.168.88.100/serial"
driver.get("http://192.168.56.102/dbackup/")
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
driver.switch_to_alert().accept()
time.sleep(1)
actionc = ActionChains(driver)
actionc.move_to_element(driver.find_element_by_link_text("用户管理")).perform()
actionc.click(driver.find_element_by_link_text("注册")).perform()
driver.find_element_by_id("username").send_keys("dingjia")
driver.find_element_by_id("strPassword").send_keys("dingjia123")
driver.find_element_by_id("confirmpassword").send_keys("dingjia123")
driver.find_element_by_id("email").send_keys("156895@qq.com")
driver.find_element_by_id("telephone").send_keys("16448556")
driver.find_element_by_id("ftpSpace").send_keys("10")
driver.find_element_by_id("ftpDay").send_keys("1")
driver.find_element_by_name("strPrivilegeName[]").click()
driver.find_element_by_id("RegisterBut").click()
time.sleep(1)
driver.switch_to_alert().accept()
actionc = ActionChains(driver)
actionc.move_to_element(driver.find_element_by_link_text("用户管理")).perform()
actionc.click(driver.find_element_by_link_text("用户组")).perform()
driver.find_element_by_css_selector("button.ms-choice").click()
driver.find_element_by_name("selectAll").click()
driver.find_element_by_css_selector("button.ms-choice").click()
driver.quit()


