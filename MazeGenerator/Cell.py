import pygame as pg

try:
    from MazeGenerator.Const import *
except ImportError:
    from Const import *


class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False

        self.rect = pg.Rect(x * W, y * W, W, W)

    def remove_walls(self, other):

        # Other is right
        if self.x - other.x == -1:
            self.walls[1] = False
            other.walls[3] = False

        # Other is left
        elif self.x - other.x == 1:
            self.walls[3] = False
            other.walls[1] = False

        # Other is above
        elif self.y - other.y == 1:
            self.walls[0] = False
            other.walls[2] = False

        # Other is below
        elif self.y - other.y == -1:
            self.walls[2] = False
            other.walls[0] = False

    def render(self, core):
        x = self.rect.x
        y = self.rect.y

        if self == core.current:
            pg.draw.rect(core.screen, GREEN, self.rect)
        elif self.visited:
            pg.draw.rect(core.screen, PURPLE, self.rect)

        if self.walls[0]:
            pg.draw.line(core.screen, WHITE, (x, y), (x + W, y))
        if self.walls[1]:
            pg.draw.line(core.screen, WHITE, (x + W, y), (x + W, y + W))
        if self.walls[2]:
            pg.draw.line(core.screen, WHITE, (x + W, y + W), (x, y + W))
        if self.walls[3]:
            pg.draw.line(core.screen, WHITE, (x, y + W), (x, y))
