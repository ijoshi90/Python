# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:32:53 2019

@author: akjoshi
"""

# for else

nums = [1,2,3,4,6,7,8,9,11,12,13,14]

for num in nums:
    if num % 5 == 0:
        print ("{} is divisible by 5".format(num))
        break
# this else is for "for loop"
else:
    print ("No number divisible by 5")