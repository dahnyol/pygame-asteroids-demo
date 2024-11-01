import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        angle = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        smaller_asteroid = self.radius - ASTEROID_MIN_RADIUS

        asteroid_obj = Asteroid(self.position.x, self.position.y, smaller_asteroid)
        asteroid2_obj = Asteroid(self.position.x, self.position.y, smaller_asteroid)

        asteroid_obj.velocity = angle * 1.2
        asteroid2_obj.velocity = angle2 * 1.2