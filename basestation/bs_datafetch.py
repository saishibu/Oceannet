#!/usr/bin/python
import basestation as ns
import time

ip_bs1="192.168.179.100"
ip_bs2="192.168.179.66"

url_login_bs1='https://192.168.179.100/login.cgi'
url_status_bs1='https://192.168.179.100/status.cgi'

url_login_bs2='https://192.168.179.66/login.cgi'
url_status_bs2='https://192.168.179.66/status.cgi'

url_client_bs1='https://192.168.179.100/sta.cgi'
url_client_bs2='https://192.168.179.66/sta.cgi'


cj1,opener1=ns.login(url_login_bs1)
cj2,opener2=ns.login(url_login_bs2)
print ('Login Success')
data1 = ns.fetchstatus(cj1,opener1,url_status_bs1,ip_bs1)
data2 = ns.fetchstatus(cj2,opener2,url_status_bs2,ip_bs2)
client1= ns.clientlist(cj1,opener1,url_status_bs1,ip_bs1)
client2= ns.clientlist(cj2,opener2,url_status_bs2,ip_bs2)


print ('Data Fetch completed')
#print (data1)
#print (data2)

#print (client1)
#print (client2)
