#!/usr/bin/python

import iperf3
server = iperf3.Server()
server.port = 5001
server.verbose=0
while 1:
	result = server.run()
