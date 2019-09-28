# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:40:46 2019

@author: akjoshi
"""

# Prime or not

number = int (input ("Enter a number to print prime numbers between 0 and number : "))

for num in range(2,number + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)