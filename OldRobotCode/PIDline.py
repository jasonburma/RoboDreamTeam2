#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
#Line follower with PID
#Lab 7

_min = 5
_max = 90
pGain = 2.4
iGain = 0.016256
dGain = 88.567
iFactor = .5
errorSum = 0.0
prevError = 0.0


speed = 200
cl = ColorSensor()

assert cl.connected, "connect the color sensor ya goon"

target = int((_min + _max)/2)


mB = LargeMotor('outB')
mC = LargeMotor('outC')

btn = Button()

start = time.clock()
for i in range(2000):

	intensity = cl.value()
	error = intensity - target
	errorSum = iFactor*errorSum + error
	errorDif = error - prevError
	correction = pGain*error + iGain*errorSum + dGain*errorDif

	
	c = (speed + correction)
	b = (speed - correction)

	print(b,c)
	mB.run_forever(speed_sp=b)
	mC.run_forever(speed_sp=c)

print((time.clock() - start)/2000)
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
