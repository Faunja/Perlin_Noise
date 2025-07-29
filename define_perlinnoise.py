import random
from User.define_user import User

class define_noise:
	def update_vectors(self):
		for y in range(self.segments + 1):
			if len(self.vectors) <= y:
				self.vectors.append([])
			for x in range(self.segments + 1):
				if len(self.vectors[y]) <= x:
					self.vectors[y].append(random.randint(0, 359))
				else:
					self.vectors[y][x] += 360 / 10 / User.affectiveFPS
					if self.vectors[y][x] >= 360:
						self.vectors[y][x] = self.vectors[y][x] - 360
	
	def smooth_step(self, variable):
		smooth = variable ** 2 * (3 - variable * 2)
		if smooth < 0:
			smooth = 0
		if smooth > 1:
			smooth = 1
		return smooth

	def update_noise(self):
		segmentScale = self.scale / self.segments
		for column in range(self.scale):
			y = self.smooth_step((column / segmentScale) % 1)
			yVector = int(column / segmentScale)
			for row in range(self.scale):
				x = self.smooth_step((row / segmentScale) % 1)
				xVector = int(row / segmentScale)

				topLeft = x * User.cos(self.vectors[yVector][xVector]) + y * User.sin(self.vectors[yVector][xVector])
				topRight = -(1 - x) * User.cos(self.vectors[yVector][xVector + 1]) + y * User.sin(self.vectors[yVector][xVector + 1])
				top = (1 - x) * topLeft + x * topRight

				bottomLeft = x * User.cos(self.vectors[yVector + 1][xVector]) - (1 - y) * User.sin(self.vectors[yVector + 1][xVector])
				bottomRight = -(1 - x) * User.cos(self.vectors[yVector + 1][xVector + 1]) - (1 - y) * User.sin(self.vectors[yVector + 1][xVector + 1])
				bottom = (1 - x) * bottomLeft + x * bottomRight

				product = (1 - y) * top + y * bottom
				self.noise[column][row] = product

	def __init__(self, segments, scale):
		self.segments = segments
		self.scale = scale
		self.vectors = []
		self.update_vectors()
		self.noise = []
		for y in range(self.scale):
			self.noise.append([])
			for x in range(self.scale):
				self.noise[y].append(0)
		self.update_noise()

class define_perlinnoise:
	def __init__(self, layers, increase):
		self.segments = 5
		self.scale = 100
		self.noise = []
		for y in range(self.scale):
			self.noise.append([])
			for x in range(self.scale):
				self.noise[y].append(0)

		self.layers = layers
		self.increase = increase
		self.noiseLayers = []
		for layer in range(self.layers):
			self.noiseLayers.append(define_noise(self.segments + layer * self.increase, self.scale))
			for y in range(self.scale):
				for x in range(self.scale):
					self.noise[y][x] += self.noiseLayers[layer].noise[y][x]
		for y in range(self.scale):
			for x in range(self.scale):
				self.noise[y][x] /= self.layers
	
	def update_layers(self):
		for y in range(self.scale):
			for x in range(self.scale):
				self.noise[y][x] = 0
		for layer in range(self.layers):
			self.noiseLayers[layer].segments = self.segments + layer * self.increase
			self.noiseLayers[layer].update_vectors()
			self.noiseLayers[layer].update_noise()
			for y in range(self.scale):
				for x in range(self.scale):
					self.noise[y][x] += self.noiseLayers[layer].noise[y][x]
		for y in range(self.scale):
			for x in range(self.scale):
				self.noise[y][x] /= self.layers

Perlinnoise = define_perlinnoise(3, 2)