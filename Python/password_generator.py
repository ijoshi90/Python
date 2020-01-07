"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 14:22
"""

# generate a password with length "passlen" with no duplicate characters in the password
from random import *

string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
password = "".join(sample(string,passlen))
print ("Generated Password : {}".format(password))