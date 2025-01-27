#!/usr/bin/env python3
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()   
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable) 
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updt in updatable:
            updt.update(dt)

        for astr in asteroids:
            for sh in shots:
                if astr.hasCollided(sh):
                    sh.kill()
                    astr.split()
            if astr.hasCollided(player):
                print("Game over!")
                exit(0)
                
        screen.fill("black")
        
        for drw in drawable:
            drw.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            print("Finished!")
            exit(0)
    

if __name__ == "__main__":
    main()