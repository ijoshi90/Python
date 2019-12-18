"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 18:34
"""

def print_number(number):
    try:
        print("In try block")
        if (number >= 0):
            print(number)

    except NameError:
        print ("In Exception : Name Error")

    except:
        print ("Exception has occured")
        print (type(number))

    finally:
        print("Finally, executes everytime")

print_number(1)
print_number("str")

def try_name_except():
    try:
        print(x)
    except NameError:
        print ("Name Error Exception")
        print (Exception)

try_name_except()

### Raise Exception
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")