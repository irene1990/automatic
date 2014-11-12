if [ $1 = "4.0" ]; then
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@4.0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
lftp scutech:dingjia@192.168.88.10/ftp_product_installer/wddps/2014/4.0
else
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@@@3.1@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
lftp scutech:dingjia@192.168.88.10/product_release/scutech/dbackup/3.1
fi
