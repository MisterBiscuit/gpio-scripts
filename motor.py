import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40

mPin1 = 13
mPin2 = 11
enablePin = 15

def analogRead(channel):
	value = bus.read_byte_data(address, cmd + channel)
	return value

def analogWrite(value):
	bus.write_byte_data(address, cmd, value)

def setup():
	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(mPin1, GPIO.OUT)
	GPIO.setup(mPin2, GPIO.OUT)
	GPIO.setup(enablePin, GPIO.OUT)

	p = GPIO.PWM(enablePin, 1000)
	p.start(0)

def mapNum(value, fromLow, fromHigh, toLow, toHigh):
	'''
	Map the value from a range of mapping to another range
	'''
	return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

def motor(ADC):
	value = ADC - 128
	if(value > 0):
		GPIO.output(mPin1, GPIO.HIGH)
		GPIO.output(mPin2, GPIO.LOW)
		print('Turn forward')
	elif(value < 0):
		GPIO.output(mPin1, GPIO.LOW)
		GPIO.output(mPin2, GPIO.HIGH)
		print('Turn backward')
	else:
		GPIO.output(mPin1, GPIO.LOW)
		GPIO.output(mPin2, GPIO.LOW)
		print('Stop')
	p.start(mapNum(abs(value), 0, 128, 0, 100))
	print('The PWM duty cycle is %d%%\n'%(abs(value) * 100 / 127))

def loop():
	while True:
		value = analogRead(0)
		print('ADC value: %d'%(value))
		motor(value)
		time.sleep(0.01)

def destroy():
	bus.close()
	GPIO.cleanup()

if __name__ == '__main__':
	print('Program starting...')
	setup()
	try:
		loop()
	except KeyboardInterruption:
		destroy()