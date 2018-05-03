import nanostation as ns
import time
import RPi.GPIO as GPIO
from dbwrite import todb
import dbwrite as db
mode='test_office'
data=dict()
cj,opener=ns.login()
pos=db.fromdb()
while 1:
	ns.stop()
	statusled(1)
	signal,rssi,noise,ccq,distance = ns.fetchstatus(cj,opener)
	ns.rssiled(rssi)
	th=ns.thmap(distance)
	signalinv=signal*-1
	if signalinv > th:
		ns.fwd()
		dir='fwd'
		pos=pos+1
		if pos >36:
			ns.rev()
			pos=pos+1
			dir='rev'
		if pos >72:
			pos=0
	data={'lat':0,'lon':0,'dir':dir,'mode':mode,'ss':signal,'nf':noise,'rssi':rssi'pos':pos,'ccq':ccq,'d':distance}
	db.todb(data)



