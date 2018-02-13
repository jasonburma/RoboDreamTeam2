#!/usr/bin/python
#Jenny Steffens

import threading
from ev3dev import *
from time import sleep
from time import clock

speed = 120 

mNS = LargeMotor('outB')		#Depends on where the motors actually are
mEW = LargeMotor('outC')

tsN = TouchSensor('ev3:in1')		#Hard to find syntax for this, but I believe its right
tsS = TouchSensor('ev3:in2')
tsE = TouchSensor('ev3:in3')
tsW = TouchSensor('ev3:in4')

driveNS = 1 	#We start in the Southwest corner, so we're going to start by heading north
driveEW = 0	

lockNS = threading.Lock()
lockEW = threading.Lock()

done = 0    #Not done


def driveControlNS():

	global driveNS
	global done

	while (done != 2):
		sleep(0.1)
		if driveNS != 0:
			lockNS.acquire(True)
			mNS.run_forever(speed_sp=(speed*driveNS))		#If driveNS is negative, we will head South
			lockNS.release()
	return
	#Killing a thread abruptly is bad for the computer. So, instead we can just return when things are all done.

def driveControlEW():
	global driveEW
	global done

	while (done != 2):
		sleep(0.1)
		if driveEW != 0:
			lockEW.acquire(True)
			mEW.run_forever(speed_sp=(speed*driveEW))		#If driveEW is negative, we will head West
			lockEW.release()

	return

def vacuumControl():

	global driveNS
	global driveEW
	global done

	if tsN.is_pressed():  #North
	
		lockNS.acquire(True)
		lockEW.acquire(True)
		mNS.stop(stop_action='brake')		#Stop the motor
		driveNS = 0;

		if not done:
			
			lockNS.release()
			driveEW = 1;
			lockEW.release()
			sleep(1)			#scootch a little to the right (half a second), and then grab the lock again. This number would really matter
			lockEW.acquire(True)		#		on how big the robot is. I'm assuming it is pretty small, and this should suffice. 
			lockNS.acquire(True)

		
		driveEW = 0;			#turn off east and west
		lockEW.release()
		driveNS = -1;			#Start heading south
		lockNS.release()		#If we've touched the East wall (done), we need to still head south, so we'll do this part either way


	if tsS.is_pressed(): #South
		

		lockNS.acquire(True)
		lockEW.acquire(True)
		mNS.stop(stop_action='brake')
		driveNS = 0

		if not done:

			driveEW = 1;			
			lockEW.release()

			sleep(1)				#scootch to the right, then grab the lock again
			lockEW.acquire(True)
			lockNS.acquire(True)
			
			driveEW = 0;
			lockEW.release()
		
			driveNS = 1;
			lockNS.release()

		else:
			
			driveEW = -1;			#If we've already touched the East wall, we want to head west to the beginning position
			lockNS.release()
			lockEW.release()




	if tsE.is_pressed(): #East
		if not done:
			lockNS.acquire(True)
			lockEW.acquire(True)
			done = 1
			driveNS = driveNS* -1
			#drive that direction

			if driveNS = 1:
				driveEW = 0
				lockNS.release()
				lockEW.release()c

				#do the north loop again

			else:
				driveEW = -1
				driveNS = 0
				lockNS.release()
				lockEW.release()
				
		else:
			pass      #We may scrape along the East wall a little as we make our last vaccuum, this is ok; we want to vaccuum everywhere
					

	if tsW.is_pressed(): #West

		if done:					#If we've touched the East wall before, this means we're at the end
			lockEW.acquire(True)
			driveEW = 0
			mEW.stop(stop_action='brake')
			lockNS.acquire(True)
			driveNS = 0
			mNS.stop(stop_action='brake')
			done = 2   
			lockNS.release()
			lockEW.release()
			     #This way the program will know the robot is in its original position
		
		else:
			pass   	#We may scape against the west wall on our way up from the start if the user puts us too close. That's fine.


threadNS = threading.Thread(target=driveControlNS)
threadEW = threading.Thread(target=driveControlEW)
threadV	 = threading.Thread(target=vacuumControl)	

threadNS.start()
threadEW.start()
threadV.start()

threadNS.join()
threadEW.join()
threadV.join()

while done != 2:
	sleep(.1)		#wait for the threads to finish

lockEW.acquire(True)
lockNS.acquire(True)


















