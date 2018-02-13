
#!/usr/bin/env python3

#Lab 6



from ev3dev.ev3 import *
from time import sleep
import random

btn = Button() # will use any button to stop script

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# exit loop with a long press on any EV3 button
while not btn.any():
    # generate a random integer between -630 and +630 inclusive
    rand=random.randint(-630,630)
    mB.run_forever(speed_sp=rand)
    mC.run_forever(speed_sp=rand)
    sleep(1)
    mB.stop(stop_action='brake')
    mC.stop(stop_action='brake')
    sleep(1)
    
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')