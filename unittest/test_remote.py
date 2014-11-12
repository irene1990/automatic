from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
# browser = webdriver.Ie(r"/usr/bin/IEDriverServer.exe")
browser = webdriver.Remote('http://192.168.88.183:4444/wd/hub', DesiredCapabilities.INTERNETEXPLORER)
time.sleep(5)
browser.get("http://www.baidu.com")
browser.find_element_by_name("wd").send_keys("scutech")
browser.find_element_by_id("su").click()
time.sleep(10)
browser.close()
