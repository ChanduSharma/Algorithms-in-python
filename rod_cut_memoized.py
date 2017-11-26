#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def rod_cut_aux(price,n,dp):
	
	if dp[n] is not None:
		return dp[n]
	
	if n == 0:
		q = 0
	else:
		q = -1
		for i in range(0,n):
			q = max(q,price[i] + rod_cut_aux(price,n-i-1,dp))
	
	dp[n] = q
	return q


def rod_cut_memoized(price,n):
	
	dp = [None for _ in range(n+1)]
	
	return rod_cut_aux(price,n,dp)

if __name__ == '__main__':
	arr = [1, 5, 8, 9, 10, 17, 17, 20]
	size = len(arr)
	print('Maximum obtainable value is',rod_cut_memoized(arr,size))
