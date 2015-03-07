echo "deb http://192.168.88.10/scutech/precise precise main universe
deb http://192.168.88.10/scutech/ubuntu oneiric main universe">>/etc/apt/sources.list.d/scutech.list
apt-get install python-software-properties
add-apt-repository ppa:likemartinma/devel
add-apt-repository ppa:likemartinma/net
apt-add-repository ppa:likemartinma/python
apt-get update
apt-get -y --force-yes dist-upgrade
apt-get install scutech-nas-plugin
apt-get install infokist
apt-get install git
apt-get install scutech-tapelib-server
sudo useradd -M -s /sbin/nologin obackup
apt-get install samba
touch /etc/samba/smbpasswd
smbpasswd -a obackup
mkdir -p /infokist/obackup
chown -R obackup:obackup /infokist/obackup
cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
echo "[obackup]
comment = Shared Folder for guest
path = /infokist/obackup/
public = yes
guest ok = no
writable = yes
#valid users = share
create mask = 0700
directory mask = 0700
force user = obackup
force group = obackup
available = yes
browseable = yes">>/etc/samba/smb.conf
/etc/init.d/smbd restart
git clone https://github.com/markh794/mhvtl.git
sudo apt-get -y install make gcc linux-headers-`uname -r` lsscsi sg3-utils zlib1g-dev liblzo2-dev
cd mhvtl/kernel
make
sudo make install
cd ..
sudo groupadd --system vtl
sudo useradd --system -c "Vitrual Tape Library" -d /opt/vtl -g vtl -m vtl
make
sudo make install
sudo chown -R vtl:vtl /opt/mhvtl
sudo service mhvtl start
lsscsi -g
apt-get install lftp
