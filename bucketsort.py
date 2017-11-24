#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
#  Copyright 2017 Chandu <chandu@chandu-HP-Pavilion-g6-Notebook-PC>

def bucketsort(arr):
	
	n = len(arr)
	
	b = [list() for i in range(n)]
	
	for i in range(n):
		index = int(n*arr[i])
		b[index].append(arr[i])
	
	for i in range(n):
		b[i].sort()
	
	index = 0
	for i in range(n):
		for j in range(len(b[i])):
			arr[index] = b[i][j]
			index += 1


if __name__ == '__main__':
	arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
	print('before sorting')
	print(*arr)
	bucketsort(arr)
	print('After sorting')
	print(*arr)
