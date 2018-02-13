
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

btn = Button() # will use any button to stop script

# Connect EV3 color sensor and check connected.
cl = ColorSensor() 
assert cl.connected, "Connect a color sensor to any sensor port"

# Put the color sensor into COL-COLOR mode
# to try to identify standard colors and return a
# corresponding integer between 0 and 7
cl.mode='COL-COLOR'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while not btn.any():    # exit loop when any button pressed
    code=cl.value()
    if code==4:  # yellow
        mB.run_forever(speed_sp=360)
        mC.run_forever(speed_sp=90)
    elif code==2:  # blue
        mB.run_forever(speed_sp=90)
        mC.run_forever(speed_sp=360)
    else:
        # no color detected or a color other than yellow or blue
        mB.run_forever(speed_sp=360)
        mC.run_forever(speed_sp=360)
    sleep(0.01)
    
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')