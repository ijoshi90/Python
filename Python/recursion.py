# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:11:11 2019

@author: akjoshi
"""

# Recursion example

import sys

print ("Recursion List Limit : " + str(sys.getrecursionlimit()))

sys.setrecursionlimit(1000)

print ("Recursion List Limit : " + str(sys.getrecursionlimit()))

i = 0

def greet():
    global i
    if (i<10):
        i += 1
        print ("Hello : {}".format(i))
        greet()
    
greet()
    