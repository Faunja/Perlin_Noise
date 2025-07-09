import random
from User.define_user import User

class define_perlinnoise:
	def create_vectors(self, width, height):
		vectors = []
		for row in range(height + 1):
			vectors.append([])
			for column in range(width + 1):
				vectors[row].append(random.randrange(360))
		return vectors

	def smooth_step(self, variable):
		smooth = variable ** 2 * (3 - variable * 2)
		if smooth < 0:
			smooth = 0
		if smooth > 1:
			smooth = 1
		return smooth

	def create_noise(self, vectors, width, height):
		scale = int(100 / (width * height) ** (1 / 2))
		noise = []
		for row in range(height * scale):
			y = row / scale + 1 / scale / 2
			smoothY = self.smooth_step(y % 1)
			noise.append([])
			for column in range(width * scale):
				x = column / scale + 1 / scale / 2
				smoothX = self.smooth_step(x % 1)
				xPosition = int(x)
				yPosition = int(y)
				topLeft = smoothX * User.cos(vectors[yPosition][xPosition]) + smoothY * User.sin(vectors[yPosition][xPosition])
				topRight = -(1 - smoothX) * User.cos(vectors[yPosition][xPosition + 1]) + smoothY * User.sin(vectors[yPosition][xPosition + 1])
				top = (1 - smoothX) * topLeft + smoothX * topRight
				bottomLeft = smoothX * User.cos(vectors[yPosition + 1][xPosition]) - (1 - smoothY) * User.sin(vectors[yPosition + 1][xPosition])
				bottomRight = -(1 - smoothX) * User.cos(vectors[yPosition + 1][xPosition + 1]) - (1 - smoothY) * User.sin(vectors[yPosition + 1][xPosition + 1])
				bottom = (1 - smoothX) * bottomLeft + smoothX * bottomRight
				product = (1 - smoothY) * top + smoothY * bottom
				noise[row].append(product)
		return noise
	
	def update_vectors(self, vectors):
		increase = 45 / User.affectiveFPS
		for row in range(len(vectors)):
			for column in range(len(vectors[row])):
				vectors[row][column] += increase
				if vectors[row][column] >= 360:
					vectors[row][column] = 360 - vectors[row][column]
		noise = self.create_noise(vectors, len(vectors) - 1, len(vectors[0]) - 1)
		return vectors, noise

	def create_map(self):
		self.noise = []
		for row in range(self.height * self.scale):
			self.noise.append([])
			for column in range(self.width * self.scale):
				self.noise[row].append(0)
		for noise in self.noiseLists:
			for y in range(len(noise)):
				yPosition = int(y * (self.height * self.scale) / len(noise))
				for x in range(len(noise[0])):
					xPosition = int(x * (self.width * self.scale) / len(noise[0]))
					self.noise[yPosition][xPosition] += noise[y][x]
		for y in range(self.height * self.scale):
			for x in range(self.width * self.scale):
				self.noise[y][x] /= self.octave

	def update_map(self):
		for repeat in range(self.octave):
			self.vectorLists[repeat], self.noiseLists[repeat] = Perlinnoise.update_vectors(self.vectorLists[repeat])
		self.create_map()

	def __init__(self, width, height, octave = 3, amplitude = 3):
		self.width = width
		self.height = height
		self.octave = octave
		self.amplitude = amplitude
		self.scale = int(100 / (width * height) ** (1 / 2))
		self.vectorLists = []
		self.noiseLists = []
		for repeat in range(octave):
			width = width + repeat * amplitude
			height = height + repeat * amplitude
			self.vectorLists.append(self.create_vectors(width, height))
			self.noiseLists.append(self.create_noise(self.vectorLists[repeat], width, height))
		self.create_map()

Perlinnoise = define_perlinnoise(1, 1)