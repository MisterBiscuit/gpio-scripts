import RPi.GPIO as GPIO
import Keypad
from LCDDisplay import LCDDisplay

from time import sleep, strftime
from datetime import datetime

ROWS = 4
COLS = 4
keys = [
    '1', '2', '3', 'A',
    '4', '5', '6', 'B',
    '7', '8', '9', 'C',
    '*', '0', '#', 'D'
]
rowsPins = [12, 16, 18, 22] # connect to the row pinouts of the keypad
colsPins = [19, 15, 13, 11] # connect to the column pinouts of the keypad

def loop():
    lcd.start()

    keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
    keypad.setDebounceTime(50)

    keyString = ""

    while(lcd.RUNNING):
        key = keypad.getKey()
        if(key != keypad.NULL):
            if len(keyString) >= 32:
                keyString = keyString[-31:]
            keyString += key
        firstLine = ""
        secondLine = ""
        if(len(keyString) > 16):
            firstLine = keyString[:16]
            secondLine = keyString[16:]
        else:
            firstLine = keyString
        stringMessage = firstLine + "\n" + secondLine
        lcd.showMessage(stringMessage)
        print('----------------')
        print(stringMessage)
        sleep(lcd.DELAY)

if __name__ == '__main__':
    print('Program starting...')
    lcd = LCDDisplay(False, 1)
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        lcd.stop()
        lcd.destroy()
