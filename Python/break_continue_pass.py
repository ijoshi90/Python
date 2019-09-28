# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:52:13 2019

@author: akjoshi
"""
# Break, Continue, Pass
fruits=["Apple", "Banana", "Cherry"]
for fruit in fruits:
    if fruit == "Banana":
        print ("Breaking at Banana")
        break
    print (fruit)

for fruit in fruits:
    if fruit == "Banana":
        print ("Continuing at Banana")
        continue
    print (fruit)
       
## Pass  
for i in range (20):
    if i%2 == 0:
        pass
        # Just an empty block, no condition, use pass
    else:
        print ("I is "+str(i))