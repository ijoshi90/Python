"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 17:06
"""

import json

file = open("birthdays.json","r")
data = file.read()

json_data = json.loads(data)
print("Json file contents type : {}".format(type(json_data)))
print(json_data)