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

        # fonts
        self.font_size = 40
        self.font = pygame.font.SysFont('arialbold', self.font_size)

        # color variables
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (100, 100, 100)
        self.red = (200, 50, 50)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.background = (40, 20, 30)

    def display(self, interaction_type, interaction_step):
        # timing functions for constant fps
        self.elapsed_time = time.perf_counter() - self.previous_time
        if self.elapsed_time > 1 / self.frame_rate:
            self.previous_time = time.perf_counter()
            self.drawScreen(interaction_type, interaction_step)
            self.frameCount += 1

    def drawScreen(self, interaction_type, interaction_step):
        self.screen.fill(self.background)

        text = "Interaction Type: " + interaction_type + "          Step: " + interaction_step
        text_display = self.font.render(text, True, self.white)
        text_rect = text_display.get_rect()
        text_left_border = len(text) * self.font_size * 0.18
        text_rect.center = (text_left_border, self.font_size)
        self.screen.blit(text_display, text_rect)

        pygame.draw.circle(self.screen, self.red, (self.screen.get_width() / 2, self.screen.get_height() / 2), 400, 10)
        pygame.display.update()
