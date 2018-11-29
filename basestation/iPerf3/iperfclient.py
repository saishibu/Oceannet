#!/usr/bin/python3

import iperf3
import json,time
import pymysql

conn =pymysql.connect(database="micronet",user="on",password="amma",host="localhost")
cur=conn.cursor()

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
	data= {"protocol":client.protocol.decode(),"txBytes":result.bytes,"jitter":result.jitter_ms,"avgCpuLoad":result.local_cpu_total,"MB_s":result.MB_ps,"mbps":result.Mbps,"deviceIp":client.server_hostname} 
	cur.execute("INSERT INTO bsparam(protocol,txBytes,jitter,avgCpuLoad,MB_s,mbps,deviceIp) VALUES(%(protocol)s,%(txBytes)s,%(jitter)s,%(avgCpuLoad)s,%(MB_s)s,%(mbps)s,%(deviceIp)s);",data)
	conn.commit()
	conn.close()

print('Success Fetch Status')
print(data)
