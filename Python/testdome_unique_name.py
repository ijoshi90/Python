"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 17-12-2019 at 10:31
"""

def unique_names(names1, names2):
    name_list = []
    for each in names1, names2:
        for name in each:
            if name in name_list:
                continue
            else:
                name_list.append(name)
    return name_list

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia