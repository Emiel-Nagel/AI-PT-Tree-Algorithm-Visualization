"""
This class displays everything that needs to be displayed.
"""


import time
import pygame


class Display:
    def __init__(self, window_width, window_height):
        self.screen = pygame.display.set_mode((window_width, window_height))

        # variables for 60fps loop
        self.frame_rate = 60
        self.previous_time = time.perf_counter()
        self.elapsed_time = 0
        self.frame_count = 0

        # fonts
        self.font_size = 40
        self.font = pygame.font.SysFont('arialbold', self.font_size)

        # text variables
        self.text_left_border = 20
        self.text_top_border = 20
        self.text_horizontal_separation = self.font_size

        # color variables
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (100, 100, 100)
        self.red = (200, 50, 50)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.background = (40, 20, 30)

    def display(self, interaction_type, interaction_step):
        """
        This method will display the program and update with 60 fps
        """
        # timing functions for constant fps
        self.elapsed_time = time.perf_counter() - self.previous_time
        if self.elapsed_time > 1 / self.frame_rate:
            self.previous_time = time.perf_counter()
            self.drawScreen(interaction_type, interaction_step)
            self.frame_count += 1

    def drawScreen(self, interaction_type, interaction_step):
        """
        This method will draw the shapes on the screen
        """
        self.screen.fill(self.background)

        type_text = "Interaction Type: " + interaction_type
        step_text = "Step: " + interaction_step
        type_text_display = self.font.render(type_text, True, self.white)
        step_text_display = self.font.render(step_text, True, self.white)
        type_text_rect = type_text_display.get_rect()
        type_text_rect.topleft = (self.text_left_border, self.text_top_border)
        step_text_rect = step_text_display.get_rect()
        step_text_rect.topleft = (self.text_left_border, self.text_top_border + self.text_horizontal_separation)
        self.screen.blit(type_text_display, type_text_rect)
        self.screen.blit(step_text_display, step_text_rect)

        pygame.draw.circle(self.screen, self.red, (self.screen.get_width() / 2, self.screen.get_height() / 2), 400, 10)
        pygame.display.update()
