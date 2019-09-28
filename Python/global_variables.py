# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:19:01 2019

@author: akjoshi
"""
a=10
b=15
c=25

print ("A is : " + str(a))
print ("B is : " + str(b))
print ("C is : " + str(c))
print ("ID of C : " + str(id(c)))

def change_value(*nums):
    a=5
    global b # Make the variable global
    b=20
    
    x = globals()['c'] # Gets the address of c
    print ("ID of x : " + str(id(x)))
    
    print ("A in function : " + str(a))
    print ("B in function : " + str(b))
    
    globals()['c'] = 30

change_value()
print ("A outside function : " + str(a))
print ("B outside function : " + str(b))
print ("C after changing using globals() : " + str(c))