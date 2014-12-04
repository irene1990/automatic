#prepration before install Oracle 11.2.0.4 in Centos
echo "############################Add Users####################################"
groupadd -g 501 oinstall
groupadd -g 502 dba
groupadd -g 503 asmadmin
groupadd -g 504 asmdba
groupadd -g 505 asmoper
useradd -u 506 -g oinstall -G asmadmin,asmdba,asmoper grid
useradd -u 507 -g oinstall -G dba,asmdba oracle
passwd grid
passwd oracle
echo "session    required     pam_limits.so" >> /etc/pam.d/login

echo "############################Add Directory####################################"
mkdir -p /u01/app/oraInventory
chown -R grid:oinstall /u01/app/oraInventory
chmod -R 775 /u01/app/oraInventory
mkdir -p /u01/11.2.0/grid
chown -R grid:oinstall /u01/11.2.0/grid
chmod -R 775 /u01/11.2.0/grid
mkdir -p /u01/app/grid
chown -R grid:oinstall /u01/app/grid
chmod -R 775 /u01/app/grid
mkdir -p /u01/app/oracle
mkdir /u01/app/oracle/cfgtoollogs
chown -R oracle:oinstall /u01/app/oracle
chown -R oracle:oinstall /u01/app/oracle/cfgtoollogs
chmod -R 775 /u01/app/oracle
chmod -R 775 /u01/app/oracle/cfgtoollogs
mkdir -p /u01/app/oracle/product/11.2.0/db_1
chown -R oracle:oinstall /u01/app/oracle/product/11.2.0/db_1
chmod -R 775 /u01/app/oracle/product/11.2.0/db_1

echo "############################Installing packages####################################"
yum install binutils
yum install elfutils-libelf
yum install libaio-devel
yum install libaio-devel.i686
yum install sysstat
yum install libgcc
yum install libgcc.i686
yum install libstdc++
yum install libstdc++.i686
yum install libstdc++-devel
yum install libstdc++-devel.i686
yum install compat-libstdc++-33
yum install gcc
yum install glibc
yum install glibc.i686
yum install glibc-devel
yum install glibc-devel.i686
yum install gcc-c++
yum install elfutils-libelf-devel
yum install elfutils-libelf-devel.i686
yum install unixODBC-devel
yum install unixODBC-devel.i686
yum install compat-libcap1

echo "############################/etc/security/limits.conf####################################"
echo "####################vi /etc/security/limits.conf
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
grid soft nproc 2047
grid hard nproc 16384
grid soft nofile 1024
grid hard nofile 65536">>/etc/security/limits.conf

echo "############################/etc/sysctl.conf####################################"
echo "####################vi /etc/sysctl.conf
fs.aio-max-nr = 1048576
fs.file-max = 6815744
kernel.shmall = 2097152
kernel.shmmax = 851210240
kernel.shmmni = 4096
# semaphores: semmsl, semmns, semopm, semmni
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default=262144
net.core.rmem_max=4194304
net.core.wmem_default=262144
net.core.wmem_max=1048586">>/etc/sysctl.conf

/sbin/sysctl -p

echo "############################/etc/hosts####################################"
echo "127.0.0.1       localhost.localdomain   localhost
# Public
192.168.82.151   node1.localdomain        node1
192.168.82.152   node2.localdomain        node2
# Private
192.168.55.151   node1-priv.localdomain   node1-priv
192.168.55.152   node2-priv.localdomain   node2-priv
# Virtual
192.168.82.153   node1-vip.localdomain    node1-vip
192.168.82.154   node2-vip.localdomain    node2-vip
# SCAN
192.168.82.155   node1-scan.localdomain node1-scan">>/etc/hosts

sleep 120
echo "############################enviroment of oracle####################################"
echo "##############################enviroment of oracle
TMP=/tmp;export TMP 
TMPDIR=/tmp;export TMPDIR
ORACLE_TERM=xterm;export ORACLE_TERM
TNS_ADMIN=$ORACLE_HOME/network/admin;export TNS_ADMIN
ORA_NLS11=$ORACLE_HOME/nls/data;export ORA_NLS11
ORACLE_BASE=/u01/app/oracle;export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/11.2.0/db_1;export ORACLE_HOME
ORACLE_SID=racdb11;export ORACLE_SID
ORACLE_HOSTNAME=node1.localdomain;export ORACLE_HOSTNAME
ORACLE_UNQNAME=orcl;export ORACLE_UNQNAME
PATH=${PATH}:/usr/bin:/bin:/usr/bin/X11:/usr/local/bin;export PATH
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib:/lib:/usr/lib:/usr/local/lib:/usr/lib64:/usr/local/lib64;export LD_LIBRARY_PATH
CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib;export CLASSPATH
PATH=$ORACLE_HOME/bin:/usr/sbin:$PATH;export PATH
THREADS_FLAG=native;export THREADS_FLAG
#DISPLAY=x.x.x.x:0.0;export DISPLAY
umask=022
if [ $USER = "oracle" ]; then
  if [ $SHELL = "/bin/ksh" ]; then
    ulimit -p 16384
    ulimit -n 65536
  else
    ulimit -u 16384 -n 65536
  fi
fi">>/home/oracle/.bash_profile

echo "############################enviroment of grid####################################"
echo "#####################enviroment of grid
TMP=/tmp;export TMP
TMPDIR=/tmp;export TMPDIR
ORACLE_BASE=/u01/app/grid;export ORACLE_BASE
ORACLE_HOME=/u01/11.2.0/grid;export ORACLE_HOME
ORACLE_SID=+ASM1;export ORACLE_SID
ORACLE_TERM=xterm;export ORACLE_TERM
TNS_ADMIN=$ORACLE_HOME/network/admin;export TNS_ADMIN
ORA_NLS11=$ORACLE_HOME/nls/data;export ORA_NLS11
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib:/lib:/usr/lib:/usr/local/lib:/usr/lib64:/usr/local/lib64;export LD_LIBRARY_PATH
PATH=$ORACLE_HOME/bin:/usr/sbin:$PATH;export PATH PATH=${PATH}:/usr/bin:/bin:/usr/bin/X11:/usr/local/bin;export PATH
CLASSPATH=${CLASSPATH}:$ORACLE_HOME/rdbms/jlib:$ORACLE_HOME/network/jlib;export CLASSPATH  THREADS_FLAG=native;export THREADS_FLAG
#DISPLAY=x.x.x.x:0.0;export DISPLAY
umask=022">>/home/grid/.bash_profile

