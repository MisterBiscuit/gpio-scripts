import RPi.GPIO as GPIO
import time

OFFSET_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSET_DUTY
SERVO_MAX_DUTY = 12.5 + OFFSET_DUTY
servoPin = 12

def map(value, fromLow, fromHigh, toLow, toHigh):
	return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

def setup():
	print('Program starting')
	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servoPin, GPIO.OUT)
	GPIO.output(servoPin, GPIO.LOW)

	p = GPIO.PWM(servoPin, 50) #set frequency to 50Hz
	p.start(0)

def servoWrite(angle):
	if(angle < 0):
		angle = 0
	elif(angle > 180):
		angle = 180
	p.ChangeDutyCycle(map(angle, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))

def loop():
	while True:
		for dc in range(0, 181, 1):
			servoWrite(dc)
			time.sleep(0.001)
		time.sleep(0.5)

		for dc in range(180, -1, -1):
			servoWrite(dc)
			time.sleep(0.001)
		time.sleep(0.5)

def destroy():
	p.stop()
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
