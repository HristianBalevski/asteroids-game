import random
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    pl = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
                    if new_radius >= ASTEROID_MIN_RADIUS:
                        random_angle = random.uniform(20, 50)
                        v1 = asteroid.velocity.rotate(+random_angle) * 1.2
                        v2 = asteroid.velocity.rotate(-random_angle) * 1.2
                        a1 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                        a1.velocity = v1
                        a2 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                        a2.velocity = v2
                    asteroid.kill()
                    shot.kill()

        for asteroid in asteroids:
            if asteroid.collides_with(pl):
                print("Game over!")
                pygame.quit()
                return

        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
 
