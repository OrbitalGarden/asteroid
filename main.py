import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       screen.fill((0,0,0))
       Player.draw(player, screen)
       pygame.display.flip()
       pygame.time.Clock.tick(clock, 60.0)
       dt = pygame.time.Clock.tick(clock) / 1000


if __name__ == "__main__":
    main()
