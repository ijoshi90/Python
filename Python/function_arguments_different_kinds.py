# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:28:56 2019

@author: akjoshi
"""

# Functions
def greet ():
    print ("\nGreet Function")

# Positional Arguments
def multiplication(a,b):
    print ("\nPositional Arguments")
    greet()
    return (a * b)

# Default Arguments
def default_values(name='A', age=20):
    print("Default Values function")
    print ("Name : " + name)
    print ("Default age : " + str (age))
    
# Keyword Arguments
def keyword_arguments(name, age):
    print ("\nKeyword Arguments")
    print ("Name : " + name)
    print ("Age : " + str(age))
    
def variable_length_argument (*num):
    # Makes use of tuple
    print ("Variable Length Argument Function")
    print ("Adding all the number")
    
    result=0
    for i in num:
        result += i
    print ("Sum of " + str (num) + " : " + str (result))
    
def kwargs(name, **data):
    # Passing multiple arguments with the help of **
    print ("Function kwargs")
    print ("Keyword Variable Length Arguments")
    print ("Name : " + name)
    print (data)
    for i,j in data.items():
        print (str(i) + " : " + str(j))
    
    
def call_functions():
    print(multiplication(3,4)) # Positional Arguments
    
    keyword_arguments(age=29,name="Akshay") # Keyword Arguments
    
    default_values ()
    default_values (age=30,name="AJ")
    
    variable_length_argument()
    variable_length_argument(1,2)
    variable_length_argument(3,4,6,8.7,0.4)
    
    print ("**kwargs")
    kwargs("Joshi", age=28, city="Berlin", phone="+49 175 922 5040")
    
call_functions()