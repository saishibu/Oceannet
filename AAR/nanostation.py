# Import necessary libraries/modules
import urllib, urllib2, cookielib  # For HTTP requests and cookies
import ssl  # For SSL/TLS support
import json  # For JSON parsing
import time  # For time-related operations
import pymysql  # For MySQL database connection
from subprocess import check_output  # For running shell commands
import RPi.GPIO as GPIO  # For Raspberry Pi GPIO control

# Configure GPIO pins for various purposes
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT)  #REV
GPIO.setup(27,GPIO.OUT)  #FWD
GPIO.setup(26,GPIO.OUT)  #Status LED
GPIO.setup(19,GPIO.OUT) #RSSI 0
GPIO.setup(13,GPIO.OUT)	#RSSI 1
GPIO.setup(6,GPIO.OUT)  #RSSI 2
GPIO.setup(5,GPIO.OUT)  #RSSI 3

# Function to get configuration data from a MySQL database
# The getConfig function connects to a MySQL database and retrieves configuration settings such as IP, log, and piggyback settings. This function is used to get system configuration data.
def getConfig():
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT ip,log,piggyback FROM config;")
	try:
		data=cur.fetchone()
# 		print(data)
		ip=data[0]
		log=data[1]
		piggyback=data[2]
	except:
		print("System not configured")
		print("Run Configuration first")
		exit()
	return(ip,log,piggyback)


# Function to get boat-related data from a MySQL database
# The getBoatData function connects to a MySQL database and retrieves boat-related data, including the boat's name and CPE IP address.
def getBoatData():
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("SELECT ssid,CPE FROM boat_data;")
	try:
		data=cur.fetchone()
# 		print(data)
		boatName=data[0]
		cpeIP=data[1]
	except:
		print("System not configured")
		print("Run Configuration first")
		exit()
	return(boatName,cpeIP)

# Function to extract the SSID of the connected wireless network
# The extssid function uses the Linux native iwconfig command to extract the SSID of the wireless network to which the Raspberry Pi is connected. It returns the SSID as a string.
def extssid():
	ssid = "No connection"
	scanoutput = check_output(["iwconfig", "wlan0"],shell=0)
	for line in scanoutput.split():
		if line.startswith("ESSID"):
			ssid = line.split('"')[1]
		
	return ssid


# Function to map an SSID to a CPE IP address in a MySQL database
# The mapip function maps an SSID to its corresponding CPE IP address by querying a MySQL database. It returns the boat's ID and CPE IP address.
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

# Function to simulate a breathing effect (Blinking) on status LED
# The breathe function controls an LED to simulate a breathing effect. It takes two parameters: t (time duration for the effect) and hide (a sleep time).
def breathe(t,hide):
	t1=0
	for t1 in range(t):
		GPIO.output(26,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(26,GPIO.LOW)
		time.sleep(0.5)
	time.sleep(hide)

# Function to write data to a MySQL database
# The todb function inserts data from a dictionary into a specified database table. It establishes a database connection, inserts the data, and then closes the connection.
def todb(data):
	conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO proto1(TIMESTAMP,BOAT, SS, NF, CCQ, D, RSSI, POS, DIR,frequency,channel,txrate,rxrate,bsip,ping) VALUES(%(TIME)s,%(boat)s,%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(rssi)s,%(pos)s,%(dir)s,%(freq)s,%(channel)s,%(txrate)s,%(rxrate)s,%(bs_ip)s,%(ping_ms)s);",data)
	conn.commit()
	conn.close()

# Function to read the last position from a MySQL database
# The fromdb function retrieves the last position value from a specified database table. It establishes a database connection, retrieves the value, and then closes the connection.
def fromdb():
	try:
		conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
		cur=conn.cursor()
		cur.execute("SELECT pos FROM proto1  ORDER BY id DESC LIMIT 1;")
		pos=cur.fetchall()
		pos=pos[0]
		pos=pos[0]
	except:
		pos=0
	return pos

# Function to control the status LED
# The statusled function controls the status LED based on a given condition (1 to turn it on, 0 to turn it off).
def statusled(cond):
	if cond == 1:
		GPIO.output(26,GPIO.HIGH) #status led on
	if cond == 0:
		GPIO.output(26,GPIO.LOW) #status led on

# Function to control RSSI LEDs based on RSSI values
# The rssiled function controls the RSSI LEDs based on the received RSSI (Received Signal Strength Indicator) value. It illuminates specific LEDs to indicate signal strength.
def rssiled(rssi):
	#1-> GREEN 2-> YELLOW 3->YELLOW 4->RED
	#print rssi
	if rssi >= 80: #all ON
		GPIO.output(5,GPIO.HIGH) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		# print "Signal Strength: Very Good" + str(rssi)
	if 61 <= rssi <= 79: #RSSI3 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.HIGH) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		# print "Signal Strength: Good " +str(rssi)
	if 41 <= rssi <= 60: #RSSI3&2 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.HIGH) #2
		GPIO.output(19,GPIO.HIGH) #1
		# print "Signal Strength: Medium " +str(rssi)
	if 21 <= rssi <= 40: #RSSI 3,2,1 off
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.HIGH) #1
		# print "Signal Strength: Poor "
	if 0 <= rssi <= 20: #(no coverage/Very Poor)
		GPIO.output(5,GPIO.LOW) #4
		GPIO.output(6,GPIO.LOW) #3
		GPIO.output(13,GPIO.LOW) #2
		GPIO.output(19,GPIO.LOW) #1
		# print "No Signal " + str(rssi)

# Function to log in to a NanoStation device using HTTP requests
# The login function logs in to a NanoStation device using HTTP requests. It takes the device's IP address and returns a cookie jar and opener for authenticated requests.
def login(ip):
	url='https://'+ip+'/login.cgi'
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open(url)
	login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
	r=opener.open(url,login_data)
	return cj,opener

# Function to fetch status information from a NanoStation device
# The fetchstatus function fetches various status information from a NanoStation device using authenticated requests. It returns signal strength, RSSI, noise, CCQ, distance, txrate, rxrate, frequency, and channel.
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

# Function to fetch IP address and ping status from a NanoStation device
# The fetchip function fetches the IP address of the Base Station (BS) and ping latency from a NanoStation device using authenticated requests.
def fetchip(cj,opener,ip):
	url='https://'+ip+'/sta.cgi'
	sta_page=opener.open(url)
	sta=sta_page.read()
	json_sta=json.loads(sta)
	bs_ip=json_sta[0]['lastip']
	ping_ms=json_sta[0]['tx_latency']
	return bs_ip,ping_ms


# Function to map thresholds based on distance
# The thmap function maps thresholds based on distance. It takes a distance value and returns specific thresholds and a hide time.
def thmap(distance):
	if distance<=1000:
		th=60
		hide= 30 
	if 1001<distance<=10000:
		th=68
		hide=120
	if 10001<distance<=15000:
		th=75
		hide=240
	if 15001<distance<=30000:
		th=85
		hide=900
	if 30001<distance<=45000:
		th=95
		hide=1800
	return th,hide

# Functions to control AAR motor direction (forward, reverse, stop)
# The fwd function is used to control the forward direction using GPIO pins.

def fwd():
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)

#The rev function is used to control the reverse direction using GPIO pins.
def rev():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
# The stop function is used to stop movement by turning off GPIO pins.
def stop():
	GPIO.output(27,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
