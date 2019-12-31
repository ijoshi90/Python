# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:20:39 2019

@author: akjoshi
"""

# Selection sort

# Selection Sort

A = [64, 25, 12, 22, 11, 2, 5, 1, 2, 99, 21, 0]
print (A)

# Traverse through all array elements 
for i in range(len(A)): 
    # Find the minimum element in remaining unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print (A[i], end= " ")