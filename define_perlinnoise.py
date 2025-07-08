import random
from User.define_user import User

class define_perlinnoise:
	def create_vectors(self):
		self.vectors = []
		for row in range(self.height + 1):
			self.vectors.append([])
			for column in range(self.width + 1):
				self.vectors[row].append(random.randrange(360))

	def update_vectors(self):
		for row in range(self.height + 1):
			for column in range(self.width + 1):
				self.vectors[row][column] += 45 / User.affectiveFPS
				if self.vectors[row][column] >= 360:
					self.vectors[row][column] = 360 - self.vectors[row][column]
		self.create_noise()

	def smooth_step(self, variable):
		smooth = variable ** 2 * (3 - 2 * variable)
		if smooth < 0:
			smooth = 0
		if smooth > 1:
			smooth = 1
		return smooth

	def create_noise(self):
		self.noise = []
		for row in range(self.height * self.scale):
			y = row / self.scale
			smoothY = self.smooth_step(y % 1)
			self.noise.append([])
			for column in range(self.width * self.scale):
				x = column / self.scale
				smoothX = self.smooth_step(x % 1)
				xPosition = int(x)
				yPosition = int(y)
				topLeft = smoothX * User.cos(self.vectors[yPosition][xPosition]) + smoothY * User.sin(self.vectors[yPosition][xPosition])
				topRight = -(1 - smoothX) * User.cos(self.vectors[yPosition][xPosition + 1]) + smoothY * User.sin(self.vectors[yPosition][xPosition + 1])
				top = (1 - smoothX) * topLeft + smoothX * topRight
				bottomLeft = smoothX * User.cos(self.vectors[yPosition + 1][xPosition]) + -(1 - smoothY) * User.sin(self.vectors[yPosition + 1][xPosition])
				bottomRight = -(1 - smoothX) * User.cos(self.vectors[yPosition + 1][xPosition + 1]) + -(1 - smoothY) * User.sin(self.vectors[yPosition + 1][xPosition + 1])
				bottom = (1 - smoothX) * bottomLeft + smoothX * bottomRight
				product = (1 - smoothY) * top + smoothY * bottom
				self.noise[row].append(product)

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.scale = 15
		self.create_vectors()
		self.create_noise()

Perlinnoise = define_perlinnoise(5, 5)