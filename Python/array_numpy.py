# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:27:24 2019

@author: akjoshi
"""

# array_numpy

from numpy import *

arr1 = array (([1,2,3,4,5]), int)
arr2 = array (([1,2,3,4,5.6]))

print (arr1)
print (arr2)

print ("arr1 datatype " + str (arr1.dtype))
print ("arr2 datatype " + str (arr2.dtype))

# linspace
# start, end, parts
print ("\nLinspace")
lin_space = linspace (0,49) # By default it is divided to 50 parts
print (lin_space)

# 0 to 10 - divided in to 20 parts
lin_space = linspace (0,10,20)
print (lin_space)

# Arange

# start, end, steps
print ("\narange")
a_range = arange (1,10,2)
print (a_range)

# Logspace
# Start, end, log of parts
print ("\nLogspace")
log_space = logspace (1,40,5)
print (log_space)

for i in log_space:
    print ('%.2f' %i)

# Zeros - by default all values are 0
print ("\nZeros")
zeroes = zeros (5,int)
print (zeroes)
# Ones -  by default all values are 1
print ("\nOnes")
one = ones (5)
print (one)