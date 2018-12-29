#!/usr/bin/python3

import iperf3
import json
import pymysql

conn =pymysql.connect(database="micronet",user="on",password="amma",host="localhost")
cur=conn.cursor()


client = iperf3.Client()
client.duration = 2
client.server_hostname = '192.168.179.80'
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

 	data1 = {"protocol":str(client.protocol),"txBytes":result.sent_Mbps,"MB_s":result.received_Mbps,"mbps":result.received_MB_s,"deviceIp":client.server_hostname} 
	print('Success Fetch Status')
	print(data1)
	cur.execute("INSERT INTO iperf(protocol,txBytes,MB_s,mbps,deviceIp) VALUES(%(protocol)s,%(txBytes)s,%(MB_s)s,%(mbps)s,%(deviceIp)s);",data1)
	conn.commit()
	conn.close()

