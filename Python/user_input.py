# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:55:32 2019

@author: akjoshi
"""
import sys

# User Input
def read_name_age():
    name = input("Enter the Name : ")
    # By default input format is string, for arithmetic operations, needs conversion
    age = int (input ("Enter Age : ")[0]) # Reads all numbers, saves only first
    print ("Hello, " + name)
    age += 1
    print ("Your age next year : " + str (age))


#### Eval ####
def eval_expr():
    expr = eval (input ("Enter expression : "))
    print ("Evaluation result: " + str (expr))
    
    
### ARGV - Command Line arguments
def argv_():
    num1 = sys.argv [1]
    num2 = sys.argv [2]
    print (num1 + " + " + num2)
### Main

#read_name_age()    
#eval_expr()
#argv_() - Call in command line with 2 numbers
