#echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
#echo '@                        Install Server                               @'
#echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
./send_server.sh $1 $2
ssh root@192.168.88.$2 'dpkg -i /root/'$1
#ssh root@192.168.88.$2 'apt-get -f install'
#echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
#echo '@                        uinstall Server                              @'
#echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
#ssh root@192.168.88.$1 'apt-get autoremove dbackup-server'
#ssh root@192.168.88.$1 'dpkg --purge dbackup-server'
#ssh root@192.168.88.$1 'rm -rf /etc/opt/scutech /var/opt/scutech /opt/scutech /var/preserve/scutech'
#Rejested User
#python UserAdd.py
