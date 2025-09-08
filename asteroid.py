import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector_A = self.velocity.rotate(random_angle)
            new_vector_B = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_A = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_A.velocity = new_vector_A * 1.2
            
            asteroid_B = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_B.velocity = new_vector_B * 1.2
