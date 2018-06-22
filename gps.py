#!/usr/bin/python

import serial,pynmea2,time,pymysql,datetime
import nanostation as ns
import subprocess,os
port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
conn=pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
cur=conn.cursor()
date=datetime.date.today().strftime("%d_%b_%y")
ssid=ns.extssid()
boat=ssid+'_'+date
a=1
while a:
	rcv = port.readline()
	#print rcv[0:6]
	#if rcv[0:6] == '$GPGGA':
	if rcv[0:6] == '$GPRMC':
		msg=pynmea2.parse(rcv)
		print msg
		lat=msg.lat
		lat=pynmea2.dm_to_sd(lat)
		#print lat
		lon=msg.lon
		lon=pynmea2.dm_to_sd(lon)
		#print lon
		#speed=msg.speed_kn
		#print speed
		data={'BOAT':boat,'lat':lat,'lon':lon}
		print data
		cur.execute("INSERT INTO gps_log(BOAT,LAT,LON) VALUES (%(BOAT)s,%(lat)s,%(lon)s);",data)
		conn.commit()
		print "GPS Committed"
		a=0
conn.close()
print "GPS Updated"
	
