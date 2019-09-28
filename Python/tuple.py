# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:29:10 2019

@author: akjoshi
"""

# Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print (thistuple[1])

for x in thistuple:
    print (x)
    
if "apple" in thistuple:
    print ("Apple is there")
    
print ("Lenght of tuple : "+str(len(thistuple)))

# Tuple creator
thistuple = tuple(("strawberry", "raspberry", "kiwi")) # note the double round-brackets
print(thistuple)

print(str(thistuple.count))
print (thistuple.index)