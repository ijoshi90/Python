"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 08-01-2020 at 22:15
"""

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]

def unique_names(names1, names2):
    return set(names1 + names2)


print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia in any order