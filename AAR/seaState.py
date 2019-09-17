#!/usr/bin/python
import FaBo9Axis_MPU9250
import time
import sys,math,pymysql,datetime

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
cur=conn.cursor()

from time import mktime
t =datetime.datetime.now()
unix_secs = mktime(t.timetuple())


try:
    while True:
        accel = mpu9250.readAccel()
        #print(" ax = " , ( accel['x'] ))
        #print(" ay = " , ( accel['y'] ))
        #print(" az = " , ( accel['z'] ))

        gyro = mpu9250.readGyro()
        #print(" gx = " , ( gyro['x'] ))
        #print(" gy = " , ( gyro['y'] ))
        #print(" gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        #print(" mx = " , ( mag['x'] ))
        #print(" my = " , ( mag['y'] ))
        #print(" mz = " , ( mag['z'] ))
        #print("\n")
	magAngle=math.atan2(mag['y'],mag['x'])
	#print(magAngle)
	if (magAngle < 0):
		magAngle += 2*22/7
	elif (magAngle >2*22/7):
		magAngle-=2*22/7
	magAngle=magAngle*180/22*7
	#print(magAngle)
	if (magAngle >=0 and magAngle <=22):
		dir="N"
	if(magAngle >=23 and magAngle <=68):
		dir='NE'
	if(magAngle >=69 and magAngle <=112):
                dir='E'
	if(magAngle >=113 and magAngle <=156):
                dir='SE'
	if(magAngle >=157 and magAngle <=202):
                dir='S'
	if(magAngle >=203 and magAngle <=245):
                dir='SW'
	if(magAngle >=246 and magAngle <=291):
                dir='W'
	if(magAngle >=292 and magAngle <=337):
                dir='NW'
	if(magAngle >=338 and magAngle <=360):
                dir='N'
	#print(dir)
	data={'time':unix_secs,'magAngle':magAngle,'Ax':accel['x'],'Ay':accel['y'],'Az':accel['z'],'Gx':gyro['x'],'Gy':gyro['y'],'Gz':gyro['z'],'Mx':mag['x'],'My':mag['y'],'Mz':mag['z'],"Dir":dir}
	print(data)
	cur.execute("INSERT INTO seastate (timestamp,Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz, Dir, magAngle) VALUES (%(time)s,%(Ax)s, %(Ay)s, %(Az)s, %(Gx)s, %(Gy)s, %(Gz)s, %(Mx)s, %(My)s, %(Mz)s, %(Dir)s, %(magAngle)s);",data)
	conn.commit()
	time.sleep(0.1)	
	print("committed")
except KeyboardInterrupt:
	conn.close()
	sys.exit()
