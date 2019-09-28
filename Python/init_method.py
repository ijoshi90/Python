"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 11-Sep-19 at 20:26
"""

class Computer:
    def __init__(self, computer, processor, ram):
        print ("In __init__")
        globals()['a'] = "Akshay"
        self.computer = computer
        self.processor = processor
        self.ram = ram

    def configuration(self):
        print ("*** Configuration ***")
        print("Type : {}".format(self.computer))
        print("Processor : {}".format(self.processor))
        print("RAM : {}".format(self.ram))

com1 = Computer("Desktop", "i5", "1 x 8GB")
com2 = Computer("Laptop", "i7", "1 x 8GB")

com1.configuration()
print ("A : {}".format(a))
com2.configuration()