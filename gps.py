import serial,pynmea2,time,pymysql

port = serial.Serial("/dev/ttyUSB0", baudrate=9600)
conn=pymysql.connect(database="OceanNet",user="on",password="amma",host="localhost")
cur=conn.cursor()
a=1
while a:
	rcv = port.readline()
	print rcv[0:6]
	if rcv[0:6] == '$GPGGA':
		msg=pynmea2.parse(rcv)
		lat=msg.lat
		print lat
		long=msg.lon
		print long
		data={'lat':lat,'long':long}
		cur.execute("INSERT INTO GPS(Lat,Longi) VALUES (%(lat)s,%(long)s);",data)
		conn.commit()
		print "GPS Committed"
		a=0
conn.close()
print "GPS Updated"
	
