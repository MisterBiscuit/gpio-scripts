import RPi.GPIO as GPIO

relayPin = 11
buttonPin = 12
relayState = False

def setup():
	print('Program starting')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(relayPin, GPIO.OUT)
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
	global relayState
	print('buttonEvent GPIO%d'%channel)
	relayState = not relayState
	if relayState:
		print('Turn on relay')
	else:
		print('Turn off relay')
	GPIO.output(relayPin, relayState)

def loop():
	GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonEvent, bouncetime=300)
	while True:
		pass

def destroy():
	GPIO.output(relayPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterruption:
		destroy()