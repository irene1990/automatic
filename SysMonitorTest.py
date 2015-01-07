#!/usr/bin/python
#coding=utf-8
#file:netiostat

###############################################
##	Author:wudongliang
##	Email:wudongliang@dashagua.cn
##	Version:1.0
##	Discription:CPU&Mem Percent   Sent&Recv KB/s
################################################

import os,psutil,time,sys

def sysStat(sleep=5):
    fname=''
    for x in list(time.localtime(time.time())[:]):
        fname=fname+str(x)
    fname=fname+'.xls'
    filelog = open(fname,'w')
    count = 1
    print 'Cou \t CPU \t Mem \t Sent \t Recv'
    filelog.write('Count \t CPU \t Mem \t Sent \t Recv\n')
    while True:
        netSentStart = psutil.net_io_counters()[0]
        netRecvStart = psutil.net_io_counters()[1]
        time.sleep(1)
        netSentEnd = psutil.net_io_counters()[0]
        netRecvEnd = psutil.net_io_counters()[1]
    
        netSent = (netSentEnd - netSentStart)/1024
        netRecv = (netRecvEnd - netRecvStart)/1024
        time.sleep(sleep-1)
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()[2]

        message = str(count) + '\t' + '% 4.1f'%cpu +'\t'+'% 4.1f'%memory +'\t' + '%.2f'%netSent + '\t' + '%.2f'%netRecv 
        print message
        filelog.write(message+'\n')
        count+=1

if __name__ == '__main__':
    sysStat()
