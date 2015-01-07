#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
if __name__ == "__main__":
    #Create a new instance of the Firfox driver
    driver = webdriver.Firefox()
    
    #max window
    driver.maximize_window()
    
    # go to the baidu skydriver home page
    driver.get('http://www.baidu.com')
    
    #print page title  
    print driver.title
    
    #find the element that's id attribute is kw1(the baidu search box)
    input_element = driver.find_element_by_id('kw')
    
    #type in the search box
    input_element.send_keys(u"授客")
    
    #submit the form
    input_element.submit()
    
    try:
        #we have to wait for the page to refresh,the last thing that seems to be updated is the title
        WebDriverWait(driver,10).until(EC.title_contains(u'授客'))
        print (driver.title)
    finally:
        driver.quit()
