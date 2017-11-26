#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def lcs_aux(x,y,i,j,dp):
	
	if dp[i][j] is not None:
		return dp[i][j]
	
	if i == 0 or j == 0:
		return 0
	
	if x[i-1] == y[j-1]:
		dp[i][j] = 1 + lcs_aux(x,y,i-1,j-1,dp)
	else:
		dp[i][j] = max(lcs_aux(x,y,i-1,j,dp),lcs_aux(x,y,i,j-1,dp))
	
	return dp[i][j]

def lcs_memoized(x,y):
	m = len(x)
	n = len(y)
	dp = [ [None for i in range(n+1)] for j in range(m+1)]

	return lcs_aux(x,y,m,n,dp)
	

if __name__ == '__main__':
	x = "ABCBDABE"
	y = "BDCABAEF"
	
	print('x',x)
	print('y',y)
	print('The length of longest common sequence is',lcs_memoized(x,y))
