import pygame
from boid import Boid
from tools import Vector
import math
import random

white, black = (217, 217, 217), (12, 12, 12)

width, height = 1920, 1080
size=(width, height)

window = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 60

flock = []
#number of boids
n = 50
#radius of perception of each boid

for i in range(n):
	flock.append(Boid(random.randint(20, width-20), random.randint(20, height-20)))


run = True
while run:
	clock.tick(fps)
	window.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for boid in flock:
		boid.limits(width, height)
		boid.behaviour(flock)
		boid.update()
		boid.Draw(window)

	pygame.display.update()
pygame.quit()
