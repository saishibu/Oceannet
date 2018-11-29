#!/usr/bin/python           # This is server.py file

import iperf3
print("Starting IPERF SERVER ")
server = iperf3.Server()
server.bind_address = '127.0.0.1'  #Change the IPAddress of the Baot Device 
server.port =  5001
server.verbose = False
while True:
	result = server.run()
