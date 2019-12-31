"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 20-12-2019 at 11:35
"""

names1 = ["Ava", "Emma", "Olivia","Joshi","Sangeetha"]
names2 = ["Olivia", "Sophia", "Emma","Akshay","Joshi"]

def unique_names (names1, names2):
    return list(set(names1 + names2))

print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia