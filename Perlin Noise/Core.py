import pygame as pg
import noise

from pygame.locals import *
from random import randint
from Const import *


class Core(object):
    def __init__(self):
        pg.init()
        pg.font.init()
        self.running = True
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Courier New', 16)

        self.x_seed = randint(-10000, 10000)
        self.y_seed = randint(-10000, 10000)
        self.seed_increment = 0.005
        self.octaves = 7
        self.pers = 0.5
        self.lac = 2
        self.repeatx = 1024
        self.repeaty = 1024
        self.base = 0

        self.generate_noise(self.x_seed, self.y_seed)

        self.text = []
        # self.update_text()

    def generate_noise(
            self,
            x_seed,
            y_seed,
            octaves=7,
            pers=0.5,
            lac=2,
            repeatx=1024,
            repeaty=1024,
            base=0
    ):

        for x in range(WINDOW_W):
            x_seed += self.seed_increment
            yseed = y_seed

            for y in range(WINDOW_H):
                yseed += self.seed_increment

                # -1 to 1
                height = noise.pnoise2(
                        x_seed,
                        yseed,
                        octaves,
                        pers,
                        lac,
                        repeatx,
                        repeaty,
                        base
                )

                # 0 to 255
                height = int((height + 1) * 127.5)

                self.screen.set_at((x, y), self.get_color(height))

    def update_text(self):
        self.text = [
            'Seed: ' + str(self.x_seed) + ' ' + str(self.y_seed),
            'Octaves: ' + str(self.octaves),
            'Pers: ' + str(self.pers),
            'Lac: ' + str(self.lac),
            'RepeatX: ' + str(self.repeatx),
            'RepeatY: ' + str(self.repeaty),
            'Base: ' + str(self.base)
        ]

        # Blit to screen
        for y, string in enumerate(self.text):
            surface = self.font.render(string, True, GREEN)
            self.screen.blit(surface, (15, 15 + 13 * y))

    def change_parameter(self, key):
        if key == K_q:
            self.octaves += 1
        elif key == K_a:
            self.octaves -= 1

        elif key == K_w:
            self.pers += 0.1
        elif key == K_s:
            self.pers -= 0.1

        elif key == K_e:
            self.lac += 0.25
        elif key == K_d:
            self.lac -= 0.25

        elif key == K_r:
            self.repeatx *= 2
        elif key == K_f:
            self.repeatx //= 2

        elif key == K_t:
            self.repeaty *= 2
        elif key == K_g:
            self.repeaty //= 2

        elif key == K_y:
            self.base += 1
        elif key == K_h:
            self.base -= 1

        elif key == K_RIGHT:
            self.x_seed += 0.5
        elif key == K_LEFT:
            self.x_seed -= 0.5
        elif key == K_UP:
            self.y_seed -= 0.5
        elif key == K_DOWN:
            self.y_seed += 0.5

    def get_color(self, height):

        # Dark blue
        if height <= 100:
            color = (0, 0, 100)

        # Blue
        elif 100 < height <= 115:
            color = (0, 0, 255)

        # Green
        elif 115 < height <= 127:
            color = (0, 129, 0)

        # Dark yellow
        elif 127 < height <= 140:
            color = (128, 128, 0)

        # Gray
        elif 140 < height <= 160:
            color = (160, 160, 160)

        # White
        elif 160 < height <= 255:
            color = (225, 225, 225)

        return color

    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit(0)

            elif e.type == pg.KEYDOWN:
                self.change_parameter(e.key)
                self.generate_noise(
                        self.x_seed,
                        self.y_seed,
                        self.octaves,
                        self.pers,
                        self.lac,
                        self.repeatx,
                        self.repeaty,
                        self.base
                )
                # self.update_text()

    def render(self):
        pg.display.update()
        self.clock.tick(FPS)

    def main_loop(self):
        while self.running:
            self.update()
            self.render()
