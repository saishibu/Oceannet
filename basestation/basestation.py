import urllib, urllib2, cookielib
import ssl,json,time
import pymysql

def todb(data):
	conn =pymysql.connect(database="micronet",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	#cur.execute("INSERT INTO basestation(bs_ID, ss, nf, ccq, d, rssi, devices) VALUES(%(bs_ID)s,%(ss)s,%(nf)s,%(ccq)s,%(d)s,%(rssi)s),%(devices)s);",data)
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
	return cj,opener
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
	
	data= {"rcvdsgnl":rcvdsgnl,"ccq":ccq,"distance":distance,"capacity":capacity,"frequency":frequency,"channel":channel,"noisefloor":noisefloor,"quality":quality,"txrate":txrate,"rxrate":rxrate,"devices":devices,"deviceIp":deviceIp} 
	todb(data)
	return data


def clientlist(cj,opener,url,ip_bs):
	clientlist=opener.open(url)
	client=clientlist.read()
	json_status=json.loads(client)
	return json_status[]
	
