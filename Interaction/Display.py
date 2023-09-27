"""
This class displays everything that needs to be displayed.
"""

import time
import pygame

from Graph.Node import Node


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
        self.text_vertical_separation = self.font_size
        self.text_fields = ["Graph Type: ", "Interaction Type: ", "Step: "]
        self.text_rect_previous = []
        # initialize text_rect_previous list
        for i in range(len(self.text_fields)):
            self.text_rect_previous.append(pygame.Rect(0, 0, 0, 0))

        # color variables
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (100, 100, 100)
        self.red = (200, 50, 50)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.background = (40, 20, 30)

        # graph variables
        self.node_size = 10
        self.node_base_size = 10

    def display(self, interaction_type, interaction_step):
        """
        This method will display the program and update with 60 fps
        """
        # timing functions for constant fps
        self.elapsed_time = time.perf_counter() - self.previous_time
        if self.elapsed_time > 1 / self.frame_rate:
            self.previous_time = time.perf_counter()
            self.draw_screen(interaction_type, interaction_step)
            self.frame_count += 1

    def draw_screen(self, interaction_type, interaction_step):
        """
        This method will draw the shapes on the screen
        """
        self.screen.fill(self.background)

        pygame.draw.circle(self.screen, self.red, (self.screen.get_width() / 2, self.screen.get_height() / 2), 400, 10)
        pygame.display.update()

    def update_graph(self, graph):
        """
        This method will update the graph onto the screen.
        Both creating the graph and updating the nodes.
        """
        update_rect = []
        for node in graph:
            node_radius = abs(node.return_value() * self.node_size) + self.node_base_size
            print("Radius: " + str(node_radius))
            print("Location: " + str(node.return_coordinate()))
            coordinate_x = node.return_coordinate()[0]
            coordinate_y = node.return_coordinate()[1]
            pygame.draw.circle(self.screen, node.return_color(), (coordinate_x, coordinate_y), node_radius, 0)
            text = str(node.return_value())
            print("Value: " + text)
            text_display = self.font.render(text, True, self.white)
            text_rect = text_display.get_rect()
            text_rect.center = (node.return_coordinate())
            self.screen.blit(text_display, text_rect)
            node_rect = pygame.Rect((coordinate_x - node_radius, coordinate_y - node_radius), (node_radius * 2, node_radius * 2))
            print(node_rect)
            update_rect.append(node_rect)
        pygame.display.update(update_rect)

    def draw_text(self, text_input):
        """
        This method will display all the necessary text on screen in the top-left corner.
        It does this by drawing a new background, then the text and then the screen, only at the coordinates directly around the text.
        To ensure that no white leftovers from previous text remain on the screen,
        if the previous text is physically bigger than the current text, the screen will be updated around the previous text.
        """
        update_rect = []
        for index in enumerate(text_input):
            text = self.text_fields[index[0]] + index[1]
            text_display = self.font.render(text, True, self.white)
            text_rect = text_display.get_rect()
            text_rect.topleft = (self.text_left_border, self.text_top_border + self.text_vertical_separation * index[0])
            if text_rect[2] > self.text_rect_previous[index[0]][2]:     # Compare whether current or previous text is bigger
                update_rect.append(text_rect)
            else:
                update_rect.append(self.text_rect_previous[index[0]])
            self.screen.fill(self.background, update_rect[index[0]])
            self.screen.blit(text_display, text_rect)
            self.text_rect_previous[index[0]] = text_rect
        pygame.display.update(update_rect)

    def reset_screen(self):
        """
        This method will reset the entire screen and create an empty background
        """
        self.screen.fill(self.background)
        pygame.display.update()
