import pygame, math
from pygame.locals import *

class define_User:
	def __init__(self):
		pygame.init()
		self.FPS = 60 ** 60
		self.affectiveFPS = self.FPS
		self.clock = pygame.time.Clock()
		self.playing = True

User = define_User()
