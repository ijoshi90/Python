# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:05:23 2019

@author: akjoshi
"""

# Prime Number
#num = int (input ("Enter the number : "))
num = 10
print ("Prime Numbers in the given range are")

if num > 1:
    for i in range (2,num):
        if (num % i) == 0:
            print (i,"is NOT prime")
        else:
            print (i,"is prime")
else:
    print ("1 is not a prime number")