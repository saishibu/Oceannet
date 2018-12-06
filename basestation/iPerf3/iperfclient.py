#!/usr/bin/python3

import iperf3
import json


client = iperf3.Client()
client.duration = 2
client.server_hostname = '127.0.0.1'
client.port = 5001
client.protocol = 'tcp'
client.blksize = 2000
client.num_streams = 10
client.reverse = True

print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
	print(result.error)
else:
	
	//data= {"protocol":str(client.protocol),"txBytes":result.bytes,"jitter":result.jitter_ms,"avgCpuLoad":result.local_cpu_total,"MB_s":result.MB_s,"mbps":result.Mbps,"deviceIp":client.server_hostname} 
	print('Success Fetch Status')
	print(data)
	
