#!/usr/bin/env python3

import iperf3
import urllib, urllib2, cookielib
import ssl,json,time
import pymysql

def todb(data):
	conn =pymysql.connect(database="micronet",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO bsparam(rcvdsgnl,ccq,distance,frequency,channel,noisefloor,txrate,rxrate,quality,capacity,deviceIp,devices) VALUES(%(rcvdsgnl)s,%(ccq)s,%(distance)s,%(frequency)s,%(channel)s,%(noisefloor)s,%(txrate)s,%(rxrate)s,%(quality)s,%(capacity)s,%(deviceIp)s,%(devices)s);",data)
	conn.commit()
	conn.close()

def login(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open(url)
	login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
	r=opener.open(url,login_data)
	return cj,openers

client = iperf3.Client()
client.duration = 1
client.server_hostname = '127.0.0.1'
client.port = 5001
client.protocol = 'udp'
client.blksize = 2000
client.num_streams = 10
client.reverse = True

print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
    print(result.error)
else:
    print('')
    print('Test completed:')
    print('  started at         {0}'.format(result.time))
    print('  bytes transmitted  {0}'.format(result.bytes))
    print('  jitter (ms)        {0}'.format(result.jitter_ms))
    print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

    print('Average transmitted data in all sorts of networky formats:')
    print('  bits per second      (bps)   {0}'.format(result.bps))
    print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
    print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
    print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
    print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
#Fetch Status from Nanostation
def fetchstatus(cj,opener,url,ip_bs):
	status_page=opener.open(url)
	status=status_page.read()
	json_status=json.loads(status)
	
	rcvdsgnl=json_status['wireless']['signal']
	#rssi=json_status['wireless']['rssi']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	frequency=json_status['wireless']['frequency'].replace("MHz","")
	channel=json_status['wireless']['channel']
	noisefloor=json_status['wireless']['noisef']
	quality=json_status['wireless']['polling']['quality']
	capacity=json_status['wireless']['polling']['capacity']
	txrate=json_status['wireless']['txrate']
	rxrate=json_status['wireless']['rxrate']
	devices=json_status['wireless']['count']
	deviceIp=ip_bs

	data= {"timestamp":time,"Bytes Transmitted":bytes,"Jitter(ms)":jitter_ms,"Avg CPU Load":local_cpu_total,"Megabits per second  (Mbps)  (kbps)":kbps,"KiloBytes per second (kB/s)":MB_s,"deviceIp":deviceIp} 
	todb(data)
	return data   
print('Success Fetch Status')
