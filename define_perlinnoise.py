import random, math
from User.define_user import User

class define_noise:
	def update_vectors(self):
		increase = 360 / 10 / User.affectiveFPS
		for y in range(self.segments + 1):
			if len(self.vectors) <= y:
				self.vectors.append([])
			for x in range(self.segments + 1):
				if len(self.vectors[y]) <= x:
					self.vectors[y].append(random.randint(0, 359))
				else:
					self.vectors[y][x] += increase
					if self.vectors[y][x] >= 360:
						self.vectors[y][x] = self.vectors[y][x] - 360
	
	def smooth_step(self, variable):
		smooth = variable ** 2 * (3 - variable * 2)
		if smooth < 0:
			return 0
		if smooth > 1:
			return 1
		return smooth

	def update_noise(self):
		vectors = []
		for y in range(self.segments + 1):
			vectors.append([])
			for x in range(self.segments + 1):
				vector = math.radians(self.vectors[y][x])
				vectors[y].append([math.cos(vector), math.sin(vector)])

		segmentScale = self.scale / self.segments
		for column in range(self.scale):
			y = self.smooth_step((column / segmentScale) % 1)
			yVector = int(column / segmentScale)
			for row in range(self.scale):
				x = self.smooth_step((row / segmentScale) % 1)
				xVector = int(row / segmentScale)

				topLeft = x * vectors[yVector][xVector][0] + y * vectors[yVector][xVector][1]
				topRight = -(1 - x) * vectors[yVector][xVector + 1][0] + y * vectors[yVector][xVector + 1][1]
				top = (1 - x) * topLeft + x * topRight

				bottomLeft = x * vectors[yVector + 1][xVector][0] - (1 - y) * vectors[yVector + 1][xVector][1]
				bottomRight = -(1 - x) * vectors[yVector + 1][xVector + 1][0] - (1 - y) * vectors[yVector + 1][xVector + 1][1]
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
	def update_layers(self):
		self.noise = []
		for y in range(self.scale):
			self.noise.append([])
			for x in range(self.scale):
				self.noise[y].append(0)

		for layer in range(self.layers):
			if len(self.noiseLayers) <= layer:
				self.noiseLayers.append(define_noise(self.segments + layer * self.increase, self.scale))
			else:
				self.noiseLayers[layer].segments = self.segments + layer * self.increase
				self.noiseLayers[layer].update_vectors()
				self.noiseLayers[layer].update_noise()
			for y in range(self.scale):
				for x in range(self.scale):
					self.noise[y][x] += self.noiseLayers[layer].noise[y][x]
		for y in range(self.scale):
			for x in range(self.scale):
				self.noise[y][x] /= self.layers

	def __init__(self, layers, increase):
		self.scale = 100

		self.segments = 3
		self.layers = layers
		self.increase = increase
		self.noiseLayers = []
		self.update_layers()

		self.changing = "Segments"

Perlinnoise = define_perlinnoise(2, 5)