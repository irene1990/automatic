#import MySQLdb
#conn204 = MySQLdb.connect(host='192.168.82.204',user='wangsx',passwd='Dingjia123',port=3306)  
#cur204 = conn204.cursor()  
#cur204.execute('create database test_7')
#conn204.select_db('test_7')  
#cur204.execute('create table seven_seven(id int,info varchar(20))')
#conn204.commit()
#value204 = [3,'after upgrade']  
#cur204.execute('insert into seven_seven values(%s,%s)',value204)  
#conn204.commit()  
#cur204.close()  
#conn204.close()
#conn201 = MySQLdb.connect(host='192.168.82.201',user='mengze',passwd='Dingjia123',port=3306)  
#cur201 = conn201.cursor()  
#cur201.execute('create database test_7')
#conn201.select_db('test_7')  
#cur201.execute('create table seven_seven(id int,info varchar(20))')
#conn201.commit()
#value201 = [3,'after upgrade']  
#cur201.execute('insert into seven_seven values(%s,%s)',value201)  
#conn201.commit()  
#cur201.close()  
#conn201.close()


import MySQLdb,time
conn = MySQLdb.connect(host='192.168.82.204',user='wangsx',passwd='Dingjia123',port=3306)  
cur = conn.cursor()  
m = 0
k = [3,4,5,6,7]
while m < 1000 :
    i = 3
    for i in k:
        dbname = "test_"+str(i)
        print dbname
        tname = ['three_three','four_four','five_five','six_six','seven_seven']
        conn.select_db(dbname)
        va = 'automatic_restore' + str(m)
        ins = 'insert into ' + tname[i-3] + ' values(' + str(m) + ',"' + va +'")'
        print ins
        cur.execute(ins)
        conn.commit()
    m += 1
    time.sleep(10)
cur.close()
conn.close()