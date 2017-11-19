# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:30:24 2017

@author: chandu
"""

def insertion_sort(A):
    for j in range(1,len(A)):
        i = j - 1
        key = A[j]
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
        
def main():
    dummy_list = [8,6,5,4,3,2,1]
    print(dummy_list)
    insertion_sort(dummy_list)
    print("list after insertion sort",dummy_list,sep='\n')
    
    
if __name__ == '__main__':
    main()