import pygame

from Handler import Handler

windowWidth = 1000
windowHeight = 1000


class Main:
    def __init__(self):
        self.runBool = True
        pygame.init()

        self.handler = Handler()

    def run(self):
        """
        Main update loop, gets run every frame
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runBool = False
            self.call()

    def call(self):
        """
        Method that calls the methods from other classes and handles the interaction
        """
        self.handler.create_graph()
        self.handler.interact()
        self.handler.draw()


# Starts and runs the game
if __name__ == "__main__":
    theMain = Main()
    theMain.run()