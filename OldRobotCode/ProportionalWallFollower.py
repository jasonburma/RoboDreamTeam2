#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

#Line follower without PID
#Lab 7

_min = 5
_max = 50
pGain = 105
speed = 150
us = UltrasonicSensor()
ts = TouchSensor()

assert us.connected, "connect the ultrasonic sensor ya goon"
assert ts.connected, "touch sensor pls"

#target = int((_min + _max)/2)
target = 15

mB = LargeMotor('outB')
mC = LargeMotor('outC')

btn = Button()

while True:

	if ts.value():
		Sound.speak("Ouch")
		mB.stop(stop_action='brake')
		mC.stop(stop_action='brake')

		sleep(1)
		mB.run_to_rel_pos(position_sp=-720, speed_sp=speed, stop_action="brake")   
		mC.run_to_rel_pos(position_sp=-720, speed_sp=speed, stop_action="brake")
		
		sleep(1)
		mB.stop(stop_action='brake')
		mC.stop(stop_action='brake')
		sleep(1)
		mB.run_to_rel_pos(position_sp=200, speed_sp=speed, stop_action="brake")
		mC.run_to_rel_pos(position_sp=-200, speed_sp=speed, stop_action="brake")
		sleep(1)

	print(us.value())
	error = us.value() - target
	if us.value() > 250:
		error = 250 - target

	

	a = (pGain * error)/10
	c = (speed + a )
	b = (speed - a)

	if c > 200:
		c = 200
	if b > 200:
		b = 200
	if c < -200:
		c = -200

	if b < -200:
		b = -200
	print(a, b, c)

	mB.run_forever(speed_sp=b)
	mC.run_forever(speed_sp=c)

	if btn.any():

		mB.stop(stop_action='brake')
		mC.stop(stop_action='brake')
		break;

