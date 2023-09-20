import pygame

windowWidth = 1000
windowHeight = 1000


class Main:
    def __init__(self):
        self.runBool = True
        pygame.init()

    def run(self):
        """
        Main update loop, gets run every frame
        """

        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runBool = False
                    sys.exit()

            # timing functions for constant fps
            self.elapsed_time = time.perf_counter() - self.previous_time
            if self.elapsed_time > 1 / self.frameRate:
                self.previous_time = time.perf_counter()
                # draw loop
                self.draw()
                self.frameCount += 1




# Starts and runs the game
if __name__ == "__main__":
    theMain = Main()
    theMain.run()