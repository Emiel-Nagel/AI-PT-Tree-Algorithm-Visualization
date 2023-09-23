"""
This class is an intermediate layer between main and the rest of the code and handles all the interactions between the classes.
"""


from Interaction.Display import Display
from Interaction.Keyboard import Keyboard
from Graph.Graph_Generator import Graph_Generator
from Graph.Graph_Coordinator import Graph_Coordinator
from Utilities.Enum_Variable import Enum_Variable


class Handler:
    def __init__(self, window_width, window_height):
        self.display = Display(window_width, window_height)
        self.keyboard = Keyboard()
        self.generator = Graph_Generator()
        self.coordinator = Graph_Coordinator(window_width, window_height)

        self.reset = True

        self.interaction_type = Enum_Variable(["Instant", "Step-by-Step", "Auto-run"])
        self.interaction_type.set_state("Step-by-Step")
        self.graph_type = Enum_Variable(["Simple_Tree", "Simple_Web", "Maze"])
        self.graph_type.set_state("Simple_Tree")

        self.interaction_step = 0  # Useful for when you want to show step by step how the algorithm works, probably needs to be used in the self.interact class

        # for startup
        self.display.reset_screen()
        self.display.draw_text([self.graph_type.return_state(), self.interaction_type.return_state(), str(self.interaction_step)])

    def create_graph(self):
        """
        This method will call to create a new graph
        """
        if self.reset:
            graph = self.generator.generate_graph(self.graph_type.return_state())
            print(graph)
            graph = self.coordinator.coordinate_graph(self.graph_type.return_state(), graph)
            print(graph)
            self.display.update_graph(graph)
        self.reset = False

    def interact(self):
        """
        This method will handle all the interaction that happens between the user and the computer
        """
        self.check_key_pressed()

    def check_key_pressed(self):
        """
        This method handles the interaction with the keyboard
        Space   = 44  Backspace = 42    Enter = 40
        """
        if 44 in self.keyboard.return_key():
            self.interaction_step += 1
            self.display.draw_text([self.graph_type.return_state(), self.interaction_type.return_state(), str(self.interaction_step)])
        if 42 in self.keyboard.return_key():
            self.interaction_step -= 1
            self.display.draw_text([self.graph_type.return_state(), self.interaction_type.return_state(), str(self.interaction_step)])
        if 40 in self.keyboard.return_key():
            self.reset = True

    def draw(self):
        """
        This method will call to display the program in a window
        """
        #self.display.display(self.interaction_type.return_state(), str(self.interaction_step))

