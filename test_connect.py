import cx_Oracle,time,sys
#conn = cx_Oracle.connect("system/Scutech123@192.168.82.202:1521/orcl")
#conn = cx_Oracle.connect("system/Dingjia123@192.168.82.37:1521/orcl11gR2")
#conn = cx_Oracle.connect("system/dingjia@192.168.82.244:1521/orcl")
conn = cx_Oracle.connect("system/Dingjia123@192.168.82.34:1521/orcl")
c = conn.cursor()
print 'you have already in oracle'
