"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 14:14
"""

"""
class myClass:
    x = 5

mc1 = myClass()
print("Object value : ",format(mc1.x))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",29)
print(p1.name)
print(p1.age)

###

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc (self):
        print("Hello, my name is {} and I am {} years old".format(self.name,self.age))

person1 = Person ("Mr. X",35)
person1.myfunc()
person1.name = "Akshay Joshi"
person1.age = 29
person1.myfunc()

del person1
"""

class Person:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln

    def print_name (self):
        print("Name is {} {}".format(self.fn,self.ln))

class Student (Person):
    def __init__(self, fn, ln, year):
        Person.__init__(self, fn, ln)
        super().__init__(fn, ln)
        self.graduation = year

    def print(self):
        print("Candidates Graduation : {}".format(self.graduation))

person2 = Person("Akshay","Joshi")
person2.print_name()

student1 = Student("Akshay", "Joshi", 2011)
student1.print_name()
student1.print()