"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 31-12-2019 at 09:04
"""

# Datastructures - Linked List in python

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Add element at beginning
    def AtBegining(self, newdata):
        NewNode = Node(newdata)

        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    # Function to add node in Between
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


# Removing an element from Linked List

list = SLinkedList()
list.headval = Node("First")
e2 = Node("Second")
e3 = Node("Fourth")

list.headval.nextval = e2
e2.nextval = e3

list.Inbetween(list.headval.nextval, "Third")

list.AtEnd("Fifth")

list.AtBegining("Zeroth")

list.listprint()
