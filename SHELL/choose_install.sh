echo "DBackup_Server|DBackup_Agent|DBackup_Fsync|DBackup_Standby|DBackup_Rdiff|DBackup_Replicator|Exit"
while true;do
read -p "What are you want to install ? "
echo  $REPLY
if [[ $REPLY == 'server' ]]; then
echo 'server'
elif [[ $REPLY == 'agent'  ]]; then
echo 'agent'
elif [[ $REPLY == 'fsync'  ]]; then
echo 'fsync'
elif [[ $REPLY == 'standby'  ]]; then
echo 'standby'
elif [[ $REPLY == 'rdiff'  ]]; then
echo 'rdiff'
elif [[ $REPLY == 'replicator'  ]]; then
echo 'replicator'
elif [[ $REPLY == 'exit'  ]]; then
break
fi
done
