#!/usr/bin/env python
#coding=utf-8

##########################################################
#	
#	脚本名称：迪备服务用户注册自动化测试
#	功能描述：用于测试用户注册
#	作    者：吴冬亮
#	版    本：1.0
#
#   使用说明：此代码适合于没有试用30天提示窗口的服务器,要用
#            admin用户登陆;所有的的admin用户的必须配置项设置完成；
#            总共注册15个用户
#
###########################################################

#导入包文件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import os
import random

#定义公有变量
#设置登陆用户名和密码
#userName=raw_input("Pelease input your user name(admin):")
#if userName=='':
#    userName='admin'
userName='admin'
#print "Your user name is: " + userName

#userPassword=raw_input("Pelease input your user password(admin):")
#if userPassword=='':
#    userPassword='admin'
userPassword='admin'
#print "Your password is: " + userPassword
    
#address=raw_input("Pelease input your user IP(192.168.88.183):")
#if address=='':
#    address="192.168.88.183"
address="192.168.88.212"
#print "The IP is: " + address
    
#port=raw_input("Pelease input your user port(80):")
#if port=='':
#    port="80"
port="80"
#print "The port is: " + port

print 

urlAddress="http://"+address+":"+port+"/dbackup/index.php"
print "The web server is: " + urlAddress

#得到浏览器对象
dbackupServer = webdriver.Firefox()

#定义一个用户list
#names = ['wudongliang','mameilin','lianzhongxin','liantingjuan','wangshuixian','fanliming','user1','user2','user3','user4','user5','user6','user7','user8','user9']
names = ['dingjia']
#定义一个登陆函数
def login():
	#将浏览器最大化
	dbackupServer.maximize_window()
	#打开管理服务器地址网页
	dbackupServer.get(urlAddress)
	#设置等待时间
	dbackupServer.implicitly_wait(5)	
        #跳过试用期对话框
        handle = dbackupServer.window_handles
        dbackupServer.switch_to_frame(0)
        dbackupServer.find_element_by_id("serialRadio").click()
        dbackupServer.find_element_by_id("trialRadio").click()
        dbackupServer.find_element_by_xpath("//div[3]/label").click()
        dbackupServer.find_element_by_id("continue").click()
        dbackupServer.switch_to_window(handle)
	#清除用户名输入框并且输入用户名
	dbackupServer.find_element_by_id("UserNameID").clear()
	dbackupServer.find_element_by_id("UserNameID").send_keys(userName)
	#清除密码输入框，并且输入密码
	dbackupServer.find_element_by_id("PWID").clear()
	dbackupServer.find_element_by_id("PWID").send_keys(userPassword)
	#点击登陆按钮
	dbackupServer.find_element_by_id("LoginButton").click()
	#设置等待时间
	time.sleep(5)
        alert = dbackupServer.switch_to_alert()
        alert.accept()

def userAdd():
    count=1
    #依次注册用户列表中的用户
    for name in names:    
        #选择用户管理
        print "选择用户管理"
        action_chains = ActionChains(dbackupServer)
        action_chains.move_to_element(dbackupServer.find_element_by_link_text("用户管理")).perform()
        action_chains.click(dbackupServer.find_element_by_link_text("注册")).perform()
        #dbackupServer.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/ul[1]/li[3]/a").click()        
        #选择用户注册
        print "#选择用户注册"
        #dbackupServer.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/ul[1]/li[3]/ul/li[2]/a").click()
        #设置等待时间
        dbackupServer.implicitly_wait(5)
        #输入用户名
        dbackupServer.find_element_by_id("username").clear()
        dbackupServer.find_element_by_id("username").send_keys(name)
        #输入用户密码，密码为用户名+123456
        userPassword='dingjia123'
        dbackupServer.find_element_by_id("strPassword").clear()
        dbackupServer.find_element_by_id("strPassword").send_keys(userPassword)
        #重复输入密码
        dbackupServer.find_element_by_id("confirmpassword").clear()
        dbackupServer.find_element_by_id("confirmpassword").send_keys(userPassword)
        #输入邮箱，邮箱为用户名@scutech.com
        emailAddress=name+'@scutech.com'
        dbackupServer.find_element_by_id("email").clear()
        dbackupServer.find_element_by_id("email").send_keys(emailAddress)
        #输入联系方式，为了简便直接输入用户名
        dbackupServer.find_element_by_id("telephone").clear()
        dbackupServer.find_element_by_id("telephone").send_keys(name)
        #为前面6个加上系统管理权限
        if count<=6:
            dbackupServer.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[12]/td[2]/table/tbody/tr/td[1]/label/input").click()
            count=count+1
        #点击“提交”按钮
        dbackupServer.find_element_by_id("RegisterBut").click()
 	    #设置等待时间
	    #time.sleep(3)       
        a=dbackupServer.switch_to_alert()
        a.accept()
        driver.Navigate().Back()
        time.sleep(3)
        action_chains.move_to_element(dbackupServer.find_element_by_link_text("授权管理")).perform()	
        action_chains.click(dbackupServer.find_element_by_link_text("序列号信息")).perform()    

    print 'regist done!'
    
#调用登陆和注册方法
login()
userAdd()
        
    

    
