# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:51:11 2019

@author: akjoshi
5"""

# Factorial of a number
n = int (input ("Enter the number : "))
fact = 1

for i in range (2,n+1):
    print ("Factorial of {} is {}".format(i-1,fact))
    fact *= i

print ("Factorial of " + str(n) + " is : "+ str(fact))