#!/bin/bash

writeLog()
{
 if [ ! -z "$1" ]
 then
  echo $1
  echo $1 >> $logfile
 fi
}

if [ "$1" == "" ]
then
 echo "Usage: ./fetchDataFromNode <ip-address>"
 echo "Example: ./fetchDataFromNode 192.168.21.226"
 exit
fi


cd /opt/smg2/

ip=$1
logfile=log/dump.log
date=$(date)

#check for valid ip
if ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]
then
 echo "Invalid ip address"
 echo "Usage: ./fetchDataFromNode <ip-address>"
 echo "Example: ./fetchDataFromNode 192.168.21.226"
 exit
fi 

echo "-----------------------------" >> $logfile

 echo "Making dump of DoubleEvents table at $ip"
 timestamp=$(($(date +%s%N)/1000000))
 date=$(date)
 echo "Timestamp now: $timestamp"
 dateiname=dump_${ip}.sql
 echo "Filename: $dateiname"
## sql dump
 echo "$date	Creating dump of $ip - dump filename: $dateiname" >> $logfile
 output=$((mysqldump -h $ip -u smg2 -psmg2 smg2 DoubleEvents > dump/$dateiname) 2>&1)
##--where="timestamp<$timestamp"
 writeLog "$output"

## insert into own db
 echo "Inserting dump into own database"
 echo "$date	Inserting into own db" >> $logfile
 output2=$((mysql -u smg2 -psmg2 smg2 < dump/$dateiname) 2>&1)
 writeLog "$output2"

## remove data from remote db
 echo "Remove data from the node database"
 echo "$date	Remove date from remote db at $ip" >> $logfile
 output3=$((mysql -h $ip -u smg2 -psmg2 smg2 -e "DELETE FROM DoubleEvents where timestamp<$timestamp") 2>&1)
 writeLog "$output3"

