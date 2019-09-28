# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:17:14 2019

@author: akjoshi
"""

# Factorial using Recursion
result = 1

def factorial(number):
    global result
    if number == 0:
        return 1
    return number * factorial (number-1)

number = 10
result = factorial(number)
print ("Factorial of {} is {}".format(number, result))