#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC> 


def bubblesort(arr):
	
	n = len(arr)
	
	for i in range(n):
		
		for j in range(n-i-1):
			
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				

if __name__ == '__main__':
	dummy_list = [23,1,54,2,232,45,7,43,9,77,6,8]
	
	print('List before bubble sort')
	print(*dummy_list)
	
	bubblesort(dummy_list)
	print('List after sorting')
	print(*dummy_list)
