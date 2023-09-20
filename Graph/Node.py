"""
This class creates an object with the properties of each node.
"""


class Node:
    def __init__(self, name, color, mother_node):
        self.node_name = name
        self.node_color = color
        self.value = 0
        self.connections = []       # Fill with tuples with four values: The name of the connected node, whether the connected node is a parent/child/neutral, the weight of the connection and the direction of the connection
        self.mother_node = False    # Value to determine whether this node is the starting node/original node of the tree
        self.mother_node = mother_node

# Do we need return methods? I believe we can just access the properties of each node with "node.value" or "node.node_name" etc from the tree class, right?
