#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Counting sort is applied when the range of the input element is in 
#  0 to k where k is a small number.
#  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC> 


def counting_sort(A,k):
	
	c = [0] * (k+1)
	# initializing the frequency table for each element of k.

	#calculating the frequency of each element of array A.
	for i in range(0,len(A)):
		c[A[i]] += 1
	
	
	for i in range(1,k+1):
		c[i] += c[i-1]
		
		
	result = [0] * len(A)
	
	for i in range(len(A)-1,-1,-1):
		result[c[A[i]]-1] = A[i]
		c[A[i]] -= 1
	
	return result
	
if __name__ == '__main__':
	dummy_list = [4,3,4,2,5,1,0,0,1,2,3,6,4,6,6,6,4,3,2,2]
	print('dummy list before counting sort')
	print(*dummy_list)
	
	dummy_list = counting_sort(dummy_list,max(dummy_list))
	
	print('List after applying counting sort')
	
	print(*dummy_list)
	
	
