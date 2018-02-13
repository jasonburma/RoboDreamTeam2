
#!/usr/bin/env python3
#Lab 6
from ev3dev.ev3 import *
from time import sleep, time
import math
import ev3dev.fonts as fonts
from PIL import Image, ImageDraw, ImageFont

lcd = Screen()

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# NumRots is number of wheel rotations needed for robot to advance 50 cm
NumRots=50/17.6        # wheel circumference = 17.6 cm
StartTime=time()       # seconds since the 'epoch'

# convert rotations to degrees
mB.run_to_rel_pos(position_sp=NumRots*360, speed_sp=360, stop_action="brake")   
mC.run_to_rel_pos(position_sp=NumRots*360, speed_sp=360, stop_action="brake")

mB.wait_while('running')
mC.wait_while('running')
    
TravelTime=time() - StartTime  # seconds since the 'epoch'
Speed= round(50/TravelTime)  # Speed = distance in cm / time in s
lcd.draw.text((40,50),str(Speed) + ' cm/s', font=fonts.load('helvB24'))
lcd.update()
sleep(5)    # Give enough time for the screen to be read