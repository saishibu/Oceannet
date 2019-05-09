import urllib, urllib2, cookielib
import ssl,json,time
import pymysql
import subprocess
from subprocess import check_output
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT)  #REV
GPIO.setup(27,GPIO.OUT)  #FWD
GPIO.setup(26,GPIO.OUT)  #Status LED
GPIO.setup(19,GPIO.OUT) #RSSI 0
GPIO.setup(13,GPIO.OUT)	#RSSI 1
GPIO.setup(6,GPIO.OUT)  #RSSI 2
GPIO.setup(5,GPIO.OUT)  #RSSI 3

#Extract SSID
def extssid():
	scanoutput = check_output(["iwconfig", "wlan0"],shell=0)
	for line in scanoutput.split():
		if line.startswith("ESSID"):
			ssid = line.split('"')[1]
    	return ssid
#Map SSID to CPE IP
def mapip(essid):
	#print type(essid)
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT ID,ssid,CPE FROM boat_data;")
	data=cur.fetchall()
	ID=0
	ip="127.0.0.1"
	for row in data:
		if row[1]==essid:
			ID=row[0]
			ip=row[2]
		#else:
			#ID=0
			#ip="Invalid SSID"
	return ID,ip
#sleep function 
def breathe(t):
	t1=0
	for t1 in range(t):
		GPIO.output(26,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(26,GPIO.LOW)
		time.sleep(0.5)
#write to database
def todb(data):
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO proto1(TIMESTAMP,BOAT, SS, NF, CCQ, D, RSSI, POS, DIR,frequency,channel,txrate,rxrate) VALUES(%(TIME)s,%(boat)s,%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(rssi)s,%(pos)s,%(dir)s,%(freq)s,%(channel)s,%(txrate)s,%(rxrate)s);",data)
	conn.commit()
	conn.close()
#read last position from database
def fromdb():
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT pos FROM proto1  ORDER BY id DESC LIMIT 1;")
	pos=cur.fetchall()
	pos=pos[0]
	pos=pos[0]
	return pos
#Status LED Config
def statusled(cond):
	if cond == 1:
		GPIO.output(26,GPIO.HIGH) #status led on
	if cond == 0:
		GPIO.output(26,GPIO.LOW) #status led on
#RSSI LED Config
def rssiled(rssi):
	#1-> GREEN 2-> YELLOW 3->YELLOW 4->RED
	#print rssi
	if rssi >= 80: #all ON
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "Signal Strength: Very Good" + str(rssi)
	if 61 <= rssi <= 79: #RSSI3 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "Signal Strength: Good " +str(rssi)
	if 41 <= rssi <= 60: #RSSI3&2 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "Signal Strength: Medium " +str(rssi)
	if 21 <= rssi <= 40: #RSSI 3,2,1 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "Signal Strength: Poor "
	if 0 <= rssi <= 20: #(no coverage/Very Poor)
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "No Signal " + str(rssi)
#Login to Nanostation
def login(ip):
	url='https://'+ip+'/login.cgi'
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open(url)
	login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
	r=opener.open(url,login_data)
	return cj,opener
#Fetch Status from Nanostation
def fetchstatus(cj,opener,ip):
	url='https://'+ip+'/status.cgi'
	status_page=opener.open(url)
	status=status_page.read()
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	rssi=json_status['wireless']['rssi']
	noise=json_status['wireless']['noisef']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	txrate=json_status['wireless']['txrate']
	rxrate=json_status['wireless']['rxrate']
	freq=json_status['wireless']['frequency']
	channel=json_status['wireless']['channel']
	
	return signal,rssi,noise,ccq,distance,txrate,rxrate,freq,channel
def fetchip(cj,opener,ip):
	url='https://'+ip+'/sta.cgi'
	sta_page=opener.open(url)
	sta=status_page.read()
	json_sta=json.loads(sta)
	bs_ip=json_status[0]['lastip']
	ping_ms=json_status['0']['tx_latency']
	return bs_ip,ping_ms


#Threshold mapping based on distance
def thmap(distance):
	if distance<=1000:
		th=60
	if 1001<distance<=15000:
		th=75
	if 15001<distance<=30000:
		th=85
	if 30001<distance<=45000:
		th=95
	return th
#Direction control for Channel Master
def fwd():
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)
def rev():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
def stop():
	GPIO.output(27,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)

#TBD: For inhouse developed rotator
#def fwd_step():
#def rev_step():
#def stop_step():
