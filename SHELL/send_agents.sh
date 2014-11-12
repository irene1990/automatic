#!/usr/bin/expect
set timeout 30
set num [lindex $argv 0]
for {set i 1} {$i<=$num} {incr i} {
set IP 0
set IP [lindex $argv $i]
#spawn scp -r /home/irene/Eclipse/workspace/Dbackup/z_test/SHELL/3.1/ root@192.168.88.$IP:/root
spawn scp -r /home/irene/Eclipse/workspace/Dbackup/z_test/SHELL/4.0/dbackup-standby-4.0.487-1.dev.i686.rpm root@192.168.88.$IP:/root
expect "root@192.168.88.$IP's password:"
send "dingjia\r"
}
interact
#set p1 [lindex $argv 1]
#set p2 [lindex $argv 2]
#set p3 [lindex $argv 3]
#for {set i 4} {$i<=$num} {incr i} {
#set nu [lindex $argv $i]
#set IP 0
#if {$nu!=""} {
#set IP [lindex $argv $i]
#spawn scp $p1 $p2 $p3 root@192.168.88.$IP:/root
#expect "root@192.168.88.$IP's password:"
#send "dingjia\r"}
#}
#interact


