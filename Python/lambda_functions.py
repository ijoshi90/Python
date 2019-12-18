# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:30:58 2019

@author: akjoshi
"""

# Lambda Functions (Anonymous Functions)
# Must be on expression

sqr = lambda a : a*a
add = lambda b,c : b + c

print ("Lambda Square : " + str(sqr(5)))
print ("Lambda add : " + str(add(5,6)))

def myfun (n):
    return lambda b : b * n

mytripler = myfun(2)

print("My Tripler Lambda : {}".format(mytripler(11)))