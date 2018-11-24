#!/usr/bin/python           # This is server.py file

import iperf3
from time import sleep, strftime, time   #log the date and time while getting the CPU iperf3
with open("/home/dhaneshraj/python/iperf3_RUN/temp.csv", "a") as log: #creates a new file called cpu_temp.csv and opens it with the name log.
		client = iperf3.Client()
		client.duration = 5
		client.server_hostname = '127.0.0.1' #Change the IP address of the Boat Device
		client.port = 5001
		client.blksize =  1234
		client.reverse =  True
		client.num_streams = 1
		client.protocol = 'udp'
		print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
		result = client.run()
		#print(type(result.decode()))
		#print(result.sent_Mbps)
		print (result.time)
		print(result.Mbps)
		# client.json_output = False
		# if result.error:
			# print(result.error)
		# else:
			# print('')
			# print('Test completed:')
			# with open("/home/dhaneshraj/python/iperf3_RUN/temp.csv", "a") as log:
				# while True:
					# time1 = result.time
					# byte_tx = result.bytes.decode()
					# log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(time),str(bytes)))
					# sleep(1)	
					
					# print('  started at         {0}'.format(result.time))
					# print('  bytes transmitted  {0}'.format(result.bytes))
					# print('  jitter (ms)        {0}'.format(result.jitter_ms))
					# print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))
					# print('  lost packets       {0} PACKETS\n'.format(result.lost_packets))

					# print('Average transmitted data in all sorts of networky formats:')
					# # print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
					# print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
					# # print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
					# # print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
