"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 20:33
"""

import datetime

file1 = open("SampleFile.txt","r")
print (file1.read())

print (datetime.datetime.now())
file1.write ("Time Now : ")
file1.write(format(datetime.datetime.now()))
print ()
file1.close()