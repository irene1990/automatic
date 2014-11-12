#!/usr/bin/expect
set timeout 30
set IP [lindex $argv 0]
spawn ssh root@192.168.82.$IP
expect "root@192.168.82.$IP's password:"
send "dingjia\r"
interact
