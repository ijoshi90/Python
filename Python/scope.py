"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 15:27
"""


# Scope - Locals
def myfunc():
    x = 300
    print(x)


myfunc()


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()


# Global

y = 400
def myfunc():
    global y
    y = 700

myfunc()
print(y)
