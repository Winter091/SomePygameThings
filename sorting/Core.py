import pygame as pg
import noise

from pygame.locals import *
from sorting.Const import *
from random import randint


class Core(object):
    def __init__(self):
        pg.init()
        pg.font.init()
        self.running = True
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Courier New', 16)

        self.seed_increment = 0.005
        self.octaves = 1
        self.pers = 0.5
        self.lac = 2
        self.repeatx = 1024
        self.repeaty = 1024
        self.base = 0

        self.text = [
            'Octaves: ' + str(self.octaves),
            'Pers: ' + str(self.pers),
            'Lac: ' + str(self.lac),
            'Repeat: ' + str(self.repeat),
            'Base: ' + str(self.base)
        ]

        self.generate_nums()

    def generate_nums(
            self,
            octaves=1,
            pers=0.5,
            lac=2,
            repeatx=1024,
            repeaty=1024,
            base=0
    ):

        nums = [[0] * WINDOW_H] * WINDOW_W
        x_seed = 0
        y_seed = 0

        for x in range(WINDOW_W):
            x_seed += self.seed_increment
            y_seed = 0

            for y in range(WINDOW_H):
                y_seed += self.seed_increment

                # -1 to 1
                bright = noise.pnoise2(
                        x_seed,
                        y_seed,
                        octaves=octaves,
                        persistence=pers,
                        lacunarity=lac,
                        repeatx=repeatx,
                        repeaty=repeaty,
                        base=base
                )

                # 0 to 255
                bright = int((bright + 1) * 127.5)

                self.screen.set_at((x, y), (bright, bright, bright))

    def update_text(self):
        self.text = [
            'Octaves: ' + str(self.octaves),
            'Pers: ' + str(self.pers),
            'Lac: ' + str(self.lac),
            'Repeatx: ' + str(self.repeatx),
            'Base: ' + str(self.base)
        ]

    def update_keys(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit(0)

            elif e.type == pg.KEYDOWN:
                if e.key == K_RIGHT:
                    self.seed += 0.5
                elif e.key == K_LEFT:
                    self.seed -= 0.5

                elif e.key == K_q:
                    self.octaves += 1
                elif e.key == K_a:
                    self.octaves -= 1

                elif e.key == K_w:
                    self.pers += 0.5
                elif e.key == K_s:
                    self.pers -= 0.5

                elif e.key == K_e:
                    self.lac += 0.25
                elif e.key == K_d:
                    self.lac -= 0.25

                elif e.key == K_r:
                    self.repeat *= 2
                elif e.key == K_f:
                    self.repeat //= 2

                elif e.key == K_t:
                    self.base += 1
                elif e.key == K_g:
                    self.base -= 1

                self.nums = self.generate_nums(self.seed,
                                               self.octaves,
                                               self.pers,
                                               self.lac,
                                               self.repeat,
                                               self.base)

    def render(self):

        # Lines ===============================================================
        # for i, num in enumerate(self.nums):
        #     color = WHITE
        #     pg.draw.line(self.screen, color, (i, WINDOW_H), (i, WINDOW_H - num))

        # Text ================================================================
        # x = 30
        # for string in self.text:
        #     text_rect = self.font.render(string, False, GREEN)
        #     self.screen.blit(text_rect, (30, x))
        #     x += 12

        pg.display.update()
        self.clock.tick(FPS)

    def main_loop(self):
        while self.running:
            self.update_keys()
            self.update_text()
            self.render()
