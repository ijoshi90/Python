"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 26-Sep-19 at 19:24
"""

class Car:
    # Class variable
    wheels = 2

    def __init__(self):
        # Instance Variable
        self.mileage = 20
        self.company = "BMW"

car1 = Car()
car2 = Car()

print ("Wheels : {}".format(Car.wheels))
# Override the value of wheels with 4
Car.wheels = 4

print (car1.company, car1.mileage, car1.wheels)
print (car2.company, car2.mileage, car2.wheels)

# Changing values of Car 2
car2.company = "Mini"
car2.mileage = "25"
car2.wheels = "3"

print (car2.company, car2.mileage, car2.wheels)