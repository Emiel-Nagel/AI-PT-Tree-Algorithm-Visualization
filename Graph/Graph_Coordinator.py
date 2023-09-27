from Graph.Node import Node

class Graph_Coordinator:
    def __init__(self, window_width, window_height):
        self.node_separation_horizontal = window_width / 100
        self.node_separation_vertical = window_height / 5
        self.margin_top = window_height / 20
        self.margin_horizontal = window_width / 5
        self.graph_width = window_width - self.margin_horizontal

    def coordinate_graph(self, graph_type, graph):
        if graph_type == "Simple_Tree":
            for node in enumerate(graph):
                layer, node_count = node[1].return_name()
                node_count += 1
                print(layer)
                print(node_count)
                # coordinate_x = (self.graph_width / layer) * node_count + (self.margin_horizontal / 2)
                # coordinate_x = node_count / (layer * 2) + 1 / (layer * 8)
                coordinate_x = (node_count + (node_count - 1)) / pow(2, layer) * self.graph_width + (self.margin_horizontal / 2)
                print(coordinate_x)
                coordinate_y = layer * self.node_separation_vertical + self.margin_top
                node[1].add_coordinate(coordinate_x, coordinate_y)
        return graph
