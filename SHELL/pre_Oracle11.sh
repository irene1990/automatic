#Prepare job before install Oracle11.2.0.4 in RHEL6
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


rpm -ivh /mnt/Packages/binutils-2.*86_64*
rpm -ivh /mnt/Packages/elfutils-libelf-0.*86_64*
rpm -ivh /mnt/Packages/libaio-0.*
rpm -ivh /mnt/Packages/libaio-devel-0.*
rpm -ivh /mnt/Packages/sysstat-9.*
rpm -ivh /mnt/Packages/kernel-headers*86_64*
rpm -ivh /mnt/Packages/glibc-2.*x86_64* 
rpm -ivh /mnt/Packages/glibc-common-2.*x86_64*
rpm -ivh /mnt/Packages/glibc-headers-2.*x86_64*
rpm -ivh /mnt/Packages/glibc-devel*86_64*
rpm -ivh /mnt/Packages/glibc-2.12-1.7.el6.i686.rpm /mnt/Packages/nss-softokn-freebl-3.12.7-1.1.el6.i686.rpm
rpm -ivh /mnt/Packages/ksh-2*
rpm -ivh /mnt/Packages/make-3.*
rpm -ivh /mnt/Packages/libgcc-4.*x86_64*
rpm -ivh /mnt/Packages/libgcc-4.*i686*
rpm -ivh /mnt/Packages/libstdc++-4.*
rpm -ivh /mnt/Packages/libstdc++-4.*.i686*
rpm -ivh /mnt/Packages/libstdc++-devel-4.*
rpm -ivh /mnt/Packages/compat-libstdc++-33*
rpm -ivh /mnt/Packages/mpfr-2.4.1-6.el6.x86_64.rpm
rpm -ivh /mnt/Packages/ppl*86_64*
rpm -ivh /mnt/Packages/*cloog-ppl*x86_64*
rpm -ivh /mnt/Packages/cpp*86_64*
rpm -ivh /mnt/Packages/gcc-4.*x86_64*
rpm -ivh /mnt/Packages/gcc-c++-4.*x86_64*
rpm -ivh /mnt/Packages/--allfiles elfutils-libelf-0*x86_64* /mnt/Packages/elfutils-libelf-devel-0*x86_64*
rpm -ivh /mnt/Packages/elfutils-libelf-0*i686* /mnt/Packages/elfutils-libelf-devel-0*i686*
rpm -ivh /mnt/Packages/unixODBC* /mnt/Packages/ncurses*i686* /mnt/Packages/readline*i686* /mnt/Packages/libtool-ltdl*i686*
rpm -ivh /mnt/Packages/compat-libcap1*x86_64*rpm

echo "####################vi /etc/security/limits.conf
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
grid soft nproc 2047
grid hard nproc 16384
grid soft nofile 1024
grid hard nofile 65536">>/etc/security/limits.conf

####################vi /etc/pam.d/login
#session    required     pam_limits.so


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


echo "127.0.0.1       localhost.localdomain   localhost
# Public
192.168.82.36   node1.localdomain        node1
192.168.82.38   node2.localdomain        node2
# Private
192.168.55.36   node1-priv.localdomain   node1-priv
192.168.55.38   node2-priv.localdomain   node2-priv
# Virtual
192.168.82.37   node1-vip.localdomain    node1-vip
192.168.82.39   node2-vip.localdomain    node2-vip
# SCAN
192.168.82.40   node1-scan.localdomain node1-scan">>/etc/hosts


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






