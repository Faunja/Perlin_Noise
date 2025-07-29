import pygame

class define_Controls:
	def __init__(self):
		self.quitGame = pygame.K_ESCAPE
		self.fullscreen = [pygame.K_F11, pygame.K_f]

		self.changedisplayStats = [pygame.K_F3, pygame.K_q]
		self.changeSegments = [pygame.K_j, pygame.K_1]
		self.changeLayers = [pygame.K_k, pygame.K_2]
		self.changeIncrease = [pygame.K_l, pygame.K_3]
		self.sizeUp = [pygame.K_w, pygame.K_UP]
		self.sizeDown = [pygame.K_s, pygame.K_DOWN]

Controls = define_Controls()
