#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, thread, random
import lcd

lcd = lcd.lcd

up = (0, 0)
down = (1, 0)

position = ()

level = (
1.2, 1.0,
0.8, 0.6,
0.4, 0.2
)
current = 0
