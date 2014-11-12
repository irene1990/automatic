#!/usr/bin/expect
set timeout 30
#set num [lindex $argv 0]
set p1 [lindex $argv 0]
set IP [lindex $argv 1]
spawn scp $p1 root@192.168.88.$IP:/root
expect "root@192.168.88.$IP's password:"
send "dingjia\r"
interact