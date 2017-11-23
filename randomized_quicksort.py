#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

import random

def quicksort_partition(arr,low,high):
	
	pivot = arr[high]
	
	i = low - 1
	
	for j in range(low,high):
		
		if arr[j] <= pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
	
	arr[i+1],arr[high] = arr[high],arr[i+1]
	
	return i+1
	
def randomized_partition(arr,low,high):
	
	i = random.randint(low,high)
	
	arr[i],arr[high] = arr[high],arr[i]
	
	return quicksort_partition(arr,low,high)
	
def randomized_quicksort(arr,low,high):
	
	if low < high:
		q = randomized_partition(arr,low,high)
		randomized_quicksort(arr,low,q-1)
		randomized_quicksort(arr,q+1,high)
	


if __name__ == '__main__':
	dummy_list = [3,23,4,1,22,45,3,7,2,97,32,12]
	#printing dummy list
	print("printing the dummy list before quicksort.")
	print(*dummy_list)
	randomized_quicksort(dummy_list,0,len(dummy_list)-1)
	print('Dummy list after quicksort.')
	print(*dummy_list)
