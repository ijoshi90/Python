"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 26-Sep-19 at 18:28
"""


class Computer:
    def config(self, *a):
        print("Configuration : {}".format(a))
        print("Class Computer : def config")

com1 = Computer()
com2 = Computer()
com3 = Computer()

# Calling function
print("Computer.config(com1)")
Computer.config(com1)

# This is used in large
print("com2.config()")
com2.config("i7")

com3.config("i7, 16GB Memory, 2GB Graphics")