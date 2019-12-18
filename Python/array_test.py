"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 14:08
"""

cars = ["BMW","Mini","Rolls Royce"]

print (cars[0])
cars[0] = "Mini"
print (cars[0])
cars[1] = "BMW"
print (cars[1])

cars.append("Audi")
cars.remove("Audi")

for each in cars:
    print (each)
