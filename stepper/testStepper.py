#!/usr/bin/python

print('initialising stepper control...')

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control_pins = [6,13,19,26]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,1],
  [1,1,0,0],
  [0,1,1,0],
  [0,0,1,1],
  [0,1,1,1],
  [0,1,1,0],
  [1,1,0,0],
  [1,0,0,1]
]
for i in range(256):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      print(halfstep_seq[halfstep][pin])
    time.sleep(0.1)
GPIO.cleanup()
print("test completed")
