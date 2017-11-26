#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def lcs(x,y):
	m = len(x)
	n = len(y)
	dp = [ [None for i in range(n+1)] for j in range(m+1)]
	
	for i in range(m+1):
		dp[i][0] = 0
		
	for i in range(n+1):
		dp[0][i] = 0 
	
	for i in range(1,m+1):
		for j in range(1,n+1):
			
			if x[i-1] == y[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	
	return dp[m][n]

if __name__ == '__main__':
	x = 'ABCBDAB'
	y = 'BDCABA'
	
	print('x',x)
	print('y',y)
	print('The length of longest common sequence is',lcs(x,y))
