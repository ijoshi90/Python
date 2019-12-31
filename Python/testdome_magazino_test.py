"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 20-12-2019 at 12:07
"""


# Jai Gurudeva Datta

class Node(object):

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def __repr__(self):
        return '<Node name={}>'.format(self.name)

    def extract_nodes_containing_string(self, needle):
        # TODO: Please implement me
        # needs to be case insensitive
        if needle is None:
            return needle
        return [needle]


def create_tree():
    return Node('root', [
        Node("MaGaZiNo", [
            Node("I"),
            Node("Love"),
            Node("magazino")
        ]),
        Node("Hello", [
            Node("Hello", [
                Node("Hello", [
                    Node("World")
                ])
            ])
        ])
    ])


root = create_tree()
print(root)
print(root.extract_nodes_containing_string('root') == [root])
