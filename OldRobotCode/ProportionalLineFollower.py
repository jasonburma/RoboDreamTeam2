#!/usr/bin/env python3
from ev3dev.ev3 import *

#Line follower without PID
#Lab 7

_min = 5
_max = 50
pGain = 10.5
speed = 200
cl = ColorSensor()

assert cl.connected, "connect the color sensor ya goon"

target = int((_min + _max)/2)


mB = LargeMotor('outB')
mC = LargeMotor('outC')

btn = Button()

while True:

	error = cl.value() - target
	a = pGain * error
	c = (speed + a )
	b = (speed - a)

	mB.run_forever(speed_sp=b)
	mC.run_forever(speed_sp=c)

	if btn.any():

		mB.stop(stop_action='brake')
		mC.stop(stop_action='brake')
		break;

