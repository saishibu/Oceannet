#!/usr/bin/python

print('initialising stepper control...')

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control_pins = [6,13,19,26]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
StepCounter = 0
WaitTime = 0.01

# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# Choose a sequence to use
Seq = Seq1
StepCount = StepCount1

# Start main loop
while 1==1:

  for pin in range(0, 4):
    xpin = control_pins[pin]
    if Seq[StepCounter][pin]!=0:
      # print " Step %i Enable %i" %(StepCounter,xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += 1

  # If we reach the end of the sequence
  # start again
  if (StepCounter==StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount

  # Wait before moving on
  time.sleep(WaitTime)
