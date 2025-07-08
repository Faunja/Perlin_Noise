import pygame
from pygame.locals import *
from define_perlinnoise import Perlinnoise

class define_Display:
	def __init__(self):
		Display = pygame.display.get_desktop_sizes()
		self.SCREENWIDTH = Display[0][0]
		self.SCREENHEIGHT = Display[0][1]
		self.fullscreen = False

		self.DISPLAYDIFFERENCE = 4 / 5
		self.DisplayWidth = round(self.SCREENWIDTH * self.DISPLAYDIFFERENCE)
		self.DisplayHeight = round(self.SCREENHEIGHT * self.DISPLAYDIFFERENCE)
		if self.DisplayWidth <= self.DisplayHeight:
			self.DisplayOffset = [0, self.DisplayHeight - self.DisplayWidth]
		elif self.DisplayWidth > self.DisplayHeight:
			self.DisplayOffset = [self.DisplayWidth - self.DisplayHeight, 0]

		self.tileSize = int((self.DisplayHeight - self.DisplayOffset[1]) / (Perlinnoise.height + 1) / Perlinnoise.scale) * Perlinnoise.scale
		if self.tileSize * Perlinnoise.width > self.DisplayWidth:
			self.tileSize = int((self.DisplayWidth - self.DisplayOffset[1]) / (Perlinnoise.width + 1) / Perlinnoise.scale) * Perlinnoise.scale
		self.tileOffset = [round((self.DisplayWidth - self.tileSize * Perlinnoise.width) / 2), round((self.DisplayHeight - self.tileSize * Perlinnoise.height) / 2)]
		self.displayStats = False

		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)

	def update_display(self, DisplayWidth, DisplayHeight, fullscreen):
		if fullscreen == False:
			self.Display = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.RESIZABLE)
		else:
			self.Display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.font = pygame.font.SysFont("impact", int(self.DisplayHeight / 32))

	def change_displaySize(self, width, height):
		self.DisplayWidth = width
		self.DisplayHeight = height
		if self.DisplayWidth < self.DisplayHeight:
			self.DisplayOffset = [0, self.DisplayHeight - self.DisplayWidth]
		elif self.DisplayWidth > self.DisplayHeight:
			self.DisplayOffset = [self.DisplayWidth - self.DisplayHeight, 0]

		self.tileSize = int((self.DisplayHeight - self.DisplayOffset[1]) / (Perlinnoise.height + 1) / Perlinnoise.scale) * Perlinnoise.scale
		if self.tileSize * Perlinnoise.width > self.DisplayWidth:
			self.tileSize = int((self.DisplayWidth - self.DisplayOffset[1]) / (Perlinnoise.width + 1) / Perlinnoise.scale) * Perlinnoise.scale
		self.tileOffset = [round((self.DisplayWidth - self.tileSize * Perlinnoise.width) / 2), round((self.DisplayHeight - self.tileSize * Perlinnoise.height) / 2)]

		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)
	
	def toggle_fullscreen(self):
		self.fullscreen = not self.fullscreen
		if self.fullscreen:
			self.change_displaySize(self.SCREENWIDTH, self.SCREENHEIGHT)
		else:
			self.change_displaySize(round(self.SCREENWIDTH * self.DISPLAYDIFFERENCE), round(self.SCREENHEIGHT * self.DISPLAYDIFFERENCE))

Display = define_Display()