import RPi.GPIO as GPIO
import Keypad

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
    keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
    keypad.setDebounceTime(50)

    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            print('You pressed key : %c'%(key))

if __name__ == '__main__':
    print('Program starting')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup
