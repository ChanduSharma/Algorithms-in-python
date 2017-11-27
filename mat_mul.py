#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

import sys

def mat_mul(p,n):
	
	dp = [ [0 for i in range(n)] for j in range(n)]
	
	for i in range(1,n):
		dp[i][i] = 0
		
	for l in range(2,n):
		for i in range(1,n-l+1):
			j = i + l - 1
			dp[i][j] = sys.maxsize
			
			for k in range(i,j):
				dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])
	
	return dp[1][n-1]

arr = [1, 2, 3 ,4]
size = len(arr)
 
print("Minimum number of multiplications is ",mat_mul(arr,size))
