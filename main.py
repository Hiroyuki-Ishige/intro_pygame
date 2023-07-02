import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_surface = pygame.image.load("graphics/sky.png")

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

    # draw all out elements
    screen.blit(test_surface, (30, 30))  # connect test_surfact to screen

    pygame.display.update()  # update everything
    clock.tick(60)  # set game to refreash 60 times/second at MAX
