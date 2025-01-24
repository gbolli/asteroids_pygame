import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # instantiate
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        pygame.Surface.fill(screen, (0,0,0))

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()



# TODO: Extending the Project
#
# Add a scoring system
# Implement multiple lives and respawning
# Add an explosion effect for the asteroids
# Add acceleration to the player movement
# Make the objects wrap around the screen instead of disappearing
# Add a background image
# Create different weapon types
# Make the asteroids lumpy instead of perfectly round
# Make the ship have a triangular hit box instead of a circular one
# Add a shield power-up
# Add a speed power-up
# Add bombs that can be dropped