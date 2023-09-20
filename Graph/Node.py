"""
This class creates an object with the properties of each node.
"""


class Node:
    def __init__(self, name, color):
        self.node_name = name
        self.node_color = color
        self.value = 0
        self.connections = []
