"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 17-12-2019 at 14:43
"""

string = "Hello, World!"

# Strings as array
print (string[2])

# Slicing
print (string[2:5])
# Negative indexing - counts from the end
print (string[-5:-2])

# Replace
print (string.replace("!","#"))
print((string.replace("Hello", "Well Hello")))

#Split
print(string.split(","))

print(string)

# Join
print(",".join(string))
