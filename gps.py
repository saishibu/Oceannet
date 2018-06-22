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
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		print msg
		lat=msg.lat
		lat=pynmea2.dm_to_sd(lat)
		#print lat
		lon=msg.lon
		lon=pynmea2.dm_to_sd(lon)
		#print lon
		data={'BOAT':boat,'lat':lat,'lon':lon}
		print data
		cur.execute("INSERT INTO gps_log(BOAT,LAT,LON) VALUES (%(BOAT)s,%(lat)s,%(lon)s);",data)
		conn.commit()
		print "GPS Committed"
	
	if rcv[0:6] == '$GPRMC':
		msg=pynmea2.parse(rcv)
		print msg
		speed=msg.spd_over_grnd_kmph
		print speed
		
		a=0
conn.close()
print "GPS Updated"
#except IndexError:
        # print("To catch an error...")
 #       continue
#except KeyboardInterrupt:
 #       print("\nProgram stopped.")
  #      exit()
	
