import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
zPin = 12

def analogRead(channel):
	bus.write_byte(address, cmd + channel)
	value = bus.read_byte(address)
	value = bus.read_byte(address)
	return value

def analogWrite(value):
	bus.write_byte_data(address, cmd, value)

def setup():
	global pR, pG, pB
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(zPin, GPIO.IN, GPIO.PUD_UP)

def loop():
	while True:
		valZ = GPIO.input(zPin)
		valY = analogRead(1)
		valX = analogRead(2)

		print('X: %d, Y: %d, Z: %d'%(valX, valY, valZ))
		time.sleep(0.01)

def destroy():
	bus.close()
	GPIO.cleanup()

if __name__ == '__main__':
	print('Program starting...')
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
