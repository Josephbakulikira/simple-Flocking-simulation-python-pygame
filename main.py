import pygame
from boid import Boid
from tools import Vector
import math
import random
from matrix import *
white, black = (217, 217, 217), (12, 12, 12)

width, height = 1920, 1080
size=(width, height)

window = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 60

scale = 50
Distance = 5
speed = 0.0005

flock = []
#number of boids
n = 100
#radius of perception of each boid

for i in range(n):
	flock.append(Boid(random.randint(20, width-20), random.randint(20, height-20)))

reset = False
run = True
while run:
	clock.tick(fps)
	window.fill((10, 0 ,10))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False
			if event.key == pygame.K_r:
				reset = True

	if reset == True:
		flock = []
		for i in range(n):
			flock.append(Boid(random.randint(20, width-20), random.randint(20, height-20)))
		reset = False

	for boid in flock:
		boid.limits(width, height)
		boid.behaviour(flock)
		boid.update()
		boid.hue += speed
		boid.Draw(window, Distance, scale)

	pygame.display.update()
pygame.quit()
