import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40

ledRedPin = 15
ledGreenPin = 13
ledBluePin = 11

def analogRead(channel):
	bus.write_byte(address, cmd + channel)
	value = bus.read_byte(address)
	return value

def analogWrite(value):
	bus.write_byte_data(address, cmd, value)

def setup():
	global pR, pG, pB
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledRedPin, GPIO.OUT)
	GPIO.setup(ledGreenPin, GPIO.OUT)
	GPIO.setup(ledBluePin, GPIO.OUT)

	pR = GPIO.PWM(ledRedPin, 1000)
	pR.start(0)
	pG = GPIO.PWM(ledGreenPin, 1000)
	pG.start(0)
	pB = GPIO.PWM(ledBluePin, 1000)
	pB.start(0)

def loop():
	while True:
		vR = analogRead(0)
		vG = analogRead(1)
		vB = analogRead(2)

		pR.ChangeDutyCycle(vR * 100 / 255)
		pG.ChangeDutyCycle(vG * 100 / 255)
		pB.ChangeDutyCycle(vB * 100 / 255)

		print('ADC value: R: %d, G: %d, B: %d'%(vR, vG, vB))
		time.sleep(0.01)

def destroy():
	bus.close()
	GPIO.cleanup()

if __name__ == '__main__':
	print('Program is starting...')
	setup():
	try:
		loop()
	except KeyboardInterrupt:
		destroy()