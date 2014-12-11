#-*-coding=utf-8
import cx_Oracle,time,sys
sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/user_defined')
#conn = cx_Oracle.connect("system/dingjia@192.168.82.244:1521/orcl")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.82.34:1521/orcl")
#conn = cx_Oracle.connect("system/Dingjia123@node1-scan:1521/orcl.localdomain")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.88.75:1521/wangsx")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.82.164:1521/orcl")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.82.155:1521/orcl.localdomain")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.82.40:1521/orcl.localdomain")
conn = cx_Oracle.connect("system/Dingjia123@192.168.82.33:1521/orcl.localdomain")
from random_char import Random_Char
c = conn.cursor()
r = Random_Char(1)
tablespace = ['kk','ww']
#i = 0
#print "****************************************************************************"
#create tablespace
#while i <len(tablespace):
#    sql0 = "create tablespace "+tablespace[i]+" datafile '/home/oracle/151/data/orcl/datafile/"+tablespace[i]+".dbf' size 1024m"
#    print sql0
#    c.execute(sql0)
#    conn.commit
#    i += 1
#i = 0
#create ten tables in every tablespace
#print "****************************************************************************"
#i = 0
#while i<len(tablespace):
#    m = 2
#    while m < 10:
#        sql1 = "create table " + tablespace[i] +'_' + str(m) + "(id number(20),ttime date,a varchar2(200),b varchar2(200),c varchar2(200),d varchar2(200),e varchar2(200),f varchar2(200),g varchar2(200),h varchar2(200),i varchar2(200),j varchar2(200),k varchar2(200),l varchar2(200),m varchar2(200),n varchar2(200),o varchar2(200),p varchar2(200),q varchar2(200),r varchar2(200),s varchar2(200),t varchar2(200),u varchar2(200),v varchar2(200),w varchar2(200),x varchar2(200),y varchar2(200),z varchar2(200)) tablespace " + tablespace[i]
#        print sql1
#        c.execute(sql1)
#        conn.commit()
#        m += 1
#    i += 1
print "****************************************************************************"
n = 100
nn = 100000
#insert datas in every tables
while n<nn:
    i = 0
    while i < len(tablespace):
        m = 0
        while m < 10:
            sql2 = 'insert into ' + tablespace[i] +'_' + str(m) + ' values('+str(n)+",sysdate,'"+str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time())))+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"')"
            print sql2
            c.execute(sql2)
            conn.commit()
            m += 1
        i += 1
    n += 1
    time.sleep(3)
c.close()
conn.close()
