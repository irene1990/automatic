#!/bin/bash
ssh root@192.168.88.236 << eeooff
cd /root
ls
scp root@192.168.88.183:/home/irene/Eclipse/workspace/Dbackup/z_test/SHELL/dbackup-agent-3.2.12786-1.i686.rpm .
exit
eeooff
echo done!