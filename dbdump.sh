#!/bin/bash

writeLog()
{
 if [ ! -z "$1" ]
 then
  echo $1
  echo $1 >> $logfile
 fi
}

cd /home/saishibu/Oceannet

ip=$1
timestamp=$(date +%d%b%Y\ %T)
echo "$ip"
echo "$timestamp"
dateiname1=dump1_${ip}.sql
dateiname2=dump2_${ip}.sql
datalog=data_${ip}.sql
gpslog=gps_${ip}.sql

logfile=log/dump.log
echo "-----------------------------" >> $logfile
echo "Making dump of data table at $ip"
echo "$timestamp	Creating dump of data from $ip - dump filename: datalog" >> $logfile
echo "Making dump of GPS table at $ip"
echo "$timestamp	Creating dump of GPS from $ip - dump filename: gpslog" >> $logfile
output=$((mysqldump -h $ip -uoceannet -pamma autosys proto1 > dbdump/$datalog ) 2>&1)
output2=$((mysqldump -h $ip -u oceannet -pamma autosys gps_log > dbdump/$gpslog ) 2>&1)
writeLog "$output"
writeLog "$output2"
echo "$timestamp	DB Extraction success" >> $logfile

echo "Remove data from the node database"
echo "$timestamp	Remove date from remote db at $ip" >> $logfile
output3=$((mysql -h $ip -uoceannet -pamma autosys -e "DELETE FROM proto1") 2>&1)
output4=$((mysql -h $ip -uoceannet -pamma autosys -e "DELETE FROM gps_log") 2>&1)
writeLog "$output3"
writeLog "$output4"


