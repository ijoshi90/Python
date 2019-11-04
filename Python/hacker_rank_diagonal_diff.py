"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 03-Nov-19 at 18:27
"""

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#from numpy import *
from math import sqrt

def diagonalDifference(arr):
    dia_1 = 0
    dia_2 = 0

    # Get the square root of matrix for length of matrix
    skip = int(sqrt(len(arr)))

    # Skip the sqrt (len) + 1 and add
    for i in range (0,len(arr),skip+1):
        #print("{} ".format(i),end=" ")
        dia_1 += arr[i]
    #print ("Dia 1 : {} ".format(dia_1))

    # Start from sqrt(len) -1 till last one
    for j in range (skip-1, len(arr)-(skip-1),skip-1):
        #print("{} ".format(j),end=" ")
        dia_2 += arr[j]
    #print ("Dia 2 : {} ".format(dia_2))

    return abs(dia_1 - dia_2)
"""
#arr = array (([
1,2,3,4,5,
                6,7,8,9,10,
                11,12,13,14,15,
                16,17,18,19,20
                ]), int)
"""
arr = [11,2,4,
       4, 5, 6,
       10, 8, -12]
print (arr)

result = diagonalDifference(arr)
print (result)