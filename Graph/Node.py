"""
This class creates an object with the properties of each node.
"""


class Node:
    def __init__(self, name, color, value, mother_node, connection):
        self.node_name = name
        self.node_color = color
        self.value = value
        self.connections = []       # Fill with tuples with four values: The name of the connected node, whether the connected node is a parent/child/neutral, the weight of the connection and the direction of the connection
        self.connections.append(connection)
        self.coordinate = [0, 0]
        self.mother_node = False    # Value to determine whether this node is the starting node/original node of the tree
        self.mother_node = mother_node

    def add_coordinate(self, coordinate_x, coordinate_y):
        self.coordinate = [coordinate_x, coordinate_y]

    def return_name(self):
        return self.node_name

    def return_color(self):
        return self.node_color

    def return_value(self):
        return self.value

    def return_coordinate(self):
        return self.coordinate

# Do we need return methods? I believe we can just access the properties of each node with "node.value" or "node.node_name" etc from the tree class, right?
