"""
This class will generate graphs containing the Node objects, based on the input of the user
"""


import random

from Graph.Node import Node
from Utilities.Enum_Variable import Enum_Variable


class Graph_Generator:
    def __init__(self):
        self.graph_depth = 5
        self.layer_size = 2

        self.range = 10

        self.red = (200, 50, 50)

    def generate_graph(self, graph_type):
        graph = []
        for layer in range(self.graph_depth):
            for node_count in range(layer * self.layer_size):
                name = [layer, node_count]
                value = random.randint(int(-self.range / 2), int(self.range / 2))
                connected_node = [layer - 1, node_count / self.layer_size]
                weight = random.randint(int(-self.range / 2), int(self.range / 2))
                connection = [connected_node, weight, "Child", "One-Way"]
                node = Node(name, self.red, value, False, connection)
                graph.append(node)
        return graph
