import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)
    timer = pygame.time.Clock()
    dt = 0
    user = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for aster in asteroids:
            if aster.collide(user):
                print("Game over!")
                exit()
            for bullet in shots:
                if aster.collide(bullet):
                    bullet.kill()
                    aster.split()
                    break
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()