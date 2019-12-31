"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 20-12-2019 at 11:08
"""

array = [4,1,7,2,9,8,3,6,5,0]
print("Original Array : {}".format(array))

for i in range (len(array)):
    minimum_index = i
    for j in range (i + 1, len(array)):
        if array [minimum_index] > array [j]:
            minimum_index = j
    array [i], array [minimum_index] = array [minimum_index], array [i]

print("Sorted Array : {}".format(array))