"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 31-12-2019 at 08:32
"""

# Data Structures - Queue in Python

class Queue:
    def __init__(self):
        self.queue = list()

    # Insert method to add element
    def insert(self,dataval):
        self.queue.insert(0,dataval)

    # Size of Queue
    def size(self):
        return len(self.queue)

    # Print the queue
    def printq(self):
        print("Queue Contents")
        for each in self.queue[::-1]:
            print(each)

    # Remove element from queue
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return False

queue1 = Queue()
queue1.insert("1 First")
queue1.insert("2 Second")
queue1.insert("3 Third")
print("Size of Queue : {}".format(queue1.size()))
queue1.printq()

print("Popped Element : {}".format(queue1.remove()))

queue1.insert("1 First")

queue1.printq()