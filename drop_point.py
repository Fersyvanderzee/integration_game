import random
import pygame


class DropPoint:

    radius = 10
    location = [random.randint(0, 1000), random.randint(0, 500)]
    color = [0, 0, 0]
    border_width = 2

    def __init__(self, name, surface):
        self.name = name

        pygame.draw.circle(surface=surface, color=self.color, center=self.location, radius=self.radius, width=self.border_width)


    def set_location(self, x, y):
        self.location[0] = x
        self.location[1] = y
