# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:30:52 2019

@author: akjoshi
"""

from array import *

# Reverse an array

array1 = array ('i',[1,2,3,4,5])
array2 = array ('i',[])
array3 = array ('i',[])
l = len(array1)
    
for j in range (l,0,-1):
    array3.append(j)

print (array1)
print (array3)