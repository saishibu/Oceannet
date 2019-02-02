#!/usr/bin/python

print('initialising stepper control...')

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control_pins = [6,13,19,26]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
for i in range(360):
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    print(pin)
    GPIO.output(pin, 1)
    time.sleep(0.01)
    GPIO.output(pin, 0)
    time.sleep(0.01)
GPIO.cleanup()
print("test completed")
