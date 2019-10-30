# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:21:20 2019

@author: akjoshi
"""

from array import *

arr = array('i', [])

l = int (input ("Enter the length : "))

print ("Enter elements")

for i in range (l):
    x = int (input("Enter the " + str (i) + " value : "))
    arr.append(x)

key = int (input ("Enter value to search : "))

for i in range (l):
    if key == arr[i]:
        print (str(key) + " is in position " + str(i))
else:
    print ("element is not in array")
    
print (arr.index(key))

# Sum of Array
new_arr = [1,2,3,4,5,6,7,8,9,10]
print(max(new_arr))