#!/usr/bin/python
import nanostation as ns
import time
import datetime
import RPi.GPIO as GPIO
date=datetime.date.today().strftime("%d_%b_%y")
ssid=ns.extssid()
boat=ssid+'_'+date
cpe_ip=ns.mapip(ssid)
print ssid,cpe_ip
data=dict()
diri=""
cj,opener=ns.login(cpe_ip)
print "login success"
ns.statusled(1)
pos=ns.fromdb()
#pos=0
while 1:
	ns.stop()
	ns.statusled(0)
	signal,rssi,noise,ccq,distance = ns.fetchstatus(cj,opener,cpe_ip)
	th=ns.thmap(distance)
	signalinv=signal*-1
	ns.rssiled(rssi)

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
	data={'dir':diri,'boat':boat,'ss':signal,'nf':noise,'rssi':rssi,'pos':pos,'ccq':ccq,'d':distance}
	print data
	ns.todb(data)
	ns.breathe(5)
GPIO.cleanup()



