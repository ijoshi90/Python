"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 30-Oct-19 at 08:15
"""

arr = [2,1,4,5,3]

def miniMaxSum(arr):
    arr.sort()
    #print (arr)
    res = sum(arr)
    print (res - (arr[(len(arr)-1)]),end=" ")
    arr.reverse()
    #print (arr)
    print(res - (arr[(len(arr) - 1)]))
miniMaxSum(arr)