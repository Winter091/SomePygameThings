import pygame as pg

from sorting.Const import *
from random import randint


class Core(object):
	def __init__(self):
		pg.init()
		pg.font.init()
		self.running = True
		self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))

		self.bg = pg.Surface((WINDOW_W, WINDOW_H))
		self.bg.fill(BLACK)

		self.clock = pg.time.Clock()
		self.font = pg.font.SysFont('Courier New', 16)

		self.nums = [randint(1, WINDOW_H) for _ in range(WINDOW_W)]
		self.iterations = 0
		self.sorted = False

	def bubble_sort(self):

		for i in range(len(self.nums) - 1):
			# ============================SORTING_START============================

			self.sorted = True
			for j in range(len(self.nums) - 1 - i):
				self.iterations += 1
				if self.nums[j] > self.nums[j + 1]:
					self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
					self.sorted = False

			if self.sorted:
				break

			# =============================SORTING_END=============================

			for e in pg.event.get():
				if e.type == pg.QUIT:
					exit(0)

			self.screen.blit(self.bg, (0, 0))

			for i, num in enumerate(self.nums):
				pg.draw.line(self.screen, WHITE, (i, WINDOW_H), (i, WINDOW_H - num))
			text_rect = self.font.render('Iterations: ' + str(self.iterations), False, GREEN)
			self.screen.blit(text_rect, (30, 30))

			pg.display.update()
			self.clock.tick(FPS)

		self.sorted = True

	def coctail_shaker_sort(self):

		for i in range(len(self.nums) // 2):
			# ============================SORTING_START================================

			self.sorted = True
			for j in range(i + 1, len(self.nums) - i):
				self.iterations += 1
				if self.nums[j] < self.nums[j - 1]:
					self.nums[j], self.nums[j - 1] = self.nums[j - 1], self.nums[j]
					self.sorted = False

			if self.sorted:
				break

			self.sorted = True
			for j in range(len(self.nums) - i - 1, i, -1):
				self.iterations += 1
				if self.nums[j] < self.nums[j - 1]:
					self.nums[j], self.nums[j - 1] = self.nums[j - 1], self.nums[j]
					self.sorted = False

			if self.sorted:
				break

			# =============================SORTING_END================================

			for e in pg.event.get():
				if e.type == pg.QUIT:
					exit(0)

			self.screen.blit(self.bg, (0, 0))

			for i, num in enumerate(self.nums):
				pg.draw.line(self.screen, WHITE, (i, WINDOW_H), (i, WINDOW_H - num))
			text_rect = self.font.render('Iterations: ' + str(self.iterations), False, GREEN)
			self.screen.blit(text_rect, (30, 30))

			pg.display.update()
			self.clock.tick(FPS)

		self.sorted = True

	def render(self):
		for e in pg.event.get():
			if e.type == pg.QUIT:
				exit(0)

		self.screen.blit(self.bg, (0, 0))

		for i, num in enumerate(self.nums):
			color = GREEN if self.sorted else WHITE
			pg.draw.line(self.screen, color, (i, WINDOW_H), (i, WINDOW_H - num))

		text_rect = self.font.render('Iterations: ' + str(self.iterations), False, GREEN)
		self.screen.blit(text_rect, (30, 30))

		pg.display.update()
		self.clock.tick(FPS)

	def main_loop(self):
		while self.running:

			if not self.sorted and pg.time.get_ticks() > 2000:
				self.coctail_shaker_sort()
			else:
				self.render()
