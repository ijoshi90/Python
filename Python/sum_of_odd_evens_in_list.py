# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:40:50 2019

@author: akjoshi
"""

# Count sum of off and even numbers in list
from random import *

odd = 0
even = 0

odd_total=0
even_total=0

odd_list=[]
even_list=[]

def odd_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
            globals()['even'] += i
            globals()['even_total'] += 1
        else:
            odd_list.append(i)
            globals()['odd'] += i
            globals()['odd_total'] += 1

numbers = []
iteration=0

while True:
    iteration += 1
    for i in range (100):
        numbers=[]
        numbers.append(randrange(0,100,1))
    odd_even(numbers)
    
#    print ("Even : {}\nOdd : {}".format(even_total, odd_total))
    
    if (even_total or odd_total) == 50:
        break
    else:
        continue
    
print ("Iteration : " + str(iteration))
print ("\nOdd List : " + str(odd_list))
print ("\nOdd Sum : " + str (odd))
print ("\nOdd Total : " + str (odd_total))
print ("\nEven List : " + str(even_list))
print ("\nEven Sum : " + str (even))
print ("\nEven Total : " + str (even_total))