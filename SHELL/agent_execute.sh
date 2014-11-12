#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   install agents                        @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##ssh root@192.168.88.232 'rm -rf /root/dbackup*'
##ssh root@192.168.88.229 'rm -rf /root/dbackup*'
##ssh root@192.168.88.205 'rm -rf /root/dbackup*'
##ssh root@192.168.88.236 'rm -rf /root/dbackup*'
#ssh root@192.168.88.232 'dpkg -i /root/'$1
#ssh root@192.168.88.232 'apt-get -f install'
#ssh root@192.168.88.232 'service dbackup_agentd config'
#ssh root@192.168.88.229 'dpkg -i /root/'$1
#ssh root@192.168.88.229 'apt-get -f install '
#ssh root@192.168.88.229 'service dbackup_agentd config'
#ssh root@192.168.88.205 'rpm -ivh /root/'$2
#ssh root@192.168.88.205 '/etc/init.d/dbackup_agentd config'
./send_agents.sh $# $1 $2 $3 $4 $5 $6 $7 $8
ssh root@192.168.88.$1 'rpm -ivh /root/'$5
ssh root@192.168.88.$1 '/etc/init.d/dbackup_agentd config'
ssh root@192.168.88.$2 'rpm -ivh /root/'$6
ssh root@192.168.88.$2 '/etc/init.d/dbackup_agentd config'
ssh root@192.168.88.$3 'rpm -ivh /root/'$7
ssh root@192.168.88.$3 '/usr/sbin/dbackup_agentd config'
ssh root@192.168.88.$4 'rpm -ivh /root/'$8
ssh root@192.168.88.$4 '/usr/sbin/dbackup_agentd config'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   uinstall agents                       @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#echo 'Uinstall 232'
#ssh root@192.168.88.232 'apt-get autoremove dbackup-agent'
#ssh root@192.168.88.232 'apt-get autoremove dbackup-rdiff'
#ssh root@192.168.88.232 'apt-get autoremove dbackup-fsync'
#ssh root@192.168.88.232 'apt-get autoremove dbackup-standby'
#echo 'Uinstall 229'
#*ssh root@192.168.88.229 'apt-get autoremove dbackup-agent'
#*ssh root@192.168.88.229 'apt-get autoremove dbackup-rdiff'
#ssh root@192.168.88.229 'apt-get autoremove dbackup-fsync'
#ssh root@192.168.88.229 'apt-get autoremove dbackup-standby'
#echo 'Uinstall 205'
#ssh root@192.168.88.205 'rpm -e dbackup-agent dbackup-standby dbackup-rdiff'
#echo 'Uinstall 236'
#ssh root@192.168.88.236 'rpm -e dbackup-agent'
#echo 'remove file from 232 229 236'
#ssh root@192.168.88.232 'rm -rf /etc/opt/scutech /var/opt/scutech /opt/scutech /inforkist*'
#ssh root@192.168.88.229 'rm -rf /etc/opt/scutech /var/opt/scutech /opt/scutech /inforkist*'
#ssh root@192.168.88.205 'rm -rf /etc/opt/scutech /var/opt/scutech /opt/scutech /inforkist*'
#ssh root@192.168.88.236 'rm -rf /etc/opt/scutech /var/opt/scutech /opt/scutech /inforkist*'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   install rdiff                         @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#./send_agents.sh $# $1 $2 $3 $4 $5 $6 $7 $8
#ssh root@192.168.88.232 'dpkg -i /root/'$1
#ssh root@192.168.88.232 'rdiff-backup-config'
#ssh root@192.168.88.229 'dpkg -i /root/'$1
#ssh root@192.168.88.205 'rpm -ivh /root/'$2
#ssh root@192.168.88.205 'rdiff-backup-config'
#ssh root@192.168.88.236 'rpm -ivh /root/'$3
#ssh root@192.168.88.236 'rdiff-backup-config'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   install standby                       @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#./send_agents.sh $# $1 $2 $3 $4 $5 $6 $7 $8
#ssh root@192.168.88.232 'dpkg -i /root/'$1
#ssh root@192.168.88.229 'dpkg -i /root/'$1
#ssh root@192.168.88.$1 'rpm -ivh /root/'$1
#ssh root@192.168.88.$2 'rpm -ivh /root/'$2
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   install fsync                         @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#./send_agents.sh $# $1 $2 $3 $4 $5 $6 $7 $8
#ssh root@192.168.88.232 'dpkg -i /root/'$1
#ssh root@192.168.88.232 '/etc/init.d/dbackup-fsync config'
#ssh root@192.168.88.229 'dpkg -i /root/'$1
#ssh root@192.168.88.205 'rpm -ivh /root/'$2
#ssh root@192.168.88.205 '/etc/init.d/dbackup-fsync config'
#ssh root@192.168.88.236 'rpm -ivh /root/'$3
#ssh root@192.168.88.236 '/etc/init.d/dbackup-fsync config'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                   remove other packges                  @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
./send_agents.sh $# $1 $2 $3 $4
ssh root@192.168.88.$1 'rm -rf /root/dbackup*deb /root/dbackup*i686*rpm *.sh'
# 232 rhel
ssh root@192.168.88.$1 'rm -rf /root/dbackup*deb /root/dbackup*x86_64*rpm *.sh'
# 229 rhel
ssh root@192.168.88.$2 'rm -rf /root/dbackup*deb /root/dbackup*x86_64*rpm *.sh'
# 77
ssh root@192.168.88.$3 'rm -rf /root/dbackup*deb /root/dbackup*x86_64*rpm *.sh'
# 91
ssh root@192.168.88.$4 'rm -rf /root/dbackup*deb /root/dbackup*x86_64*rpm *.sh'

#ssh root@192.168.88.232 'rm -rf /root/dbackup*rpm'
#ssh root@192.168.88.229 'rm -rf /root/dbackup*rpm'