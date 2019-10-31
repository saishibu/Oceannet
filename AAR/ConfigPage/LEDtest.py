#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT)  #REV
GPIO.setup(27,GPIO.OUT)  #FWD
GPIO.setup(26,GPIO.OUT)  #Status LED
GPIO.setup(19,GPIO.OUT) #RSSI 0
GPIO.setup(13,GPIO.OUT)	#RSSI 1
GPIO.setup(6,GPIO.OUT)  #RSSI 2
GPIO.setup(5,GPIO.OUT)  #RSSI 3
#Status LED
GPIO.output(26,GPIO.HIGH)
time.sleep(1)
GPIO.output(26,GPIO.LOW)
time.sleep(1)
print("Status LED Completed")
#FWD LED
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
print("FWD LED Completed")
#Rev LED
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
print("REV LED Completed")
#RSSI4 - 
GPIO.output(19,GPIO.HIGH)
time.sleep(1)
GPIO.output(19,GPIO.LOW)
time.sleep(1)
print("RSSI4 LED Completed")
#RSSI3
GPIO.output(13,GPIO.HIGH)
time.sleep(1)
GPIO.output(13,GPIO.LOW)
time.sleep(1)
print("RSSI3 LED Completed")
#RSSI2
GPIO.output(6,GPIO.HIGH)
time.sleep(1)
GPIO.output(6,GPIO.LOW)
time.sleep(1)
print("RSSI2 LED Completed")
#RSSI4
GPIO.output(5,GPIO.HIGH)
time.sleep(1)
GPIO.output(5,GPIO.LOW)
time.sleep(1)
print("RSSI1 LED Completed")

#Full signal
GPIO.output(5,GPIO.HIGH) #4
GPIO.output(6,GPIO.HIGH) #3
GPIO.output(13,GPIO.HIGH) #2
GPIO.output(19,GPIO.HIGH) #1
time.sleep(1)
GPIO.output(5,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
time.sleep(1)
print("Full Signal  Completed")

#75% signal
GPIO.output(5,GPIO.HIGH) #4
GPIO.output(6,GPIO.HIGH) #3
GPIO.output(13,GPIO.HIGH) #2
#GPIO.output(19,GPIO.HIGH) #1
time.sleep(1)
GPIO.output(5,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
#GPIO.output(19,GPIO.LOW)
time.sleep(1)
print("75% Signal  Completed")

#50% signal
GPIO.output(5,GPIO.HIGH) #4
GPIO.output(6,GPIO.HIGH) #3
#GPIO.output(13,GPIO.HIGH) #2
#GPIO.output(19,GPIO.HIGH) #1
time.sleep(1)
GPIO.output(5,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
#GPIO.output(13,GPIO.LOW)
#GPIO.output(19,GPIO.LOW)
time.sleep(1)
print( "50% Signal  Completed" )

#25% signal
GPIO.output(5,GPIO.HIGH) #4
#GPIO.output(6,GPIO.HIGH) #3
#GPIO.output(13,GPIO.HIGH) #2
#GPIO.output(19,GPIO.HIGH) #1
time.sleep(1)
GPIO.output(5,GPIO.LOW)
#GPIO.output(6,GPIO.LOW)
#GPIO.output(13,GPIO.LOW)
#GPIO.output(19,GPIO.LOW)
time.sleep(1)
print("25% Signal  Completed" )

#No signal
GPIO.output(5,GPIO.HIGH) #4
#GPIO.output(6,GPIO.HIGH) #3
GPIO.output(13,GPIO.HIGH) #2
#GPIO.output(19,GPIO.HIGH) #1
time.sleep(1)
GPIO.output(5,GPIO.LOW)
#GPIO.output(6,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
#GPIO.output(19,GPIO.LOW)
time.sleep(1)
print("N0 Signal  Completed")

print("Success: LED Test Complete")
