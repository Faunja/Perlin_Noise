import pygame
from pygame.locals import *
from User.define_user import User
from Display.define_display import Display
from define_perlinnoise import Perlinnoise

def draw_text(text, position, orientation = [0, 0], font = Display.font, color = (255, 255, 255)):
	text = font.render(text, True, color)
	width, height = text.get_size()
	position = (position[0] * width + orientation[0] * width, position[1] * height + orientation[1] * height)
	Display.Display.blit(text, position)

def display_stats():
	draw_text("FPS : "+str(int(User.affectiveFPS)), [0, 0], color = (60, 60, 255))
	if Perlinnoise.changing == "Segments":
		draw_text("Segments : "+str(int(Perlinnoise.segments)), [0, 1], color = (60, 255, 60))
	else:
		draw_text("Segments : "+str(int(Perlinnoise.segments)), [0, 1], color = (60, 60, 255))
	if Perlinnoise.changing == "Layers":
		draw_text("Layers : "+str(int(Perlinnoise.layers)), [0, 2], color = (60, 255, 60))
	else:
		draw_text("Layers : "+str(int(Perlinnoise.layers)), [0, 2], color = (60, 60, 255))
	if Perlinnoise.changing == "Increase":
		draw_text("Increasing : "+str(int(Perlinnoise.increase)), [0, 3], color = (60, 255, 60))
	else:
		draw_text("Increasing : "+str(int(Perlinnoise.increase)), [0, 3], color = (60, 60, 255))

def display_grid():
	xOffset = Display.tileOffset[0]
	yOffset = Display.tileOffset[1]
	segmentScale = Perlinnoise.scale / Perlinnoise.segments
	tileSize = int(Display.tileSize / Perlinnoise.scale)
	colorScale = int(255 / segmentScale)
	for y in range(Perlinnoise.scale):
		yPosition = tileSize * y + yOffset
		gridY = int(y / segmentScale) * segmentScale
		for x in range(Perlinnoise.scale):
			xPosition = tileSize * x + xOffset
			gridX = int(x / segmentScale) * segmentScale
			try:
				pygame.draw.rect(Display.Display, ((x - gridX) * colorScale, 0, (y - gridY) * colorScale), (xPosition, yPosition, tileSize, tileSize))
			except:
				pygame.draw.rect(Display.Display, (0, 255, 0), (xPosition, yPosition, tileSize, tileSize))

def display_vectors():
	xOffset = Display.tileOffset[0]
	yOffset = Display.tileOffset[1]
	segmentSize = int(Display.tileSize / Perlinnoise.segments)
	tileSize = int(Display.tileSize / Perlinnoise.scale) / 2
	for y in range(1, Perlinnoise.segments):
		yPosition = segmentSize * y + yOffset
		for x in range(1, Perlinnoise.segments):
			xPosition = segmentSize * x + xOffset
			pygame.draw.circle(Display.Display, (255, 255, 255), (xPosition, yPosition), tileSize)

def display_noise():
	xOffset = Display.tileOffset[0]
	yOffset = Display.tileOffset[1]
	tileSize = int(Display.tileSize / Perlinnoise.scale)
	noise = Perlinnoise.noise
	for y in range(Perlinnoise.scale):
		yPosition = tileSize * y + yOffset
		for x in range(Perlinnoise.scale):
			xPosition = tileSize * x + xOffset
			positive = int(int(noise[y][x] < 0) * -noise[y][x] * 255)
			negative = int(int(noise[y][x] >= 0) * noise[y][x] * 255)
			try:
				pygame.draw.rect(Display.Display, (negative, positive, negative + positive), (xPosition, yPosition, tileSize, tileSize))
			except:
				pass

def display_game():
	Display.Display.fill((0, 0, 0))
	display_noise()
	if Display.displayStats:
		display_vectors()
		display_stats()