#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

ledPin = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('using pin %d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('...LED on')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print('...LED off')
        time.sleep(1)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        try:
            loop()
        except KeyboardInterrupt: # When 'Ctrl+C' is pressed, do cleanup
            destroy()
    except:
        print('An error occurred...')
