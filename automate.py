#!/usr/bin/python
import nanostation as ns
import time
import RPi.GPIO as GPIO
boat='test_setup'
data=dict()
diri=""
cj,opener=ns.login()
print "login success"
ns.statusled(1)
pos=ns.fromdb()
#pos=0
while 1:
	ns.stop()
	ns.statusled(0)
	signal,rssi,noise,ccq,distance = ns.fetchstatus(cj,opener)
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
	data={'dir':diri,'boat':boat,'ss':signal,'nf':noise,'rssi':rssi,'pos':pos,'ccq':ccq,'d':distance}
	print data
	ns.todb(data)
	ns.breathe(5)



