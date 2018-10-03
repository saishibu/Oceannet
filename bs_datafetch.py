#!/usr/bin/python
import basestation as ns
import time

url_login_bs1='https://192.168.179.100/login.cgi'
url_status_bs1='https://192.168.179.100/status.cgi'
url_login_bs2='https://192.168.179.66/login.cgi'
url_status_bs2='https://192.168.179.66/status.cgi'

cj1,opener1=ns.login(url_login_bs1)
cj2,opener2=ns.login(url_login_bs2)
print 'Login Success'
a=1
while a:
	
	signal1,rssi1,noise1,ccq1,distance1,devices1 = ns.fetchstatus(cj1,opener1,url_status_bs1)
	signal2,rssi2,noise2,ccq2,distance2,devices2 = ns.fetchstatus(cj2,opener2,url_status_bs2)
	print 'Data Fetch completed'
	data1={'bs_ID':'100','ss':signal1,'nf':noise1,'rssi':rssi1,'ccq':ccq1,'d':distance1,'devices':devices1}
	data2={'bs_ID':'66','ss':signal2,'nf':noise2,'rssi':rssi2,'ccq':ccq2,'d':distance2,'devices':devices2}
	#data1={'bs_ID':'100','ss':signal1,'nf':noise1,'rssi':rssi1,'ccq':ccq1,'d':distance1}
	#data2={'bs_ID':'66','ss':signal2,'nf':noise2,'rssi':rssi2,'ccq':ccq2,'d':distance2}
	print data1
	print data2	
	ns.todb(data1)
	ns.todb(data2)
	#time.sleep(300)
	a=0
