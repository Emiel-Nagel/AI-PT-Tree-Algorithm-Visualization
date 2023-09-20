from Display import Display


class Handler:
    def __init__(self):
        self.display = Display()

    def create_graph(self):
        pass

    def interact(self):
        pass

    def draw(self):
        self.display.display()
