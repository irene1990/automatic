import sys,time,MySQLdb
sys.path.append(r'/home/irene/Eclipse/workspace/Dbackup/webautotest/user_defined')
from random_char import Random_Char
try:
    r = Random_Char(1)
    num = 80000 
    conn = MySQLdb.connect(host='192.168.88.198',user='wangsx',passwd='dingjia',port=3306)
    cur = conn.cursor()
    while num < 90000:
        i = 0
        while i<6:
            u = 'use big_data' + str(i) + ';'
            cur.execute(u)
            print u
            k = 0
            while k < 10:
                #sql1 = "create table propro" + str(k) + "(id int,a varchar(200),b varchar(200),c varchar(200),d varchar(200),e varchar(200),f varchar(200),g varchar(200),h varchar(200),i varchar(200),j varchar(200),k varchar(200),l varchar(200),m varchar(200),n varchar(200),o varchar(200),p varchar(200),q varchar(200),r varchar(200),s varchar(200),t varchar(200),u varchar(200),v varchar(200),w varchar(200),x varchar(200),y varchar(200),z varchar(200));"
                sql1 = 'insert into propro' + str(k) + ' values('+str(num)+",'"+str(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime(time.time())))+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"','"+r.c_l_n(30,50)+"');"
                print sql1
                cur.execute(sql1)
                conn.commit()
                k += 1
            i +=1
        num +=1
        #time.sleep(1)
        print '============'+str(num)+'==========='+ str(i) +'========================'
    cur.close() 
    conn.close()
    print 'Insert Data Finished ! '
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0],e.args[1])
