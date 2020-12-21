import pygame
from tools import Vector, getDistance, NEIGHBORHOOD_RADIUS,SubVectors
from random import uniform
import colorsys

# def hsvToRGB(h, s, v):
# 	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

class Boid:
	def __init__(self, x, y):
		self.position = Vector(x, y)
		vec_x = uniform(-1, 1)
		vec_y = uniform(-1, 1)
		self.velocity = Vector(vec_x, vec_y)
		self.velocity.normalize()
		#set a random magnitude
		self.velocity = self.velocity * uniform(1.5, 4)
		self.acceleration = Vector()
		self.color = (12,12,12)
		self.max_speed = 3
		self.max_length = 1

	def limits(self, width , height):
		if self.position.x > width:
			self.position.x = 0
		elif self.position.x < 0:
			self.position.x = width

		if self.position.y > height:
			self.position.y = 0
		elif self.position.y < 0:
			self.position.y = height

	def behaviour(self, flock):
		self.acceleration.reset()
		avoid = self.separation(flock)
		align = self.alignment(flock)
		coh = self.cohesion(flock)
		self.acceleration.add(avoid)
		self.acceleration.add(align)
		self.acceleration.add(coh)

	def separation(self, flockMates):
		total = 0
		steering = Vector()

		for mate in flockMates:
			dist = getDistance(self.position, mate.position)
			if mate is not self and dist < NEIGHBORHOOD_RADIUS:
				temp = SubVectors(self.position,mate.position)
				temp = temp/dist
				steering.add(temp)
				total += 1

		if total > 0:
			steering = steering / total
			# steering = steering - self.position
			steering.normalize()
			steering = steering * self.max_speed
			steering = steering - self.velocity
			steering.limit(self.max_length)

		return steering
	def alignment(self, flockMates):
		total = 0
		steering = Vector()
		# hue = uniform(0, 0.5)
		for mate in flockMates:
			dist = getDistance(self.position, mate.position)
			if mate is not self and dist < NEIGHBORHOOD_RADIUS:
				steering.add(mate.velocity)
				mate.color = (110, 48, 20)
				total += 1

		if total > 0:
			steering = steering / total
			steering.normalize()
			steering = steering * self.max_speed
			steering = steering - self.velocity
			steering.limit(self.max_length)
		return steering

	def cohesion(self, flockMates):
		total = 0
		steering = Vector()

		for mate in flockMates:
			dist = getDistance(self.position, mate.position)
			if mate is not self and dist < NEIGHBORHOOD_RADIUS:
				steering.add(mate.position)
				total += 1

		if total > 0:
			steering = steering / total
			steering = steering - self.position
			steering.normalize()
			steering = steering * self.max_speed
			steering = steering - self.velocity
			steering.limit(self.max_length)

		return steering

	def update(self):

		self.position = self.position + self.velocity
		self.velocity = self.velocity + self.acceleration
		self.velocity.limit(self.max_speed)

	def Draw(self, screen):
		pygame.draw.circle(screen, self.color, self.position.parseToInt(), 10)
