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
output=$((mysqldump -h $ip -uoceannet -pamma autosys proto1 --skip-add-drop-table > dbdump/$datalog ) 2>&1)
output2=$((mysqldump -h $ip -uoceannet -pamma autosys gps_log --skip-add-drop-table > dbdump/$gpslog ) 2>&1)
writeLog "$output"
writeLog "$output2"
echo "$timestamp	DB Extraction success" >> $logfile

## insert into own db
 echo "Inserting dump into own database"
 echo "$timestamp	Inserting into own db" >> $logfile
 output3=$((mysql -h localhost -uroot -pamma Oceannet  < dbdump/$datalog) 2>&1)
 output4=$((mysql -h localhost -uroot -pamma Oceannet  < dbdump/$gpslog) 2>&1)
 writeLog "$output3"
 writeLog "$output4"
 ## Remove old data from database
echo "Remove data from the node database"
echo "$timestamp	Remove date from remote db at $ip" >> $logfile
output5=$((mysql -h $ip -uoceannet -pamma autosys -e "DELETE FROM TABLE proto1 where ID>2") 2>&1)
output6=$((mysql -h $ip -uoceannet -pamma autosys -e "TRUNCATE TABLE gps_log where ID >2") 2>&1)
writeLog "$output5"
writeLog "$output6"
## Make a dummy value
echo "Make a dummy Value"
echo "$timestamp	Make a dummy Value at $ip" >> $logfile
output7=$((mysql -h $ip -uoceannet -pamma autosys -e "NSERT INTO proto1(BOAT, SS, NF, CCQ, D, RSSI, POS, DIR) VALUES('dummy',0,0,0,0,0,0,'0');") 2>&1)
writeLog "$output7"


