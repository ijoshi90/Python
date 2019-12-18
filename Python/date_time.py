"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 15:42
"""

# Python date and time functions

#import datetime
from datetime import *

#x = datetime.datetime.now()
#
print("Current Date and Time : {}".format(datetime.now()))

#strftime method
print(datetime.now().strftime("%A")) # Prints day
print(datetime.now().date()) # Prints only date
print(datetime.now().isoformat()) # ISO format
print(datetime.now().timestamp()) # Time stamp
print("Split across")
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day) # Prints only date
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)