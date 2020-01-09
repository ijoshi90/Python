# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:17:29 2019

@author: akjoshi
"""
import time

# Print Pattern

#number = int (input ("Enter a number : "))
number = 10
for it1 in range (number):
    for it2 in range (it1+1):
        print (it2+1, end="")
        #time.sleep(1)
    print ()

for it1 in range (number):
    for it2 in range (number-it1-1):
        print (it2+1, end="")
        #time.sleep(1)
    print ()
