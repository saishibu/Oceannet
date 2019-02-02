#!/usr/bin/python

print('initialising stepper control...')

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control_pins = [6,13,19,26]
control_pins2 = [26,19,13,6]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,1],
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1]
]
for i in range(100):
  for halfstep in range(8):
    for pin in range(4):
      print(i)
      if i<=30:
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.01)
      else:
        GPIO.output(control_pins2[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.01)
            
GPIO.cleanup()
print("test completed")
