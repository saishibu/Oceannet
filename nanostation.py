import urllib, urllib2, cookielib
import ssl,json

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT)  #REV
GPIO.setup(27,GPIO.OUT)  #FWD
GPIO.setup(26,GPIO.OUT)  #Status LED
GPIO.setup(19,GPIO.OUT) #RSSI 0
GPIO.setup(13,GPIO.OUT)	#RSSI 1
GPIO.setup(6,GPIO.OUT)  #RSSI 2
GPIO.setup(5,GPIO.OUT)  #RSSI 3
#Status LED Config
def statusled(cond):
	if cond == 1:
		GPIO.output(26,GPIO.HIGH) #status led on
	if cond == 0
		GPIO.output(26,GPIO.LOW) #status led on
#RSSI LED Config
def rssiled(rssi):
	#RSSI
	if rssi >= 90: #all ON
		GPIO.output(19,GPIO.HIGH) #RSSI 0
		GPIO.output(13,GPIO.HIGH) #RSSI 1
		GPIO.output(6,GPIO.HIGH)  #RSSI 2
		GPIO.output(5,GPIO.HIGH)  #RSSI 3
	if 75 <= rssi <= 89: #RSSI3 off
		GPIO.output(19,GPIO.HIGH) #RSSI 0
		GPIO.output(13,GPIO.HIGH) #RSSI 1
		GPIO.output(6,GPIO.HIGH)  #RSSI 2
		GPIO.output(5,GPIO.LOW)   #RSSI 3
	if 51 <= rssi <= 74: #RSSI3&2 off
		GPIO.output(19,GPIO.HIGH) #RSSI 0
		GPIO.output(13,GPIO.HIGH) #RSSI 1
		GPIO.output(6,GPIO.LOW)   #RSSI 2
		GPIO.output(5,GPIO.LOW)   #RSSI 3
	if 26 <= rssi <= 50: #RSSI 3,2,1 off
		GPIO.output(19,GPIO.HIGH) #RSSI 0
		GPIO.output(13,GPIO.LOW) #RSSI 1
		GPIO.output(6,GPIO.LOW)   #RSSI 2
		GPIO.output(5,GPIO.LOW)   #RSSI 3
	if 0 <= rssi <= 25: #all off (no coverage)
		GPIO.output(19,GPIO.HIGH) #RSSI 0
		GPIO.output(13,GPIO.HIGH) #RSSI 1
		GPIO.output(6,GPIO.LOW)   #RSSI 2
		GPIO.output(5,GPIO.LOW)   #RSSI 3
#Login to Nanostation
def login(ip,login,username,password):
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open('https://192.168.179.107/login.cgi')
	login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
	r=opener.open('https://192.168.179.107/login.cgi',login_data)
	return cj,opener
#Fetch Status from Nanostation
def fetchstatus(cj,opener):
	status_page=opener.open('https://192.168.179.107/status.cgi')
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
		th=65
		return th
	if distance<=15000:
		th=75
		return th
	if distance<=30000:
		th=85
		return th
	if distance<=45000:
		th=95
		return th
#Direction control for Channel Master
def fwd_ch():
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)
def rev_ch():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
def stop_ch():
	GPIO.output(27,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)

#TBD: For inhouse developed rotator
def fwd_step():
def rev_step():
def stop_step():
