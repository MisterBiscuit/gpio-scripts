import RPi.GPIO as GPIO
import time

ledPin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, 1000) # frequency to 1kHz
    p.start(0) # duty cycle = 0

def loop():
    while True:
        for dc in range(0, 101, 1): # increase duty cycle: 0>100
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100, -1, -1): # increase duty cycle: 100>0
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    p.stop()
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
