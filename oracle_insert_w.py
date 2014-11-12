#-*-coding=utf-8
#import cx_Oracle,time,sys
#sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/user_defined')
#from random_char import Random_Char
#conn = cx_Oracle.connect("system/Dingjia123@192.168.88.244:1521/ORCL")
#c = conn.cursor()
#print 'you have already in oracle'
#time.sleep(10800)
#tablespace = ['orcl_1','orcl_2']
#i = 300
#s = 400
#Random_Char是我自己写的一个函数，用来获取随机字符的。下面sql2中 r.c_l_n(30,50)，就是我调用了这个函数的某个方法去获取有大写+小写+数字组成的，长度为30～50之间的随机字符
#sql1 = "create table " + tablespace[i] +'_' + str(k) + "(id number(20),a varchar2(200),b varchar2(200),c varchar2(200),d varchar2(200),e varchar2(200),f varchar2(200),g varchar2(200),h varchar2(200),i varchar2(200),j varchar2(200),k varchar2(200),l varchar2(200),m varchar2(200),n varchar2(200),o varchar2(200),p varchar2(200),q varchar2(200),r varchar2(200),s varchar2(200),t varchar2(200),u varchar2(200),v varchar2(200),w varchar2(200),x varchar2(200),y varchar2(200),z varchar2(200)) tablespace " + tablespace[i],'three','four','five','six','seven','eight','night','ten'
#r = Random_Char(1)
#add tables
#while i < len(tablespace) :
#    m = 0
#    while m < 10:
#        sql1 = "create table " + tablespace[i] +'_' + str(m) + "(id number(20),a varchar2(200),b varchar2(200),c varchar2(200),d varchar2(200),e varchar2(200),f varchar2(200),g varchar2(200),h varchar2(200),i varchar2(200),j varchar2(200),k varchar2(200),l varchar2(200),m varchar2(200),n varchar2(200),o varchar2(200),p varchar2(200),q varchar2(200),r varchar2(200),s varchar2(200),t varchar2(200),u varchar2(200),v varchar2(200),w varchar2(200),x varchar2(200),y varchar2(200),z varchar2(200)) tablespace " + tablespace[i]
#        m += 1
#        print sql1
#        c.execute(sql1)
#        conn.commit()
#        time.sleep(60)
#        print '======================='+str(i)+'==================='+str(m)+'==========================================='
#    i += 1
#while i< s:
#    m = 0
#    while m<len(tablespace):
#        k = 0
#        while k<10:
#            sql2 = 'insert into ' + tablespace[m] +'_' + str(k) + ' values('+str(i)+",'"+str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time())))+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"')"
#            k += 1
#            print sql2
           #执行和提交sql
#            c.execute(sql2)
#            conn.commit()
#        m +=1
#    print '=========================================='+str(i)+'==========================================='
#    i += 1
#    time.sleep(1)
#     sql = "insert into system.first values(" + str(i) + ",'" + str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time()))) + "')"
# sql1 = "select name from v$datafile"
# r = c.execute(sql1)
# li = r.fetchall()
# for row in li:
#     print row
#c.close()
#conn.close()


