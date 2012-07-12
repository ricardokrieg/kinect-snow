import pygame
import random

from snowflake import Snowflake

NUM_FLAKES = 1800
START_BATCH = 20

class SnowManager:
	def __init__(self, screen_width):
		self.screen_width = screen_width

		self.snowflakes = [Snowflake() for i in range(0, NUM_FLAKES)]
	# init

	def update(self, mask):
		self.start_some_flakes()

		for snowflake in self.snowflakes:
			snowflake.update(mask, self.screen_width)
	# update

	def draw(self, surface):
		for snowflake in self.snowflakes:
			snowflake.draw(surface)
	# draw

	def start_some_flakes(self):
		started = 0

		for snowflake in self.snowflakes:
			if started < START_BATCH:
				if not snowflake.is_visible():
					if random.choice([True, False]):
						snowflake.set_position()
						started += 1
			else:
				break
	# start_some_flakes
# SnowManager