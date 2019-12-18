# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:40:20 2019

@author: akjoshi
"""

# Set Example
thisset = {"1 apple", "2 banana", "3 cherry","4 kiwi"}
print(thisset)

for i in thisset:
    print (i)
    
print ("5 banana" in thisset)
print ("2 banana" in thisset)

thisset.add("5 Strawberry")
print (thisset)

thisset.update(["6 Raspberry","7 Blueberry"])
print (thisset)

print ("Set length : "+str(len(thisset)))

# Remove will raise error if item is not there
thisset.remove("7 Blueberry")
print (thisset)

# Discard will not raise error if item is not there
thisset.discard("4 kiwi")
print(thisset)

# Pop removes last item
x=thisset.pop()
print (x)
print (thisset)

# Del deletes the set completely
del (thisset)
#print (thisset)

# Set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)