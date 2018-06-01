import pygame as pg

from shaders.Const import *
from shaders.MenuManager import MenuManager
from shaders.Map import Map


class Core(object):
    def __init__(self):
        pg.init()

        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.bg.fill(pg.Color('#459adf'))
        self.run = True
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.keyR = False
        self.keyL = False
        self.keyD = False
        self.keyU = False

        self.oMenuManager = MenuManager()
        self.oMap = Map()

    def main_loop(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(100)

    def input(self):
        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    self.keyR = True
                elif e.key == pg.K_LEFT:
                    self.keyL = True
                elif e.key == pg.K_DOWN:
                    self.keyD = True
                elif e.key == pg.K_UP:
                    self.keyU = True

            elif e.type == pg.KEYUP:
                if e.key == pg.K_RIGHT:
                    self.keyR = False
                elif e.key == pg.K_LEFT:
                    self.keyL = False
                elif e.key == pg.K_DOWN:
                    self.keyD = False
                elif e.key == pg.K_UP:
                    self.keyU = False

    def update(self):
        self.oMenuManager.update(self)

    def render(self):
        self.oMenuManager.render(self)

    def get_map(self):
        return self.oMap
