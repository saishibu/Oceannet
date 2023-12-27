#!/usr/bin/python

# This code appears to collect data from a NanoStation device, control LEDs, log information, and store data in a database while running an infinite loop. 
# It also includes error handling for exceptions and uses external modules for various functionalities.

# Import the nanostation module (https://github.com/saishibu/Oceannet/blob/master/AAR/nanostation.py) as ns. This module contains functions and definitions related to controlling a NanoStation device.
import nanostation as ns
import time
import datetime
import RPi.GPIO as GPIO
import piggyback as pb
from time import mktime
import logging

# Configure logging settings. It specifies that log messages should be written to the file /home/pi/log/arr.log and the logging level is set to DEBUG.
logging.basicConfig(filename='/home/pi/log/arr.log',level=logging.DEBUG)

# Get the current date and format it as a string.
date=datetime.date.today().strftime("%d_%b_%y")

# Get the current date and time, then convert it to UNIX timestamp format.
t =datetime.datetime.now()
unix_secs = mktime(t.timetuple())

# Call the getConfig() function from the ns module to retrieve configuration data, including IP, log settings, and piggyback settings.
ip,log,piggyback=ns.getConfig()

# Call the getBoatData() function from the ns module to retrieve boat-related data, including the boat name and CPE IP address.
boat,cpe_ip=ns.getBoatData()

# Call the extssid() function from the ns module to extract the SSID of the connected wireless network.
ssid=ns.extssid()

# Initialize an empty dictionary called data and an empty string called diri.
data=dict()
diri=""

# If the log setting is 'on', log a connection successful message along with boat name, IP address, and SSID information.
if log=='on':
	logging.info("Connection Successful\n Boat Name: " + str (boat)+ "\n" + "IP Address: "+str(cpe_ip) + ". Controller Connnected to "+str(ssid))
	
# Call the login() function from the ns module to log in to a NanoStation device using the CPE IP address. This function likely sets up a session and stores cookies for subsequent requests.
cj,opener=ns.login(cpe_ip)

# Print a message indicating successful login to a boat with its name and CPE IP address.
print("Logged in to " + boat + " " +cpe_ip)

# If the log setting is 'on', log a message indicating a successful login.
if log=='on':
	logging.info("login success")

# Call the statusled() function from the ns module to turn on a status LED (assuming this controls an LED).
ns.statusled(1)

# Call the fromdb() function from the ns module to retrieve the last position from a database.
pos=ns.fromdb()

# Initialize the hide variable to 0.
hide=0

# Start an infinite loop.
while 1:
	# Call the stop() function and turn off the status LED at the beginning of each loop iteration.
	ns.stop()
	ns.statusled(0)

	# Call the fetchstatus() function from the ns module to retrieve various status information from the NanoStation device. These values are unpacked into variables.
	signal,rssi,noise,ccq,distance,txrate,rxrate,freq,channel = ns.fetchstatus(cj,opener,cpe_ip)
	
	# Try to call the fetchip() function from the ns module to retrieve IP address and ping status. Handle exceptions and set default values if there's an error.
	try:
		bs_ip,ping_ms=ns.fetchip(cj,opener,cpe_ip)
	except:
		bs_ip="0.0.0.0"
		ping_ms=0
	
	# Call the thmap() function from the ns module to map thresholds based on the distance. These values are unpacked into variables.
	th,hide=ns.thmap(distance)
	
	# Calculate the inverse of the signal strength (signalinv) and call the rssiled() function to control RSSI LEDs based on RSSI values.
	signalinv=signal*-1
	ns.rssiled(rssi)
	
	# Create a dictionary named data with various collected data values.
	    data = {
        'ping_ms': ping_ms,
        'TIME': unix_secs,
        'dir': diri,
        'boat': 1,
        'ss': signal,
        'nf': noise,
        'rssi': rssi,
        'pos': pos,
        'ccq': ccq,
        'd': distance,
        'txrate': txrate,
        'rxrate': rxrate,
        'freq': freq,
        'channel': channel,
        'bs_ip': bs_ip
    }

# 	if log==1:
# 		print data
	# Check the signal level and control the rotation of AAR
	if signalinv > th:
		hide=0
		if pos>36:
			pos=0
			diri='Calibration'
		elif pos >18 and pos <36:
			ns.rev()
			pos=pos+1
			diri='Reverse'
		else:
			ns.fwd()
			diri='Forward'
			pos=pos+1
	elif signalinv ==0:
		if pos >36:
			pos=0
			diri='Calibration'
		elif pos >18 and pos<36:
			ns.rev()
			pos=pos+1
			diri='Rescan & Reverse'
		else:
			ns.fwd()
			diri='Rescan & Forward'
			pos=pos+1
	else:
		hide=10
		ns.stop()
		diri='Stop'
		
	#Data storage
	data={'ping_ms':ping_ms,'TIME':unix_secs,'dir':diri,'boat':1,'ss':signal,'nf':noise,'rssi':rssi,'pos':pos,'ccq':ccq,'d':distance,'txrate':txrate,'rxrate':rxrate,'freq':freq,'channel':channel,'bs_ip':bs_ip}

	# If the log setting is 'on', log the data dictionary.

	if log=='on':
		logging.info(data)
	if piggyback ==1:
		pb.helper(data)
	
	# Call the todb() function from the ns module to write the data to a database.
	ns.todb(data)

	# Call the breathe() function from the ns module to simulate a breathing effect using an LED for 5 seconds (with hide seconds hidden).
	ns.breathe(5,hide)
# Clean up and release the Raspberry Pi GPIO resources before exiting the script.
GPIO.cleanup()



