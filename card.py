import pygame
import random


class FunctionCard:

    location = [random.randint(0, 1000), random.randint(0, 500)]
    color = [0, 0, 0]
    width = 200
    height = 150

    def __init__(self, name, surface):
        self.name = name
        self.x_max = self.location[0] + self.width
        self.y_max = self.location[1] + self.height


        border_width = 2
        rect = (self.location, (self.width, self.height))

        pygame.draw.rect(surface=surface, color=self.color, rect=rect, width=border_width)

    def get_name(self):
        return self.name

    def get_xy(self):
        return self.location

    def set_location(self, x, y):
        self.location[0] = x
        self.location[1] = y

    def set_color(self, color):
        self.color[0] = color[0]
        self.color[1] = color[1]
        self.color[2] = color[2]




