import pygame, math
from pygame.locals import *
from User.define_user import User
from Display.define_display import Display
from define_perlinnoise import Perlinnoise

def draw_text(text, position, orientation = [0, 0], font = Display.font, color = (255, 255, 255)):
	text = font.render(text, True, color)
	width, height = text.get_size()
	position = (position[0] + orientation[0] * width, position[1] + orientation[1] * height)
	Display.Display.blit(text, position)

def display_stats():
	if User.affectiveFPS < 40:
		draw_text("FPS: "+str(int(User.affectiveFPS)), [0, 0], color = (255, 60, 60))
		return
	draw_text("FPS: "+str(int(User.affectiveFPS)), [0, 0], color = (60, 255, 60))

def display_noise():
	noise = Perlinnoise.noise
	xOffset = Display.tileOffset[0]
	yOffset = Display.tileOffset[1]
	tileSize = int(Display.tileSize / Perlinnoise.scale)
	for y in range(Perlinnoise.height * Perlinnoise.scale):
		yPosition = tileSize * y + yOffset
		for x in range(Perlinnoise.width * Perlinnoise.scale):
			xPosition = tileSize * x + xOffset
			increase = abs(noise[y][x] * 255)
			positive = int(int(noise[y][x] < 0) * -noise[y][x] * 255)
			negative = int(int(noise[y][x] >= 0) * noise[y][x] * 255)
			try:
				pygame.draw.rect(Display.Display, (positive, negative + positive, negative), (xPosition, yPosition, tileSize, tileSize))
			except:
				pass

def display_game():
	Display.Display.fill((0, 0, 0))
	display_noise()
	if Display.displayStats:
		display_stats()