"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 09-01-2020 at 09:57
"""

# Binary Search

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 30
low = 0
high = len(list)
found = False

while (low <= high and not found):
    mid = (low + high) // 2
    if list[mid] == key:
        found = True
    else:
        if key < list[mid]:
            high = mid - 1
        else:
            low = mid + 1

print(found)