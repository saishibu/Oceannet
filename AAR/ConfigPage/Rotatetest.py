#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT)  #REV
GPIO.setup(27,GPIO.OUT)  #FWD
GPIO.setup(26,GPIO.OUT)  #Status LED
#Status LED
GPIO.output(26,GPIO.HIGH)
time.sleep(1)
print("Status LED Completed")
print("Starting rotation test")
#FWD LED
GPIO.output(27,GPIO.HIGH)
time.sleep(31)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
print("FWD  Completed")
#Rev LED
GPIO.output(17,GPIO.HIGH)
time.sleep(31)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
print("REV  Completed")
GPIO.output(26,GPIO.LOW)
print("Success: Rotate Test Complete")
