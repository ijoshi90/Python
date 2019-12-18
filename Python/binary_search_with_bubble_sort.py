"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 11:11
"""

# Binary search

# Sort the array first
def bubble_sort_the_array(array):
    length = len(array)

    for i in range(length):  # Entire input array
        for j in range(0, length - i - 1):  # From 0th position to length - iteration - 1
            if array[j] > array[j + 1]:  # if element at j > element at j+1, swap them
                array[j], array[j + 1] = array[j + 1], array[j]
    return (array)


# Searching Function
def binary_search(arrray, key):
    low = 0
    high = len(arrray) - 1
    found = False

    while (low <= high and not found):
        mid = (low + high) // 2
        if array[mid] == key:
            found = True
        elif key < arrray[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return found


# Main
array = [1, 3, 8, 9, 2, 5, 2, 3, 6, 5, 8, 10, 19, 12, 14, 7, 20]
print("Original Array : {}".format(array))
key = 9
print("Key to Search : {}".format(key))
arrray = bubble_sort_the_array(array)  # Bubble sort the array
print("Sorted Array : {}".format(array))
result = binary_search(array, key)
print("End Result : {}".format(result))
