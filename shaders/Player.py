import pygame as pg

from shaders.Const import *


class Player(object):
    def __init__(self, x, y, w, h, image):
        self.rect = pg.Rect(x, y, w, h)
        self.image = image
        self.x_vel = 0
        self.y_vel = 0

    def update(self, core):
        self.physics(core)

    def physics(self, core):
        if core.keyL:
            self.x_vel -= SPEED_INCREASE_RATE
        elif core.keyR:
            self.x_vel += SPEED_INCREASE_RATE
        elif core.keyD:
            self.y_vel += SPEED_INCREASE_RATE
        elif core.keyU:
            self.y_vel -= SPEED_INCREASE_RATE

        if not (core.keyL or core.keyR or core.keyD or core.keyU) and (self.x_vel or self.y_vel):
            if self.x_vel > 0:
                self.x_vel -= SPEED_DECREASE_RATE
            elif self.x_vel < 0:
                self.x_vel += SPEED_DECREASE_RATE

            if self.y_vel > 0:
                self.y_vel -= SPEED_DECREASE_RATE
            elif self.y_vel < 0:
                self.y_vel += SPEED_DECREASE_RATE

        if self.x_vel > MAX_X_SPEED:
            self.x_vel = MAX_X_SPEED
        elif self.x_vel < -MAX_X_SPEED:
            self.x_vel = -MAX_X_SPEED
        elif self.y_vel > MAX_Y_SPEED:
            self.y_vel = MAX_Y_SPEED
        elif self.y_vel < -MAX_Y_SPEED:
            self.y_vel = -MAX_Y_SPEED

        tiles = core.get_map().get_tiles_for_collision(self.rect.x // 32, self.rect.y // 32)

        self.rect.x += self.x_vel
        self.update_x_pos(tiles)

        self.rect.y += self.y_vel
        self.update_y_pos(tiles)

    def update_x_pos(self, tiles):
        for tile in tiles:
            if tile is not None and tile != 0:
                if self.rect.colliderect(tile.rect):
                    if self.x_vel > 0:
                        self.x_vel = 0
                        self.rect.right = tile.rect.left
                    elif self.x_vel < 0:
                        self.x_vel = 0
                        self.rect.left = tile.rect.right

    def update_y_pos(self, tiles):
        for tile in tiles:
            if tile is not None and tile != 0:
                if self.rect.colliderect(tile.rect):
                    if self.y_vel > 0:
                        self.y_vel = 0
                        self.rect.bottom = tile.rect.top
                    elif self.y_vel < 0:
                        self.y_vel = 0
                        self.rect.top = tile.rect.bottom

    def render(self, core):
        core.screen.blit(self.image, self.rect)
