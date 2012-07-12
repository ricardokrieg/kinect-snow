import pygame
from pygame.color import THECOLORS
import random

Y_DROP = 10
X_DRIFT = 6
SIZE = 6

class Snowflake:
	def __init__(self):
		self.x = 0
		self.y = 0
	# init

	def update(self, mask, width):
		if not self.is_visible() or self.is_on_top_edge_of_user(mask, width): return

		self.x += random.randint(0, X_DRIFT) - X_DRIFT/2
		self.y += random.randint(0, Y_DROP)
	# update

	def draw(self, surface):
		pygame.draw.circle(surface, THECOLORS['white'], (self.x, self.y), SIZE/2)
	# draw

	def is_visible(self):
		if self.x < 0 or self.x >= 640 or self.y < 0 or self.y >= 480: return False

		return True
	# is_visible

	def set_position(self):
		self.x = random.randint(0, 640)
		self.y = 1
	# set_position

	def is_on_top_edge_of_user(self, mask, width):
		if mask[self.y*width + self.x] != 0 and mask[(self.y-SIZE*2)*width + self.x] == 0: return True

		return False
	# is_on_top_edge_of_user
# Snowflake