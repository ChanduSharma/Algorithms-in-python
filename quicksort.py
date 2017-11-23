#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC> 

def quicksort_partition(arr,p,r):
	
	x = arr[r]
	i = p - 1
	for j in range(p,r):
		if arr[j] <= x:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]
	
	arr[i+1],arr[r] = arr[r],arr[i+1]
	return i+1

def quicksort(arr,p,r):
	if p < r:
		q = quicksort_partition(arr,p,r)
		quicksort(arr,p,q-1)
		quicksort(arr,q+1,r)
		

if __name__ == '__main__':
	dummy_list = [3,23,4,1,22,45,3,7,2,97,32,12]
	#printing dummy list
	print("printing the dummy list before quicksort.")
	print(*dummy_list)
	quicksort(dummy_list,0,len(dummy_list)-1)
	print('Dummy list after heapsort.')
	print(*dummy_list)
