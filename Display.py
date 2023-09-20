import time
import pygame


class Display:
    def __init__(self, window_width, window_height):
        self.screen = pygame.display.set_mode((window_width, window_height))

        # variables for 60fps loop
        self.frame_rate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frameCount = 0

    def display(self):
        # timing functions for constant fps
        self.elapsed_time = time.perf_counter() - self.previous_time
        if self.elapsed_time > 1 / self.frame_rate:
            self.previous_time = time.perf_counter()
            self.drawScreen()
            self.frameCount += 1

    def drawScreen(self):
        pass
