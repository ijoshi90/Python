"""
Author: Akshay Joshi
GitHub: https://github.com/ijoshi90
Creation Date: 22.10.24

Description: Test process with activity monitor
"""

from time import sleep

counter = 1
max = 1550
value = 1

while (True):
    if counter <= max:
        value *= counter
        #sleep (1)
        counter += 1
    else:
        break

    print("Counter : {}, Value : {}".format(counter, value))