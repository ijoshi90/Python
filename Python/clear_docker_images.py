"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 01-01-2020 at 14:49
"""

import os

command = "docker rm $(docker ps -a -f status=exited -q) > /dev/null 2>&1"

output = os.system(command)

if output != 0:
    print ("No image to clear")
else:
    print ("Cleared")