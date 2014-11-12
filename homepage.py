#-*-coding=utf-8
import sys,time
sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/model/system')
from Login import Login
from User import User
from selenium import webdriver
driver = webdriver.Firefox()

#~~~~~~~~~~~~~~~~~~~~~~~~登录~~~~~~~~~~~~~~~~~~~~~~~~~
#Login(ip,username,password)
l = Login("192.168.88.243","admin","admin",driver)
l.test_login()
#~~~~~~~~~~~~~~~~~~~~~~~~登录成功~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~用户~~~~~~~~~~~~~~~~~~~~~
#User(driver)
#AddUser(name,password,email,telephone,privilege)
#privilege---1:系统权限；2:上级监控；3:备份恢复；4:查看报表
u = User(driver)
u.AddUser("dingjia","dingjia123","1111@qq.com","123456789","14")
#time.sleep(5)
#u.DeleteUser("kkkkkk3",'n')
#u.LockUser("dingjia",'y')
#u.UnlockUser("dingjia",'y')
#u.ModifidUser('dingjia','','','24')
#VisitedCient(user,clients),client多客户端由;号分开
#u.VisitedCient(u,"dingjia","localhost.localdomain_192.168.88.215;rhel5_mysql_216")
#~~~~~~~~~~~~~~~~~~~~~~~~用户成功~~~~~~~~~~~~~~~~~~~~~
driver.quit()
