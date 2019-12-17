# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:17:24 2019

@author: akjoshi
"""

#lists

thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[2]) # Print n element

thislist[1] = "blackcurrant" # Change value of n element
print(thislist)

# Looping through list
for x in thislist:
    print (x)
   
key="cherry"
if key in thislist:
    print (key + " is there")

print(len(thislist))
print ("Length of thislist : "+str(len(thislist)))

thislist.append("orange") # Add items to the end
print (thislist)

thislist.insert(1,"strawberry") # Inster at specific position
print (thislist)

thislist.remove ("apple") # Remove specified element
print (thislist)

thislist.pop(1) # Removes specified index, else last one
print(thislist)

del thislist[1] # Deletes the specified index
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
print (thislist)
thislist.clear() # Clears the list
print (thislist)

thislist = ["apple", "banana", "cherry"]
mylist=thislist.copy() # Copy of the list
mynewlist=list(thislist)
print(mylist)
print (mynewlist)

newlist=list(("app","da","ba","ca"))
print(newlist)

newlist.reverse()
print (newlist)
newlist.sort()
print (newlist)

newlist.pop()
#mynewlist.remove("")

# Negative Index
athislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Negative Index")
print(athislist[-5:-1])