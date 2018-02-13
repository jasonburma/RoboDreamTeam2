#!/usr/bin/env python3
#Lab 6
from ev3dev.ev3 import *

cl = ColorSensor() 
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode='COL-COLOR'

us = UltrasonicSensor() 
assert us.connected, "Connect a US sensor to any sensor port"
us.mode='US-DIST-CM'

mB = LargeMotor('outB'); mC = LargeMotor('outC')

mB.run_forever(speed_sp=450)
mC.run_forever(speed_sp=450)

while True:   # forever
    Distance=us.value()/10  # convert mm to cm
    Color=cl.value()
    if Distance>6 and Distance<25 and Color == 1:  # 1 = black
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake')
        break