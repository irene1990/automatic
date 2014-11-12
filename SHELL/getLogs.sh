#!/usr/bin/expect
set timeout 30
set num [lindex $argv 0]
for {set i 1} {$i<=$num} {incr i} {
set IP 0
set IP [lindex $argv $i]
spawn mkdir -p /home/irene/Desktop/log/192.168.82.$IP
spawn scp -r root@192.168.82.$IP:/var/log/dbackup_agent/ /home/irene/Desktop/log/192.168.82.$IP/
expect "root@192.168.82.$IP's password:"
send "dingjia\r"
spawn scp -r root@192.168.82.$IP:/var/log/dbackup_standby/ /home/irene/Desktop/log/192.168.82.$IP/
expect "root@192.168.82.$IP's password:"
send "dingjia\r"
}
interact

