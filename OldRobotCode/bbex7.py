
#!/usr/bin/env python3
from ev3dev.ev3 import *

#Lab 6

# Connect EV3 color sensor and touch sensor. Check connected.
cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any port" 

# Put the color sensor into COL-AMBIENT mode
# to measure ambient light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode='COL-AMBIENT'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while True:     # forever
    if ts.value()==0:    # touch sensor NOT pressed
        Leds.all_off()   # turn off LEDs
        val=cl.value()
        # turn motors at opposite speeds to turn on the spot
        mB.run_forever(speed_sp=val*9)
        mC.run_forever(speed_sp=-val*9) 
    else:   #  touch sensor is pressed
        mB.stop(stop_action='brake')
        mC.stop(stop_action='brake')
        Leds.set_color(Leds.LEFT,  Leds.RED)
        Leds.set_color(Leds.RIGHT, Leds.RED)