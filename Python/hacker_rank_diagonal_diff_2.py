"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 03-Nov-19 at 18:27
"""

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
from math import sqrt

def diagonalDifference(v):
    prim =0
    sec=0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(prim-sec)
arr = [11,2,4,
       4, 5, 6,
       10, 8, -12]

result = diagonalDifference(arr)
print (result)