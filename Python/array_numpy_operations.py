# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:00:38 2019

@author: akjoshi
"""
from numpy import *
# Array - numpy operations
arr = array (([1,2,3,4,5]))
arr1 = array (([6,7,8]))
arr += 5

print (arr)

print (sin(arr))
print (sin(arr)/cos(arr))
print (cos(arr))
print (tan(arr))

print (sum(arr))
print (sort(arr))

print (concatenate([arr, arr1]))

# Shallow Copy
arr2 = arr.view()
arr3 = arr

# Deep Copy
arr4 = arr.copy()
# Shallow copy, deep copy

# Address is new when function view is used, else it remains same
print ("Address of arr2 : " + (str(id(arr2))))
print ("Address of arr : " + (str(id(arr))))