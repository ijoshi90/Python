# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:13:26 2019

@author: akjoshi
"""

# Linear Search

series = input ("Enter the series in space separated format : ")
key = input ("Enter the key to search : ")

for element in series:
    if element == key:
        print (key + " is found in series")
        break
else:
    print ("Did not find the " + key + " in series")