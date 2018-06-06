#!/bin/bash

cd /home/saishibu/Oceannet

ip=$1
timestamp=$(date +%d%b%Y\ %T)
echo "$ip"
echo "$timestamp"

logfile=$ip_dbdump.log
echo "-----------------------------" >> $logfile
echo "Making dump of oceannet table at $ip"
echo "$timestamp	Creating dump of $ip - dump filename: $ip" >> $logfile
output=$((mysqldump -h $ip -u on -pamma autosys proto1 > ${timestamp}_data_${ip}.sql) 2>&1)
output2=$((mysqldump -h $ip -u on -pamma autosys gps_log > ${timestamp}_gps_${ip}.sql) 2>&1)

echo "Remove data from the node database"
echo "$timestamp	Remove date from remote db at $ip" >> $logfile


