#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
# name = 'Chandra Kant Sharma'

	
	
def writer(name):

	#printing each character with a delay of 0.2 seconds.
	for i in range(len(name)):
		print(name[i],end='',flush=True)
		time.sleep(0.12)

	time.sleep(2) 
	for i in range(len(name)):
		print('\b \b',end='',flush=True)
		time.sleep(0.12)

if __name__ == '__main__':

	#getting the name from the command line.
	name = ' '.join(sys.argv[1:])
	
	writer(name)
