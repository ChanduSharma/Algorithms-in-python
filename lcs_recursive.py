#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def lcs_recursive(x,y,i,j):
	
	if i == 0 or j == 0:
		return 0
	
	if x[i-1] == y[j-1]:
		return 1 + lcs_recursive(x,y,i-1,j-1)
	else:
		return max(lcs_recursive(x,y,i-1,j),lcs_recursive(x,y,i,j-1))
		

if __name__ == '__main__':
	x = 'ABCBDAB'
	y = 'BDCABA'
	
	print('x',x)
	print('y',y)
	print('The length of longest common sequence is',lcs_recursive(x,y,len(x),len(y)))
