from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

class LCDDisplay:
    PCF8574_address = 0x27
    PCF8574A_address = 0x3F

    def __init__(self, scroll = False, delay = 1):
        self.RUNNING = False
        self.SCROLL = scroll
        self.DELAY = delay
        try:
            self.MCP = PCF8574_GPIO(self.PCF8574_address)
        except:
            try:
                self.MCP = PCF8574_GPIO(self.PCF8574A_address)
            except:
                raise Exception('I2C address error.')

        self.LCD = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.MCP)
        self.MCP.output(3, 1) # turn on LCD backlight
        self.LCD.begin(16, 2) # set number of LCD columns and lines

    def start(self):
        self.RUNNING = True

    def stop(self):
        self.RUNNING = False

    def setScroll(self, scroll):
        self.SCROLL = scroll

    def setDelay(self, delay):
        self.DELAY = delay

    def destroy(self):
        self.LCD.clear()

    def showMessage(self, message):
        self.LCD.setCursor(0, 0)

        line1, line2 = message.split('\n')
        self.LCD.message(line1 + '\n')
        self.LCD.message(line2)
