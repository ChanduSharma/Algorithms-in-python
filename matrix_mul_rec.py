#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

#Dynamic programming 
#Parenthesizing a chain of matrix to minimize scalar multiplications

INT_MAX = 2**15 - 1

def mat_mul_rec(p,i,j):
	
	if i == j:
		return 0
	
	q = INT_MAX
	for k in range(i,j):
		q = min(q,mat_mul_rec(p,i,k) + mat_mul_rec(p,k+1,j) + p[i-1]*p[k]*p[j])
	
	return q

arr = [1, 2, 3 ,4]
size = len(arr)
 
print("Minimum number of multiplications is ",mat_mul_rec(arr,1, size-1))
		
