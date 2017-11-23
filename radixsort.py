#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>


def countingsort(arr,exp):
	
	n = len(arr)
	
	output = [0] * n
	
	count = [0] * 10
	
	for i in range(n):
		index = arr[i]//exp
		count[index%10] += 1
	
	for i in range(1,10):
		count[i] += count[i-1]
	
	i = n - 1
	while i >= 0:
		index = arr[i]//exp
		output[count[index%10]-1] = arr[i]
		count[index%10] -= 1
		i -= 1
	
	for i in range(len(arr)):
		arr[i] = output[i]
	
def radixsort(arr):
	
	exp = 1
	largest_number = max(arr)
	
	while largest_number//exp > 0:
		countingsort(arr,exp)
		exp *= 10


if __name__ == '__main__':
	arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
	print('array before sorting')
	print(*arr)
	
	radixsort(arr)
	
	print('array after sorting')
	print(*arr)
