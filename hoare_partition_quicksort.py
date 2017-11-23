#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Hoare partition based quicksort
#  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC> 


def hoare_partition(arr,low,high):
	
	pivot = arr[low]
	i = low - 1
	j = high + 1
	
	while True:
		
		i += 1
		while arr[i] < pivot:
			i += 1
		
		j -= 1
		while arr[j] > pivot:
			j -= 1
		
		
		
		if i < j:
			arr[i],arr[j] = arr[j],arr[i]
		else:
			return j

def quicksort(arr,low,high):
	
	if low < high:
		q = hoare_partition(arr,low,high)
		
		quicksort(arr,low,q)
		quicksort(arr,q+1,high)
		
if __name__ == '__main__':
	dummy_list = [3,23,4,1,22,45,3,7,2,97,32,12]
	#printing dummy list
	print("printing the dummy list before quicksort.")
	print(*dummy_list)
	quicksort(dummy_list,0,len(dummy_list)-1)
	print('Dummy list after quicksort.')
	print(*dummy_list)


