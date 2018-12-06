import pygame as pg

from double_pendulum.Const import *
from math import *


def get_a1(obj):
	m1 = obj.m1
	m2 = obj.m2
	g = obj.g
	a1 = obj.a1
	a2 = obj.a2
	a1_v = obj.a1_v
	a2_v = obj.a2_v
	r1 = obj.r1
	r2 = obj.r2

	num1 = -g * (2 * m1 + m2) * sin(a1)
	num2 = -m2 * g * sin(a1 - 2 * a2)
	num3 = -2 * sin(a1 - a2) * m2
	num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2)
	den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
	res = (num1 + num2 + num3 * num4) / den

	return res


def get_a2(obj):
	m1 = obj.m1
	m2 = obj.m2
	g = obj.g
	a1 = obj.a1
	a2 = obj.a2
	a1_v = obj.a1_v
	a2_v = obj.a2_v
	r1 = obj.r1
	r2 = obj.r2

	num1 = 2 * sin(a1 - a2)
	num2 = (a1_v * a1_v * r1 * (m1 + m2))
	num3 = g * (m1 + m2) * cos(a1)
	num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2)
	den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
	res = (num1 * (num2 + num3 + num4)) / den

	return res


class Core(object):
	def __init__(self):
		pg.init()
		self.running = True
		self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))

		self.bg = pg.Surface((WINDOW_W, WINDOW_H))
		self.bg.fill(BG_COLOR)

		self.clock = pg.time.Clock()

		# ============================================

		self.g = 0.9

		self.r1 = 150
		self.r2 = 150

		self.m1 = 1
		self.m2 = 0.000001

		self.a1 = pi/2
		self.a2 = pi/3
		self.a1_v = 0
		self.a2_v = 0
		self.a1_a = 0
		self.a2_a = 0

		self.x1 = 0
		self.y1 = 0

		self.x2 = 0
		self.y2 = 0

		self.last_x = 0
		self.last_y = 0

		self.lines = []
		self.frames = 1

		self.damping = 0.1

	def update(self):

		for e in pg.event.get():
			if e.type == pg.QUIT:
				self.running = False

			elif e.type == pg.KEYDOWN:
				if e.key == pg.K_RIGHT:
					self.r1 += 10
				elif e.key == pg.K_LEFT:
					self.r1 -= 10
				elif e.key == pg.K_DOWN:
					self.r2 -= 10
				elif e.key == pg.K_UP:
					self.r2 += 10

		self.a1_v += self.a1_a
		self.a2_v += self.a2_a
		self.a1 += self.a1_v
		self.a2 += self.a2_v

		self.x1 = int(self.r1 * sin(self.a1)) + ZERO_PNT[0]
		self.y1 = int(self.r1 * cos(self.a1)) + ZERO_PNT[1]

		self.last_x = self.x2
		self.last_y = self.y2

		self.x2 = self.x1 + int(self.r2 * sin(self.a2))
		self.y2 = self.y1 + int(self.r2 * cos(self.a2))

		self.a1_a = get_a1(self)
		self.a2_a = get_a2(self)

		if self.frames > 1:
			self.lines.append(((self.last_x, self.last_y), (self.x2, self.y2)))
			if self.frames > MAX_ROUTE_LEN:
				self.lines = self.lines[1:]

	def render(self):
		self.screen.blit(self.bg, (0, 0))

		# First
		pg.draw.line(self.screen, BLACK, ZERO_PNT, (self.x1, self.y1), 3)
		pg.draw.circle(self.screen, BLACK, (self.x1, self.y1), 15)

		# Second
		pg.draw.line(self.screen, BLACK, (self.x1, self.y1), (self.x2, self.y2), 3)
		pg.draw.circle(self.screen, BLACK, (self.x2, self.y2), 15)

		# Path
		for line in self.lines:
			pg.draw.line(self.screen, BLACK, line[0], line[1], 1)

		pg.display.update()

		self.frames += 1

	def main_loop(self):
		while self.running:
			self.update()
			self.render()
			self.clock.tick(FPS)

