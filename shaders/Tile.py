import pygame as pg


class Tile(object):
    def __init__(self, x, y, w, h, image):
        self.rect = pg.Rect(x, y, w, h)
        self.image = image

    def update(self, core):
        pass

    def render(self, core):
        core.screen.blit(self.image, self.rect)
