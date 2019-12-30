# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:58:59 2019

@author: akjoshi
"""

# Fibonacci series

#number = int ( input ("Enter the number to generate fibonacci sequence : "))
#maxi = int ( input ("Enter the Max Range : "))
number = 20
maxi = 1000000000

base = 0
current = 1
series = str (base) + " " + str (current)
ser1=[]

ser1.append(base)
ser1.append(current)
# 0, 1, 1, 2, 3, 5, 8
if number == 0:
    series = "0 is not a valid number to print fibonacci"
    ser1 = series
    
elif number == 1:
    series = 0
    ser1 = [0]
else:
    for i in range (number - 2):
        new = base + current
        if new <= maxi:
            base = current
            current = new
            series = series + " " + str (new)
            ser1.append(new)
print ("Fibonacci series : " + str(series))
print ("Fibonacci List : {}".format(ser1))