import cx_Oracle,time,random,sys
sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/user_defined')
from random_char import Random_Char
#conn = cx_Oracle.connect("system/Scutech123@192.168.88.218:1521/rac.localdomain")
#conn = cx_Oracle.connect("system/dingjia@192.168.88.77:1521/test")
#conn = cx_Oracle.connect("system/dingjia@192.168.88.222:1521/orcl")
#conn = cx_Oracle.connect("system/dingjia@192.168.88.239:1521/orcl")
conn = cx_Oracle.connect("system/dingjia@192.168.88.207:1521/whole")
c = conn.cursor()
r = Random_Char(1)
print 'you have already in oracle'
f = open("insert_207.log", 'a')
k=12001
ak = k+2000
#table = ['CUSTOM_DETAIL_ZHEJIANG','CUSTOM_DETAIL_XINJIANG','CUSTOM_DETAIL_XIANGGANG','CUSTOM_DETAIL_WUHAN','CUSTOM_DETAIL_TIANJIN','CUSTOM_DETAIL_SHENZHEN','CUSTOM_DETAIL_SHANGHAI','CUSTOM_DETAIL_JIANGXI','CUSTOM_DETAIL_GUANGZHOU','CUSTOM_DETAIL_FUJIAN','CUSTOM_DETAIL_CHANGSHA','CUSTOM_DETAIL_BEIJING','GOODS_DETAIL_ZHEJIANG','GOODS_DETAIL_XINJIANG','GOODS_DETAIL_XIANGGANG','GOODS_DETAIL_WUHAN','GOODS_DETAIL_TIANJIN','GOODS_DETAIL_SHENZHEN','GOODS_DETAIL_SHANGHAI','GOODS_DETAIL_JIANGXI','GOODS_DETAIL_GUANGZHOU','GOODS_DETAIL_FUJIAN','GOODS_DETAIL_CHANGSHA','GOODS_DETAIL_BEIJING','SUPPLIER_DETAIL_ZHEJIANG','SUPPLIER_DETAIL_XINJIANG','SUPPLIER_DETAIL_XIANGGANG','SUPPLIER_DETAIL_WUHAN','SUPPLIER_DETAIL_TIANJIN','SUPPLIER_DETAIL_SHENZHEN','SUPPLIER_DETAIL_SHANGHAI','SUPPLIER_DETAIL_JIANGXI','SUPPLIER_DETAIL_GUANGZHOU','SUPPLIER_DETAIL_FUJIAN','SUPPLIER_DETAIL_CHANGSHA','SUPPLIER_DETAIL_BEIJING']
table = ['CUSTOM_DETAIL222_ZHEJIANG','CUSTOM_DETAIL222_XINJIANG','CUSTOM_DETAIL222_XIANGGANG','CUSTOM_DETAIL222_WUHAN','CUSTOM_DETAIL222_TIANJIN','CUSTOM_DETAIL222_SHENZHEN','CUSTOM_DETAIL222_SHANGHAI','CUSTOM_DETAIL222_JIANGXI','CUSTOM_DETAIL222_GUANGZHOU','CUSTOM_DETAIL222_FUJIAN','CUSTOM_DETAIL222_CHANGSHA','CUSTOM_DETAIL222_BEIJING','GOODS_DETAIL222_ZHEJIANG','GOODS_DETAIL222_XINJIANG','GOODS_DETAIL222_XIANGGANG','GOODS_DETAIL222_WUHAN','GOODS_DETAIL222_TIANJIN','GOODS_DETAIL222_SHENZHEN','GOODS_DETAIL222_SHANGHAI','GOODS_DETAIL222_JIANGXI','GOODS_DETAIL222_GUANGZHOU','GOODS_DETAIL222_FUJIAN','GOODS_DETAIL222_CHANGSHA','GOODS_DETAIL222_BEIJING','SUPPLIER_DETAIL222_ZHEJIANG','SUPPLIER_DETAIL222_XINJIANG','SUPPLIER_DETAIL222_XIANGGANG','SUPPLIER_DETAIL222_WUHAN','SUPPLIER_DETAIL222_TIANJIN','SUPPLIER_DETAIL222_SHENZHEN','SUPPLIER_DETAIL222_SHANGHAI','SUPPLIER_DETAIL222_JIANGXI','SUPPLIER_DETAIL222_GUANGZHOU','SUPPLIER_DETAIL222_FUJIAN','SUPPLIER_DETAIL222_CHANGSHA','SUPPLIER_DETAIL222_BEIJING']
while k < ak:
    i = 0
    s=random.randint(1,100000000000000)
    while i< len(table):
        sql2 = 'insert into ' + table[i] + ' values('+str(k)+",'"+r.c_l_n(10,20)+"','"+r.c_l_n(10,20)+"',"+str(s)+","+str(s)+",'"+r.c_l_n(10,20)+"','"+r.c_l_n(10,20)+"',"+str(s)+')'
        print sql2
        #执行和提交sql
        c.execute(sql2)
        conn.commit()
        f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"-----")
        f.write(sql2+"\n")
        i += 1
    print '=========================================='+str(k)+'==========================================='
    #time.sleep(60)
    k +=1
c.close()
conn.close()