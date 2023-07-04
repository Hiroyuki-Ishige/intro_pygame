import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # Create text

text_surface = test_font.render("My game", True, "white")
sky_surface = pygame.image.load("graphics/sky(800).jpg")  # Import image
ground_surface = pygame.image.load("graphics/ground(800).jpg")  # Import image
snail_surface = pygame.image.load("graphics/snail_2.png")  # Import image
snail_x_pos = 750

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

    # draw all out elements
    screen.blit(text_surface, (0, 0))  # attach image to screen
    screen.blit(sky_surface, (30, 30))  # attach image to screen
    screen.blit(ground_surface, (30, 300))  # attach image to screen
    screen.blit(snail_surface, (snail_x_pos, 250))  # attach image to screen
    snail_x_pos -= 1

    if snail_x_pos < 0:
        snail_x_pos = 750

    pygame.display.update()  # update everything
    clock.tick(60)  # set game to refreash 60 times/second at MAX
