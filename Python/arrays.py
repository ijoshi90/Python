# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:35:33 2019

@author: akjoshi
"""

array=" Hello, world! "
print (array[1]) # nth element
print (array[2:5]) # n -> m

# Strip function - removes whitespaces from begin & end
print(array.strip())

# length function
print (len(array))

print (array.lower())
print (array.upper())
print (array.split(","))

# Format
age=29
name="AJ"
txt="My name is AJ, I am "  + str(age)
txt1="My name is {}, I am {}"
print (txt)
print ("Using format : " + txt1.format(name,age))

########################

cars = ["BMW","Mini","VW","Kia"]
print ("Length of array cars : "+str(len(cars)))

for each in cars:
    print (each)
    
cars.append("Honda")

for each in cars:
    print (each)
    
cars.pop (4)
cars.remove ("Kia")

print (cars)