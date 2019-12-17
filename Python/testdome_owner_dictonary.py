"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 17-12-2019 at 10:22
"""


def group_by_owners(files):
    values = []
    dictionary = {}

    for key,value in files.items():
        values.append(value)

    s_values = set(values)
    l_values = list(s_values)

    for i in l_values:
        keys = []
        for key,value in files.items():
            if value == i:
             keys.append(key)
        dictionary [i] =keys

    return dictionary


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))