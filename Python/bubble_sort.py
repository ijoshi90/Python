# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:40:03 2019

@author: akjoshi
"""

# Bubble sort

array = [1,5,2,3,0,1,5,2,6]

print ("Unsorted array : {}".format((array)))

def bubble_sort(array):
    length = len (array)
    
    # Go through all array elements
    for i in range (length):
        # Last i elements are in place
        for j in range (0, length-i-1):
            # Traverse till length-i-1 and swap the elements if its found > next element
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array [j]
                
bubble_sort (array)
print ("Sorted array : {}".format(array))