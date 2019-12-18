"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 10:35
"""

maximum = 10
minimum = 1

def recursion (number):
    if number <= maximum:
        print("Iteration at : {}".format(number))
        recursion(number+1)
    else:
        print("End of recursion at : {}".format(number))
        return 0

number = int(input("Enter a number between 1 and 10 : "))
if number >= minimum and number <= maximum:
    print("Input validated..")
    recursion(number)
else:
    print("Invalid Inut")
    exit (1)