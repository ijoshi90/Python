# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:29:06 2019

@author: akjoshi
"""

# Functions
    
def identity(fname="Akshay"):
    print (fname+" Message")

identity()        
identity("Joshi")

#---------------

def addition(a,b):
    return a + b

print ("A + B = " + str(addition(2,3)))
print ("A + B = " + str(addition(4,7)))
print ("A + B = " + str(addition(5,9)))

#------------ Passing List
my_list = ["BMW","X1","2020","Silver"]

def print_it (car_list):
    for each in car_list:
        print (each)

print_it (my_list)
################


# Function Recursion
def fun_recursion(number):
    if number > 0:
        print ("IF : " + str(number))
        number -= 1
        fun_recursion (number)
    else:
        print ("Else : " + str (number))
        
fun_recursion (5)

####### Lambda function - ONLY ONE Expression
x = lambda a : a * 10
print (x(5))

y = lambda a , b : a / b
print (y(4,6))

z = lambda a,b,c : a + b - c
print (z(3,4,5))