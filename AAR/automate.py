#!/usr/bin/python
import nanostation as ns
import time
import datetime
import RPi.GPIO as GPIO
import piggyback as pb
date=datetime.date.today().strftime("%d_%b_%y")

from time import mktime
t =datetime.datetime.now()
unix_secs = mktime(t.timetuple())

boat,cpe_ip=ns.getBoatData()

data=dict()
diri=""
#cpe_ip="192.168.179.123"

cj,opener=ns.login(cpe_ip)
print "Connection Successful\n Boat Name: " + str (boat)+ "\n" + "IP Address: "+str(cpe_ip)
print "login success"
ns.statusled(1)
pos=ns.fromdb()
#pos=0
while 1:
	ns.stop()
	ns.statusled(0)
	signal,rssi,noise,ccq,distance,txrate,rxrate,freq,channel = ns.fetchstatus(cj,opener,cpe_ip)
	try:
		bs_ip,ping_ms=ns.fetchip(cj,opener,cpe_ip)
	except:
		bs_ip="0.0.0.0"
		ping_ms=0
	th=ns.thmap(distance)
	signalinv=signal*-1
	ns.rssiled(signalinv)

	#automation:
	if signalinv > th:
		ns.fwd()
		diri='fwd'
		pos=pos+1
		if pos >36:
			ns.rev()
			pos=pos+1
			diri='rev'
		if pos >72:
			pos=0
	#Data storage
	data={'ping_ms':ping_ms,'TIME':unix_secs,'dir':diri,'boat':1,'ss':signal,'nf':noise,'rssi':rssi,'pos':pos,'ccq':ccq,'d':distance,'txrate':txrate,'rxrate':rxrate,'freq':freq,'channel':channel,'bs_ip':bs_ip}
	print data
	pb.helper(data)
	ns.todb(data)
	ns.breathe(5)
GPIO.cleanup()



