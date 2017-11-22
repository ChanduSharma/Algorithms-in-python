#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>


def max_heapify(arr,n,i):
	
	while i < n:
		l = 2*i + 1
		r = 2*i + 2
		
		if l < n and arr[l] > arr[i]:
			largest = l
		else:
			largest = i
		
		if r < n and arr[r] > arr[largest]:
			largest = r
		
		if largest != i:
			arr[i],arr[largest] = arr[largest],arr[i]
			i = largest
		else:
			 break
	

def heapsort(arr):
	
	n = len(arr)
	
	#building max heap
	
	for i in range(n-1,-1,-1):
		max_heapify(arr,n,i)
		
	for i in range(n-1,0,-1):
		arr[i],arr[0] = arr[0],arr[i]
		max_heapify(arr,i,0)




if __name__ == '__main__':
	dummy_list = [3,23,4,1,22,45,3,7,2,97,32,12]
	#printing dummy list
	print("printing the dummy list before heapsort.")
	print(*dummy_list)
	heapsort(dummy_list)
	print('Dummy list after heapsort.')
	print(*dummy_list)
	
