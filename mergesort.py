#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def merge(A,p,q,r):
	m = q - p + 1
	n = r - q
	
	L = [0] * m
	R = [0] * n
	
	for i in range(0,m):
		L[i] = A[p+i]
	
	for i in range(0,n):
		R[i] = A[q + i + 1]
	
	i = 0
	j = 0
	k = p
	
	while i < m and j < n:
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1
	
	while i < m:
		A[k] = L[i]
		i += 1
		k += 1
	
	while j < n:
		A[k] = R[j]
		j += 1
		k += 1


def merge_sort(A,p,r):
	if p < r:
		q = (p + r)//2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)


if __name__ == '__main__':
	dummy_list = [11,22,33,1,7,3,5,35,2,-3]
	print("Before merge sort")
	print(*dummy_list)
	print('\n')
	merge_sort(dummy_list,0,len(dummy_list)-1)
	print('After the merge sort')
	print(*dummy_list)
	
	
