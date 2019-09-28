# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:24:42 2019

@author: akjoshi
"""

# Array new

from array import *

# i means unsigned
vals = array ('i',[5,2,5,6,-7,8])

print (vals)
print ("Buffer info : "+ str (vals.buffer_info()))
vals.reverse()
print (vals)
print (vals[0])

for i in range (len(vals)):
    print (vals[i])
    
# character type
chars = array ('u',['a','e','i','o','u'])
for ch in chars:
    print (ch)
    
# Unknown type
newArr = array (vals.typecode, [a for a in vals])
for i in newArr:
    print (i)