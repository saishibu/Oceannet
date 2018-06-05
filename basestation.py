import urllib, urllib2, cookielib
import ssl,json,time
import pymysql

def todb(data):
	conn =pymysql.connect(database="Oceannet",user="root",password="amma",host="localhost")
	cur=conn.cursor()
	#cur.execute("INSERT INTO basestation(bs_ID, ss, nf, ccq, d, rssi, devices) VALUES(%(bs_ID)s,%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(rssi)s),%(devices)s);",data)
	cur.execute("INSERT INTO basestation(ss,nf,ccq,d,bs,rssi,devices) VALUES(%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(bs_ID)s,%(rssi)s,%(devices)s);",data)
	conn.commit()
	conn.close()

def login(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	cj=cookielib.CookieJar()
	opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	r=opener.open(url)
	login_data=urllib.urlencode({'username':'ubnt', 'password':'1234','action':'login'})
	r=opener.open(url,login_data)
	return cj,opener
#Fetch Status from Nanostation
def fetchstatus(cj,opener,url):
	status_page=opener.open(url)
	status=status_page.read()
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	rssi=json_status['wireless']['rssi']
	noise=json_status['wireless']['noisef']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	devices=json_status['wireless']['polling']['airsync_connections']
	return signal,rssi,noise,ccq,distance,devices
