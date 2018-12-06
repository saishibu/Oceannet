#!/usr/bin/python3

import iperf3
import json,time
import pymysql

conn =pymysql.connect(database="micronet",user="on",password="amma@123",host="localhost")
cur=conn.cursor()

client = iperf3.Client()
client.duration = 1
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

	print('')
	print('Test Completed')
	print('Send Megabits per second {0}'.format(result.sent_Mbps))
	print('Send Megabits per second {0}'.format(result.sent_MB_s))
	print('Received Megabits per second- BitRate {0}'.format(result.received_Mbps))
	print('Received Megabits per second {0}'.format(result.sent_MB_s))
	data= {"protocol":str(client.protocol),"sentMbps":result.sent_Mbps,"sentMB_S":result.sent_MB_s,"receivedMbps":result.received_Mbps,"receivedMB_s":result.received_MB_s,"deviceIp":client.server_hostname} 
	print('Success Fetch Status')
	print(data)
	cur.execute("INSERT INTO iperftcp(protocol,sentMbps,sentMB_S,receivedMbps,receivedMB_s,deviceIp) VALUES(%(protocol)s,%(sentMbps)s,%(sentMB_S)s,%(receivedMbps)s,%(receivedMB_s)s,%(deviceIp)s);",data)
	conn.commit()
	conn.close()

            # # TCP specific test results
            # if self.protocol == 'TCP':
            #     sent_json = self.json['end']['sum_sent']
            #     self.sent_bytes = sent_json['bytes']
            #     self.sent_bps = sent_json['bits_per_second']

            #     recv_json = self.json['end']['sum_received']
            #     self.received_bytes = recv_json['bytes']
            #     self.received_bps = recv_json['bits_per_second']

            #     # Bits are measured in 10**3 terms
            #     # Bytes are measured in 2**10 terms
            #     # kbps = Kilobits per second
            #     # Mbps = Megabits per second
            #     # kB_s = kiloBytes per second
            #     # MB_s = MegaBytes per second

            #     self.sent_kbps = self.sent_bps / 1000
            #     self.sent_Mbps = self.sent_kbps / 1000
            #     self.sent_kB_s = self.sent_bps / (8 * 1024)
            #     self.sent_MB_s = self.sent_kB_s / 1024

            #     self.received_kbps = self.received_bps / 1000
            #     self.received_Mbps = self.received_kbps / 1000
            #     self.received_kB_s = self.received_bps / (8 * 1024)
            #     self.received_MB_s = self.received_kB_s / 1024

            #     # retransmits only returned from client
            #     self.retransmits = sent_json.get('retransmits')