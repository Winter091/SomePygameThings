import pygame as pg

from MazeGenerator.Const import *
from MazeGenerator.Cell import Cell

from random import randint


class Core(object):
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.running = True

        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.bg.fill(GRAY)

        self.grid = []
        self._init_objects()

        self.current = self.grid[0]

        self.stack = []

    def _init_objects(self):
        for j in range(C):
            for i in range(R):
                cell = Cell(i, j)
                self.grid.append(cell)

    def main_loop(self):
        while self.running:
            self.update()
            self.render()
            self.clock.tick(FPS)

    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

        self.current.visited = True

        # Get all unvisited neighbours
        next = self.check_neighbours()

        # If the current cell has any neighbours
        # which have not been visited
        if next is not None:

            # Push the current cell to the stack
            self.stack.append(self.current)

            # Remove the wall between the current
            # cell and the chosen cell
            self.current.remove_walls(next)

            # Make the chosen cell the current cell
            self.current = next

        # Else if stack is not empty
        elif len(self.stack) != 0:

            # Pop a cell from the stack;
            # Make it the current cell
            self.current = self.stack.pop()

        # No neighbours and stack hasn't got anything:
        # Program is over
        else:
            pass

    def i(self, x, y):
        if x < 0 or y < 0 or x > C - 1 or y > R - 1:
            return None
        return x + y * C

    def check_neighbours(self):
        neighbours = []

        try:
            top = self.grid[self.i(self.current.x, self.current.y - 1)]
        except TypeError:
            top = None

        try:
            right = self.grid[self.i(self.current.x + 1, self.current.y)]
        except TypeError:
            right = None

        try:
            bottom = self.grid[self.i(self.current.x, self.current.y + 1)]
        except TypeError:
            bottom = None

        try:
            left = self.grid[self.i(self.current.x - 1, self.current.y)]
        except TypeError:
            left = None

        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)

        if len(neighbours) > 0:
            return neighbours[randint(0, len(neighbours) - 1)]
        else:
            return None

    def render(self):
        self.screen.blit(self.bg, (0, 0))

        for cell in self.grid:
            cell.render(self)

        pg.display.update()
