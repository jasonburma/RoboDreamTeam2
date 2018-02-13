#!/usr/bin/python

import threading

#these functions will be working on seperate threads


myLock = threading.Lock()
counter = 0;


def functionA():
	global counter
	for i in range(1000000):
	
		#myLock.acquire(True)
		counter += 1
	#	myLock.release()

def functionB():
	global counter
	for i in range(1000000):
		
		#myLock.acquire(True)
		counter -= 1
		#myLock.release()

#set up the threads

threadA = threading.Thread(target=functionA)
threadB = threading.Thread(target=functionB)

threadA.start()
threadB.start()

threadA.join()
threadB.join()

#myLock.acquire(True)

print counter

#myLock.release()