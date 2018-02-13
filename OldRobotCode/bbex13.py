#!/usr/bin/env python3
#Lab 6
from ev3dev.ev3 import *
from time import sleep, time

mB = LargeMotor('outB'); mC = LargeMotor('outC')

ts = TouchSensor() 
assert ts.connected, "Connect a touch sensor to any sensor port"

Presses=0  # Number of presses (actually releases)
PreviousState=0

Sound.beep()  # signal to start presses

StartTime=time()
while (time()-StartTime)<5:    # loop until 5 seconds have passed
    CurrentState=ts.value()
    if PreviousState==1 and  CurrentState==0: # button has been released
        Presses+=1  # Short for Presses = Presses + 1
    PreviousState=CurrentState   # Ready for next loop
    sleep(0.01)

mB.run_to_rel_pos(position_sp=Presses*360, speed_sp=450, stop_action='brake')
mC.run_to_rel_pos(position_sp=Presses*360, speed_sp=450, stop_action='brake')

# Wait for motors to complete
mB.wait_while('running'); mC.wait_while('running')