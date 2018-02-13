#!/usr/bin/python

import threading

#these functions will be working on seperate threads
#Lab 8

myLock = threading.Lock()
counter = 0;


def functionA():
	global counter
	for i in range(4):
	
		myLock.acquire(True)
		counter += 1
		print("A" + str(counter))
		myLock.release()

def functionB():
	global counter
	for i in range(4):
		
		myLock.acquire(True)
		counter -= 1
		print("B" + str(counter))
		myLock.release()

#set up the threads

threadA = threading.Thread(target=functionA)
threadB = threading.Thread(target=functionB)

threadA.start()
threadB.start()

threadA.join()
threadB.join()

myLock.acquire(True)

print counter

myLock.release()