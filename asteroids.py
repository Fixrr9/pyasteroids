import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rAngle = random.uniform(20,50)
        r1 = self.velocity.rotate(rAngle)
        r2 = self.velocity.rotate(-rAngle)
        rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0],self.position[1],rad)
        ast2 = Asteroid(self.position[0],self.position[1],rad)
        ast1.velocity = r1 * 1.2
        ast2.velocity = r2 * 1.2