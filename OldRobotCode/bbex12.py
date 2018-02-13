
#!/usr/bin/env python3
#Lab 6
from ev3dev.ev3 import *
from time import sleep

mB = LargeMotor('outB'); mC = LargeMotor('outC')

cl = ColorSensor() 
assert cl.connected, "Connect a color sensor to any sensor port"

# Put the color sensor into COL-COLOR mode
# to try to identify standard colors and return a
# corresponding integer between 0 and 7
cl.mode='COL-COLOR'

while True: 
    ColorCode=cl.value()
    if ColorCode==3:   # color 3 = green
        mB.run_to_rel_pos(position_sp=360, speed_sp=450, stop_action='brake')
        mC.run_to_rel_pos(position_sp=360, speed_sp=450, stop_action='brake')
    else:
        Sound.play('sounds/click.wav').wait()
        sleep(1)
    