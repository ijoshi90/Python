# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:43:24 2019

@author: akjoshi
"""
# For loop
fruits=["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print (fruit)
    
for character in "String":
    print (character)
    
for x in range(5):
    print (x)
    
for x in range(22,10,-2): # Start, end, increment
    print (x)
else:
    print ("Finished the loop in else")
    
# Nested Loop
veggies=["Carrot","Beetroot","Beans"]

for fruit in fruits:
    for veg in veggies:
        print (fruit, veg)

string = "Akshay"
for i in string:
    print (i)