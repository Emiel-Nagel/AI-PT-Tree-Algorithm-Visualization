"""
This class is an intermediate layer between main and the rest of the code and handles all the interactions between the classes.
"""


from Interaction.Display import Display
from Utilities.Enum_Variable import Enum_Variable


class Handler:
    def __init__(self, window_width, window_height):
        self.display = Display(window_width, window_height)

        self.interaction_type = Enum_Variable(["Instant", "Step-by-Step", "Auto-run"])
        self.interaction_type.set_state("Step-by-Step")

        self.interaction_step = 1  # Useful for when you want to show step by step how the algorithm works, probably needs to be used in the self.interact class

    def create_graph(self):
        """
        This method will call to create a new graph
        """
        pass

    def interact(self):
        """
        This method will handle all the interaction that happens between the user and the computer
        """
        pass

    def draw(self):
        """
        This method will call to display the program in a window
        """
        self.display.display(self.interaction_type.return_state(), str(self.interaction_step))
