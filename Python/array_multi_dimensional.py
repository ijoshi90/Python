# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:37:51 2019

@author: akjoshi
"""

# Multi dimensional Array

from numpy import *

arr1 = array ((
        [1,2,3,4,5,6],
        [4,5,6,7,8,9]
        ))

print (arr1)

print ("Dimensionas : " + str(ndim(arr1)))
print ("Shape : " + str(shape(arr1)))
print ("Size : " + str(size(arr1)))

# Convert 2D Array to 1D Array
arr2 = arr1.flatten()

print ("Arr2 after flattening Arr1 : ")
print (arr2)

# Convert 1D to 3D Array - Single to 3D array
arr3 = arr2.reshape(2,2,3)
# Rows, Cols, No of elements
print ("Arr3 after reshaping arr2 :")
print (arr3)

arr4 = arr2.reshape(3,4)
# No of arrays, No of rows, No of elements
print ("Arr4 after reshaping arr2 :")
print (arr4)

arr5 = arr2.reshape(4,3)
# Rows, Cols, No of elements
print ("Arr5 after reshaping arr2 :")
print (arr5)