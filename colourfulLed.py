import RPi.GPIO as GPIO
import time
import random

pins = {'pinG': 11, 'pinR': 12, 'pinB': 13}

def setup():
    global pR, pG, pB
    print('Program starting...')
    GPIO.setmode(GPIO.BOARD)
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)
    pR = GPIO.PWM(pins['pinR'], 2000) # set frequency to 2kHz
    pG = GPIO.PWM(pins['pinG'], 2000)
    pB = GPIO.PWM(pins['pinB'], 2000)
    pR.start(0)
    pG.start(0)
    pB.start(0)

def setColor(rVal, gVal, bVal):
    print('r=%d, g=%d, b=%d'%(rVal, gVal, bVal))
    pR.ChangeDutyCycle(rVal)
    pG.ChangeDutyCycle(gVal)
    pB.ChangeDutyCycle(bVal)

def randomLoop():
    while True:
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        setColor(r, g, b)
        time.sleep(0.3)

def rgbwLoop():
    while True:
        setColor(0, 100, 100) #green
        time.sleep(0.7)
        setColor(100, 0, 100) #red
        time.sleep(0.7)
        setColor(100, 100, 0) #blue
        time.sleep(0.7)
        setColor(0, 0, 0) #white
        time.sleep(0.7)
        setColor(0, 100, 0) #cyan
        time.sleep(0.7)
        setColor(0, 0, 100) #yellow
        time.sleep(0.7)
        setColor(100, 0, 0) #purple
        time.sleep(0.7)

def loop():
    #randomLoop()
    rgbwLoop()

def destroy():
    pR.stop()
    pG.stop()
    pB.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
