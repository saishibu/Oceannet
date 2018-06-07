import urllib, urllib2, cookielib
import ssl,json,time
import pymysql
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
	scanoutput = check_output(["iwconfig", "wlan0"])
	for line in scanoutput.split():
		if line.startswith("ESSID"):
			ssid = line.split('"')[1]
    	return ssid
#Map SSID to CPE IP
def mapip(essid):
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT CPE FROM `boat_data` WHERE ssid='Oceannet_Test';")
	ip=cur.fetchall()
	ip=ip[0]
	ip=ip[0]
	
	return ip
#sleep function 
def breathe(t):
	t1=0
	for t1 in range(t):
		GPIO.output(26,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(26,GPIO.LOW)
#write to database
def todb(data):
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO proto1(BOAT, SS, NF, CCQ, D, RSSI, POS, DIR) VALUES(%(boat)s,%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(rssi)s,%(pos)s,%(dir)s);",data)
	conn.commit()
	conn.close()
#read last position from database
def fromdb():
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT pos FROM proto1  limit 1;")
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
	print rssi
	if rssi >= 80: #all ON
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "80+"
	if 61 <= rssi <= 79: #RSSI3 off
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.LOW) #1
		print "61to79"
	if 41 <= rssi <= 60: #RSSI3&2 off
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.LOW) #1
		print "41to60"
	if 21 <= rssi <= 40: #RSSI 3,2,1 off
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.LOW) #1
		print "21to40"
	if 0 <= rssi <= 20: #(no coverage/Very Poor)
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.HIGH) #1
		print "nil"
#Login to Nanostation
def login():
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open('https://192.168.179.118/login.cgi')
	login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
	r=opener.open('https://192.168.179.118/login.cgi',login_data)
	return cj,opener
#Fetch Status from Nanostation
def fetchstatus(cj,opener):
	status_page=opener.open('https://192.168.179.118/status.cgi')
	status=status_page.read()
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	rssi=json_status['wireless']['rssi']
	noise=json_status['wireless']['noisef']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	return signal,rssi,noise,ccq,distance
#Threshold mapping based on distance
def thmap(distance):
	if distance<=1000:
		th=50
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
