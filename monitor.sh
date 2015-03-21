#!/bin/sh
set j=0
echo "Count	Date			Cpu(%)	Mem(%)	Netrec	Netsend"
while true
do
        date=$(date | awk '{print $2,$3,$4,$6}')
        memery_used=$(swapinfo | awk 'NR==5' | awk '{print $3}')
        memery_all=$(swapinfo | awk 'NR==5' | awk '{print $2}')
        memery_percent=$(echo "scale=4;$memery_used / $memery_all" | bc)
        percent_part1=$(echo $memery_percent | cut -c 2-3)
        percent_part2=$(echo $memery_percent | cut -c 4-5)
        cpu_idle=$(sar -u 4 | awk 'NR==5' | awk '{print $5}')
        cpu_used=`expr 100 - $cpu_idle`
	j=$(($j+1))
	echo "$j	$date	$cpu_used	$percent_part1.$percent_part2"
	#sleep 1
done 
