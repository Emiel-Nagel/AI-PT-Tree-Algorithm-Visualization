import time


class Display:
    def __init__(self):
        # variables for 60fps loop
        self.frameRate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frameCount = 0

    def display(self):
        # timing functions for constant fps
        self.elapsed_time = time.perf_counter() - self.previous_time
        if self.elapsed_time > 1 / self.frameRate:
            self.previous_time = time.perf_counter()
            # draw loop
            self.drawScreen()
            self.frameCount += 1

    def drawScreen(self):
        pass
