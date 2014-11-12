#-*-coding=utf-8
import cx_Oracle,time,sys
#sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/user_defined')
#conn = cx_Oracle.connect("system/dingjia@192.168.82.244:1521/orcl")
conn = cx_Oracle.connect("system/Dingjia123@192.168.82.34:1521/orcl")
#from random_char import Random_Char
#conn = cx_Oracle.connect("system/Dingjia123@192.168.88.75:1521/wangsx")
c = conn.cursor()
#print 'you have already in oracle'
#tablespace = ['three','four']
#i =0
#Random_Char是我自己写的一个函数，用来获取随机字符的。下面sql2中 r.c_l_n(30,50)，就是我调用了这个函数的某个方法去获取有大写+小写+数字组成的，长度为30～50之间的随机字符
#sql1 = "create table " + tablespace[i] +'_' + str(k) + "(id number(20),a varchar2(200),b varchar2(200),c varchar2(200),d varchar2(200),e varchar2(200),f varchar2(200),g varchar2(200),h varchar2(200),i varchar2(200),j varchar2(200),k varchar2(200),l varchar2(200),m varchar2(200),n varchar2(200),o varchar2(200),p varchar2(200),q varchar2(200),r varchar2(200),s varchar2(200),t varchar2(200),u varchar2(200),v varchar2(200),w varchar2(200),x varchar2(200),y varchar2(200),z varchar2(200)) tablespace " + tablespace[i],'three','four','five','six','seven','eight','night','ten'
#r = Random_Char(1)
#add tables
#while i < len(tablespace) :
#    m = 0
#    while m < 20:
#        sql1 = "create table " + tablespace[i] +'_' + str(m) + "(id number(20),a varchar2(200),b varchar2(200),c varchar2(200),d varchar2(200),e varchar2(200),f varchar2(200),g varchar2(200),h varchar2(200),i varchar2(200),j varchar2(200),k varchar2(200),l varchar2(200),m varchar2(200),n varchar2(200),o varchar2(200),p varchar2(200),q varchar2(200),r varchar2(200),s varchar2(200),t varchar2(200),u varchar2(200),v varchar2(200),w varchar2(200),x varchar2(200),y varchar2(200),z varchar2(200)) tablespace " + tablespace[i]
#        m += 1
#        print sql1
#        c.execute(sql1)
#        conn.commit()
#        time.sleep(1)
#        print '======================='+str(i)+'==================='+str(m)+'==========================================='
#    i += 1
#while i< 500000:
#    m = 0
#    while m<len(tablespace):
#        k = 0
#        while k<20:
#            sql2 = 'insert into ' + tablespace[m] +'_' + str(k) + ' values('+str(i)+",'"+str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time())))+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"')"
#            k += 1
#            print sql2
           #执行和提交sql
#            c.execute(sql2)
#            conn.commit()
#        m +=1
#    print '=========================================='+str(i)+'==========================================='
#    i += 1
    #time.sleep(2)
#     sql = "insert into system.first values(" + str(i) + ",'" + str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time()))) + "')"
# sql1 = "select name from v$datafile"
# r = c.execute(sql1)
# li = r.fetchall()
# for row in li:
#     print row
#c.close()
#conn.close()
k=4
mk=2000
#sql = "create tablespace local_244 datafile '/u01/app/product/10.2.0/db_1/oradata/orcl/local_244.dbf' size 10m"
#print sql
#c.execute(sql)
#conn.commit
#sql0 = "create table kk(name varchar2(200),ttime date) tablespace local_244"
#sql0 = "create table kk(name varchar2(200),ttime date) tablespace local_33"
sql0 = "create table ww(name varchar2(200),ttime date) tablespace local_33"
print sql0
c.execute(sql0)
conn.commit
while k < mk:
    sql1 = "insert into kk values('after upgade',sysdate)"
    print sql1
    c.execute(sql1)
    conn.commit()
    sql2 = "insert into ww values('after upgade',sysdate)"
    print sql2
    c.execute(sql2)
    conn.commit()
    k += 1
    time.sleep(3)
c.close()
conn.close()
