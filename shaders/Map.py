import pygame as pg

from pytmx.util_pygame import load_pygame
from shaders.Tile import Tile
from shaders.Player import Player
from shaders.Const import *


class Map(object):
    def __init__(self):
        self.tiles = []
        self.tiles_bg = []
        self.map_size = [0, 0]
        self.tile_map = None
        self.bg_image = pg.Surface((WINDOW_W, WINDOW_H))

        self.oPlayer = Player(64, 64, 32, 32, pg.image.load('tile_map/player.bmp'))

        self.load_level('tile_map/test_map.tmx')

    def load_level(self, filename):
        level = load_pygame(filename)

        self.map_size = [level.width, level.height]
        self.tile_map = [[0] * level.height for _ in range(level.width)]

        layer_num = 0
        for layer in level.visible_layers:
            for y in range(level.height):
                for x in range(level.width):

                    # Load pg surface
                    image = level.get_tile_image(x, y, layer_num)

                    # Image is none when there are no tile in that place
                    if image is not None:
                        if layer.name == 'Foreground':
                            # Two lists: first for collision, second for rendering
                            self.tile_map[x][y] = Tile(x * 32, y * 32, 32, 32, image)
                            self.tiles.append(self.tile_map[x][y])
                        elif layer.name == 'Background':
                            pass
            layer_num += 1

    def update(self, core):
        self.get_player().update(core)

    def render(self, core):
        core.screen.blit(self.bg_image, (0, 0))

        for tile in self.tiles:
            tile.render(core)

        self.get_player().render(core)

    def get_player(self):
        return self.oPlayer

    def get_tiles_for_collision(self, x, y):
        return (
            self.tile_map[x][y],

            self.tile_map[x + 1][y],
            self.tile_map[x][y + 1],
            self.tile_map[x + 1][y + 1],

            self.tile_map[x - 1][y],
            self.tile_map[x][y - 1],
            self.tile_map[x - 1][y - 1]
        )