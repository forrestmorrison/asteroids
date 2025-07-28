import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super.__init__(x, y, radius, velocity)

    def draw(self, screen):
        pygame.draw.circle("White", (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt