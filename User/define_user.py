import pygame, math
from pygame.locals import *

class define_User:
	def __init__(self):
		pygame.init()
		self.FPS = 60 ** 60
		self.affectiveFPS = self.FPS
		self.clock = pygame.time.Clock()
		self.playing = True

	def sin(self, degree):
		return math.sin(math.radians(degree))
	def cos(self, degree):
		return math.cos(math.radians(degree))

User = define_User()
