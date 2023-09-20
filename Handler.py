from Display import Display
from Enum_Variable import Enum_Variable


class Handler:
    def __init__(self, window_width, window_height):
        self.display = Display(window_width, window_height)

        self.interaction_type = Enum_Variable(["Instant", "Step-by-Step", "Auto-run"])
        self.interaction_type.set_state("Instant")

        self.interaction_step = 0  # Useful for when you want to show step by step how the algorithm works, probably needs to be used in the self.interact class

    def create_graph(self):
        pass

    def interact(self):
        pass

    def draw(self):
        self.display.display()
