"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 31-12-2019 at 08:06
"""

# Data Structures - Stacks using Python
class Stack:
    def __init__(self):
        self.stack = []

    # Adding Data
    def push(self, data):
        # Unique, repeated elements will not be added
        #if data not in self.stack:
        #    self.stack.append(data)
        #    return True
        #else:
        #    return False
        self.stack.append(data)
    # Look at the top of the stack
    def peek(self):
        return self.stack[-1]

    # Pop stack element
    def pop(self):
        if len(self.stack) <= 0:
            return False
        else:
            return self.stack.pop()

    # Print stack elements
    def printstack(self):
        print("Now stack is")
        for each in stack.stack[::-1]:
            print(each)

stack = Stack()
stack.push("First")
stack.push("First")
stack.push("Second")
stack.push("Third")
stack.push("Fourth")

stack.printstack()

print("Pushing Fifth")
stack.push("Fifth")


print("Element at Top : {}".format(stack.peek()))

print("Popped Element : {}".format(stack.pop()))

stack.printstack()