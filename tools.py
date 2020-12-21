from math import sqrt

NEIGHBORHOOD_RADIUS = 50

class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __mul__(self, a):
		self.x = self.x * a
		self.y = self.y * a
		return self

	def __add__(self, a):
		self.x = self.x + a.x
		self.y = self.y + a.y
		return self

	def __sub__(self, a):
		self.x = self.x - a.x
		self.y = self.y - a.y
		return self

	def __truediv__(self, a):
		self.x = self.x / a
		self.y = self.y / a
		return self

	def add(self, a):
		self.x = self.x + a.x
		self.y = self.y + a.y

	def parseToInt(self):
		return (int(self.x), int(self.y))

	def magnitude(self):
		return sqrt(self.x * self.x + self.y * self.y)

	def normalize(self):
		mag = self.magnitude()
		if not (mag == 0 ):
			self = self/mag
	def limit(self, max_length):
		squared_mag = self.magnitude() * self.magnitude()
		if squared_mag > (max_length * max_length):
			self.x = self.x/sqrt(squared_mag)
			self.y = self.y/sqrt(squared_mag)
			self.x = self.x * max_length
			self.y = self.y * max_length
	def reset(self, x=0, y=0):
		self.x = x
		self.y = y


def getDistance(v1, v2):
	return sqrt((v1.x - v2.x)*(v1.x - v2.x) + (v1.y -v2.y)*(v1.y -v2.y))

def AddVectors(v1, v2):
	return Vector(v1.x + v2.x, v1.y + v2.y)

def SubVectors(v1, v2):
	return Vector(v1.x - v2.x, v1.y - v2.y)
