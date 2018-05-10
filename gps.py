import serial,pynmea2,time,pymysql

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
conn=pymysql.connect(database="OceanNet",user="on",password="amma",host="localhost")
cur=conn.cursor()
BOAT='Sarveshwara_May10'
a=1
while a:
	rcv = port.readline()
	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		lat=msg.lat
		print lat
		lon=msg.lon
		print lon
		data={'BOAT':BOAT,'lat':lat,'long':long}
		cur.execute("INSERT INTO GPS(BOAT,LAT,LON) VALUES (%(BOAT)s,%(lat)s,%(lon)s);",data)
		conn.commit()
		print "GPS Committed"
		a=0
conn.close()
print "GPS Updated"
	
