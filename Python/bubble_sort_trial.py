"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 09-01-2020 at 10:15
"""

list = [1, 3, 8, 9, 2, 5, 2, 3, 6, 5, 8, 10, 19, 12, 14, 7, 20]

def bubble (list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list [i] > list [j]:
                list [i], list [j] = list [j], list[i]

bubble(list)
print(list)