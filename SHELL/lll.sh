#!/usr/bin/expect
spawn ./install.sh
expect "spawn ./install.sh
Pseudo-terminal will not be allocated because stdin is not a terminal.
root@192.168.88.236's password:"
send "dingjia\r"}
#expect "root@192.168.88.236's password:"
#send "dingjia\r"}
interact
