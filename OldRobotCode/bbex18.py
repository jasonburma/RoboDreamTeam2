#!/usr/bin/env python3
#Lab 6
from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor() 
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode='COL-COLOR'

ts=TouchSensor()
assert ts.connected, "Connect a touch sensor to any sensor port"

mB = LargeMotor('outB'); mC = LargeMotor('outC')

def WaitForBump():  # a 'bump' is a release of the touch sensor button
    PreviousState=0
    while True:
        CurrentState=ts.value()
        if PreviousState==1 and CurrentState==0: #button was released
            break     # button has just been released so exit loop
        PreviousState=CurrentState   # Ready for next loop
        sleep(0.01)  # don't read the sensor too frequently

Colors=[]  # create empty list
for i in range(0, 4):  # i=0 then 1 then 2 then 3
    Sound.play('sounds/click.wav').wait()
    WaitForBump()
    while True:   # Wait for a valid color to be detected
        ColorCode=cl.value()
        if ColorCode==2 or ColorCode==3 or ColorCode==4:
        # blue,green,yellow
            Colors.append(ColorCode)
            break   # exit the loop
        sleep(0.01)  # don't read the sensor too frequently

Sound.play('sounds/horn.wav').wait()

for k in range(0, 4):     # k=0 then 1 then 2 then 3
    if Colors[k]==2:      # blue
        mB.run_to_rel_pos(position_sp=-345, speed_sp=450, stop_action='hold')
         mC.run_to_rel_pos(position_sp=345,  speed_sp=450, stop_action='hold')
        # 345 degrees wheel rotation is about correct
        # to turn the robot 90 degrees    
    elif Colors[k]==3:    # green
        mB.run_to_rel_pos(position_sp=360,  speed_sp=450)
        mC.run_to_rel_pos(position_sp=360,  speed_sp=450)
    elif Colors[k]==4:    # yellow
        mB.run_to_rel_pos(position_sp=345,  speed_sp=450)
        mC.run_to_rel_pos(position_sp=-345, speed_sp=450)
    sleep(3)  # give enough time for the motors to finish moving
