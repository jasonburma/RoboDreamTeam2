#!/usr/bin/env python3
#Lab 6

from ev3dev.ev3 import *
from time import sleep
import math  # needed for cos() and radians()

# Connect gyro sensor to any sensor port and check it is connected.
gy = GyroSensor() 
assert gy.connected, "Connect a single gyro sensor to any sensor port"

gy.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.

# Attach large motors to ports B and C

mB = LargeMotor('outB')
mC = LargeMotor('outC')

# Make robot slowly turn to the right on the spot
mB.run_forever(speed_sp=250)
mC.run_forever(speed_sp=-250)

while gy.value()<45:
    sleep(0.01) # Continue looping while turn angle less than 45 deg

length = 25/math.cos(math.radians(gy.value()))   # calculate length of hypotenuse
rots=length/17.6
# calculate wheel rotations (wheel circumference = 17.6cm)

mB.run_to_rel_pos(position_sp=rots*360, speed_sp=500, stop_action="hold")
mC.run_to_rel_pos(position_sp=rots*360, speed_sp=500, stop_action="hold")

mB.wait_while('running')
mC.wait_while('running')