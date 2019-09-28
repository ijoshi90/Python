"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 12-Sep-19 at 17:12
"""
class New_Class:
    def __init__(self):
        self.name = "Akshay"
        self.age = "29"

c1 = New_Class()
c2 = New_Class()

# C2 overrides C1
c2.name = "Sangeetha"
c2.age = "28"

print("C1 - {} : {}".format(c1.name,c1.age))
print("C2 - {} : {}".format(c2.name,c2.age))
