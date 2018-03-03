import RPi.GPIO as GPIO

buzzerPin = 11
buttonPin = 12

def setup():
    print('Program starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin) == GPIO.LOW:
            GPIO.output(buzzerPin, GPIO.HIGH)
            print('Buzzer on')
        else:
            GPIO.output(buzzerPin, GPIO.LOW)
            print('Buzzer off')

def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

