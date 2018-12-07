#!/usr/bin/python3

import iperf3
import json
import pymysql

conn =pymysql.connect(database="micronet",user="on",password="amma@123",host="localhost")
cur=conn.cursor()


client = iperf3.Client()
client.duration = 2
client.server_hostname = '127.0.0.1'
client.port = 5002
client.protocol = 'udp'
client.blksize = 2000
client.num_streams = 10
client.reverse = True

print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
   print(result.error)
else:

 	data = {"protocol":str(client.protocol),"txBytes":result.bytes,"jitter":result.jitter_ms,"avgCpuLoad":result.local_cpu_total,"MB_s":result.MB_s,"mbps":result.Mbps,"deviceIp":client.server_hostname,"packets":result.packets,"lostPackets":result.lost_packets,"lostPercent":result.lost_percent,"seconds":result.seconds} 
 	#print('')
 	#print('Test completed:')
 	#print('lostPercent {0}'.format(result.lost_percent))
 	print('Success Fetch Status')
 	print(data)
 	cur.execute("INSERT INTO iperfudp(protocol,txBytes,jitter,avgCpuLoad,MB_s,mbps,deviceIp,packets,lostPackets,lostPercent,seconds) VALUES(%(protocol)s,%(txBytes)s,%(jitter)s,%(avgCpuLoad)s,%(MB_s)s,%(mbps)s,%(deviceIp)s,%(packets)s,%(lostPackets)s,%(lostPercent)s,%(seconds)s);",data)
 	conn.commit()
 	conn.close()

