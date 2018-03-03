import smbus
import time

address = 0x48 # default address for PCF8591
bus = smbus.SMBus(1)
cmd = 0x40 #command

def analogRead(chn): # read ADC value, chn: 0,1,2,3
    value = bus.read_byte_data(address, cmd + chn)
    return value

def analogWrite(value): # write DAC value
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value = analogRead(0) # read the ADC value of channel 0
        analogWrite(value) # write the DAC value
        voltage = value / 255.0 * 3.3 # calculate the voltage value
        print('ADC value: %d, voltage: %.2f'%(value, voltage))
        time.sleep(0.1)

def destroy():
    bus.close()
    print('Closed bus')

if __name__ == '__main__':
    print('Program starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
