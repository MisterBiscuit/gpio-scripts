from LCDDisplay import LCDDisplay

from time import sleep, strftime
from datetime import datetime

def get_cpu_temp():
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format(float(cpu)/1000) + ' C'

def get_time_now():
    return datetime.now().strftime('%H:%M:%S')

def loop():
    lcd.start()

    while(lcd.RUNNING):
        cpuTemp = 'CPU: ' + get_cpu_temp()
        time = get_time_now()

        lcd.showMessage(cpuTemp + '\n' + time)
        print("DISPLAYING\n==========")
        print(cpuTemp)
        print(time)
        print("\n")
        sleep(lcd.DELAY)

if __name__ == '__main__':
    print('Program starting...')
    lcd = LCDDisplay(False, 1)
    try:
        loop()
    except KeyboardInterrupt:
        lcd.stop()
        lcd.destroy()
