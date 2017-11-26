#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>


def rod_cut(price,n):
	
	dp = [None for _ in range(n+1)]
	
	dp[0] = 0
	
	for j in range(1,n+1):
		
		q = -1
		
		for i in range(j):
			q = max(q, price[i] + dp[j-i-1])
		
		dp[j] = q
		
	return dp[n]
	
if __name__ == '__main__':
	arr = [1, 5, 8, 9, 10, 17, 17, 20]
	size = len(arr)
	print('Maximum obtainable value is',rod_cut(arr,size))

