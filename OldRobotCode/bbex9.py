
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

us = UltrasonicSensor() 
assert us.connected, "Connect a US sensor to any sensor port"
us.mode='US-DIST-CM'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while True:    # forever
    Distance=us.value()/10  # convert to cm
    if Distance >10 and Distance <20:
        mB.run_forever(speed_sp=450)
        mC.run_forever(speed_sp=450)
    else:
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake')
    sleep(0.1)