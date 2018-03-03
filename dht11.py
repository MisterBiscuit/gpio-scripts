import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT

DHTPin = 11

def loop():
    dht = DHT.DHT(DHTPin)
    sumCnt = 0
    while(True):
        sumCnt += 1
        chk = dht.readDHT11(DHTPin)
        print("Iteration %d : %d"%(sumCnt, chk))
        if(chk is dht.DHTLIB_OK):
            print("DHT11, OK!")
        elif(chk is dht.DHTLIB_ERROR_CHECKSUM):
            print("DHTLIB_ERROR_CHECKSUM")
        elif(chk is dht.DHTLIB_ERROR_TIMEOUT):
            print("DHTLIB_ERROR_TIMEOUT")
        else:
            print("Other error")

        print("Humidity: %.2f, Temperature: %.2f\n"%(dht.humidity, dht.temperature))
        time.sleep(1)

if __name__ == '__main__':
    print("Program starting")
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
