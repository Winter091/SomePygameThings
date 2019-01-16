import pygame as pg
import noise

from pygame.locals import *
from Const import *


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

        self.generate_noise()

        self.text = []
        self.update_text()

    def generate_noise(
            self,
            octaves=1,
            pers=0.5,
            lac=2,
            repeatx=1024,
            repeaty=1024,
            base=0
    ):

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
            'Seed ++: ' + str(self.seed_increment),
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
            self.seed_increment += 0.001
        elif key == K_LEFT:
            self.seed_increment -= 0.001

    def update(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit(0)

            elif e.type == pg.KEYDOWN:
                self.change_parameter(e.key)
                self.generate_noise(
                        octaves=self.octaves,
                        pers=self.pers,
                        lac=self.lac,
                        repeatx=self.repeatx,
                        repeaty=self.repeaty,
                        base=self.base
                )
                self.update_text()

    def render(self):
        pg.display.update()
        self.clock.tick(FPS)

    def main_loop(self):
        while self.running:
            self.update()
            self.render()
