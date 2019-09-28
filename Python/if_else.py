# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:51:54 2019

@author: akjoshi
"""

# If else example

a=10
b=20
c=9
D=5

if a < b:
    print ("A < B")
elif a == c:
    print ("A = C")
elif a > d:
    print ("A > D")
else:
    print ("None of the above")
    
# Short hand IF
    
if (a > b): print ("A > B")

# Short hand if else
print ("A > B") if (a > b) else print ("A !> B")

print("A") if a > b else print("=") if a == b else print("B")

if a > b and c > a:
    print("Both conditions are True")
  
if a > b or a > c:
    print("At least one of the conditions is True")