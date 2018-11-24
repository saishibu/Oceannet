#!/usr/bin/python
import basestation as ns
import time

ip_bs1=192.168.179.100
ip_bs1=192.168.179.66
url_login_bs1='https://192.168.179.100/login.cgi'
url_status_bs1='https://192.168.179.100/status.cgi'
url_login_bs2='https://192.168.179.66/login.cgi'
url_status_bs2='https://192.168.179.66/status.cgi'

cj1,opener1=ns.login(url_login_bs1)
cj2,opener2=ns.login(url_login_bs2)
print 'Login Success'
a=1
while a:
	
	data1 = ns.fetchstatus(cj1,opener1,url_status_bs1,ip_bs1)
	data2 = ns.fetchstatus(cj2,opener2,url_status_bs2,ip_bs1)
	print 'Data Fetch completed'
	
	print data1
	print data2	

	a=0
