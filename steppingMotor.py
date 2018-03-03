import RPi.GPIO as GPIO
import time

motorPins = (12, 16, 18, 22)
CCWStep = (0x01, 0x02, 0x04, 0x08)
CWStep = (0x08, 0x04, 0x02, 0x01)

def setup():
	print('Program starting')
	GPIO.setmode(GPIO.BOARD)
	for pin in motorPins:
		GPIO.setup(pin, GPIO.OUT)

def moveOneCycle(direction, ms):
	'''
	As for four phase stepping motors, four steps is a cycle.
	Drives a motor clockwise or anticlockwise for four steps
	'''
	for j in range(0, 4, 1):
		for i in range(0, 4, 1):
			if(direction == 1): #Clockwise
				GPIO.output(motorPins[i], ((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
			else:
				GPIO.output(motorPins[i], ((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
		if(ms < 3): # the delay cannot be less than 3ms or it will exceed the motor's top speed
			ms = 3
		time.sleep(ms * 0.001)

def moveSteps(direction, ms, steps):
	'''
	Continuous rotation function.
	The steps parameter specifies the rotation cyles, every four steps is a full cycle
	'''
	for i in range(steps):
		moveOneCycle(direction, ms)

def motorStop():
	'''
	Stop rotating
	'''
	for i in range(0, 4, 1):
		GPIO.output(motorPins[i], GPIO.LOW)

def loop():
	while True:
		moveSteps(1, 3, 512) # rotating 360 degrees clockwise, a total of 2048 steps in a circle, namely 512 cycles
		time.sleep(0.5)
		moveSteps(0, 3, 512) # rotating 360 degrees anticlockwise
		time.sleep(0.5)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterruption:
		destroy()