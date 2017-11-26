#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def rod_cut_rec(p,n):
	
	# If the length of rod is zero means no profit.
	# or otherwise return something else if you can fool them in 
	#buying invisible rods.
	if n <= 0:
		return 0
		
	q = -1
	
	#checking every possible case of cutting the rod.
	for i in range(0,n):
		q = max(q,p[i] + rod_cut_rec(p,n-i-1))
		
	return q

if __name__ == '__main__':
	arr = [1, 5, 8, 9, 10, 17, 17, 20]
	size = len(arr)
	print('Maximum obtainable value is',rod_cut_rec(arr,size))
