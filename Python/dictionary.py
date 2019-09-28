# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:05:09 2019

@author: akjoshi
"""

#dictionary

dictionary_car = {
        "Brand" : "BMW",
        "Model" : "X1",
        "Year" : "2020",
        "Owner" : "Sanaksh"
        }

print (dictionary_car)

# Accessing
this_dictionary = dictionary_car["Model"]
print (this_dictionary)
print (dictionary_car["Year"])

print (dictionary_car.get("Owner"))

dictionary_car["Owner"]="Adi Shankara"
print (dictionary_car.get("Owner"))

for x in dictionary_car:
    print (x + " : " +dictionary_car[x])
    
for x in dictionary_car.values():
    print (x)
    
for x, y in dictionary_car.items():
    print (x, y)
    
if "Brand" in dictionary_car:
    print ("Brand is present")
    
if "BMW" in dictionary_car.values():
    print ("BMW is there")
    
print ("Length of dictionary : "+str(len(dictionary_car)))

# Adding to dictionary
dictionary_car["Type"]="Petrol"
print (dictionary_car)

# Removing from dictionary
dictionary_car.pop("Year")
print (dictionary_car)

# del
del dictionary_car["Model"]
print (dictionary_car)

# Copying a dictionary
new_dictionary=dictionary_car.copy()
print (new_dictionary)
new_dictionary=dict(dictionary_car)
print (new_dictionary)

dictionary_car.clear()
print (dictionary_car)

# Copying a dictionary
new_dictionary=dictionary_car.copy()
print (new_dictionary)

del dictionary_car

# dict() : Constructor
dictionary = dict(brand="BMW",model="3 Series")
print (dictionary)