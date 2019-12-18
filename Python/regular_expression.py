"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 18:08
"""

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print (x)