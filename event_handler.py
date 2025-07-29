import pygame, copy
from pygame.locals import *
from User.define_user import User
from User.define_controls import Controls
from define_perlinnoise import Perlinnoise
from Display.define_display import Display

def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEWHEEL:
			if event.y == -1 and Perlinnoise.segments < 10:
				Perlinnoise.segments += 1
			if event.y == 1 and Perlinnoise.segments > 1:
				Perlinnoise.segments -= 1

		if event.type == pygame.KEYDOWN:
			if event.key == Controls.quitGame:
				User.playing = False

			if event.key in Controls.changedisplayStats:
				Display.displayStats = 1 - Display.displayStats
			if event.key in Controls.fullscreen:
				Display.toggle_fullscreen()

			if event.key in Controls.sizeUp and Perlinnoise.segments < 10:
				Perlinnoise.segments += 1
			if event.key in Controls.sizeDown and Perlinnoise.segments > 1:
				Perlinnoise.segments -= 1

		if event.type == pygame.VIDEORESIZE:
			width, height = event.size
			Display.change_displaySize(width, height)

		if event.type == pygame.QUIT:
			User.playing = False
	
	Perlinnoise.update_layers()
