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
time.sleep(2)
GPIO.output(26,GPIO.LOW)
time.sleep(2)
#FWD LED
GPIO.output(27,GPIO.HIGH)
time.sleep(2)
GPIO.output(27,GPIO.LOW)
time.sleep(2)
#Rev LED
GPIO.output(17,GPIO.HIGH)
time.sleep(2)
GPIO.output(17,GPIO.LOW)
time.sleep(2)
#RSSI1
GPIO.output(19,GPIO.HIGH)
time.sleep(2)
GPIO.output(19,GPIO.LOW)
time.sleep(2)
#RSSI2
GPIO.output(13,GPIO.HIGH)
time.sleep(2)
GPIO.output(13,GPIO.LOW)
time.sleep(2)
#RSSI3
GPIO.output(6,GPIO.HIGH)
time.sleep(2)
GPIO.output(6,GPIO.LOW)
time.sleep(2)
#RSSI4
GPIO.output(5,GPIO.HIGH)
time.sleep(2)
GPIO.output(5,GPIO.LOW)
time.sleep(2)

print "LED Test Complete"
