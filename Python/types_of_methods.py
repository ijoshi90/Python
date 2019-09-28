"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 26-Sep-19 at 19:37
"""
"""
# Types of Methods
instance method
class method
static method

Accessors - access the value
Mutators - modify the value
"""

class Student:
    school = "AIT"
    def __init__(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    # Instance Method
    def average (self):
        print ("Instance Method")
        return (self.marks1 + self.marks2 + self.marks3) / 3

    def get_m1(self):
        return self.marks1

    def set_m2(self,value):
        self.marks2 = value

    # Class Method
    @classmethod # Decorator
    def getSchoolName(cls):
        print ("Class Method")
        return cls.school

    # Static Method - no self
    @staticmethod
    def info():
        print ("Static method")
        print("This is student class")

# Class method called
print ("School : {}".format(Student.getSchoolName()))

# Instance method called
s1 = Student(100,99,98)
print ("S1 Avg : {}".format(s1.average()))

s2 = Student(97,96,95)
print ("S2 Avg : {}".format(s2.average()))

print ("M1 : {}".format(s1.get_m1()))

# Static method called
Student.info()