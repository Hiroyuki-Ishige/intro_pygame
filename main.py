import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

FLAME_RATE = 60  # set refreash times/second

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # Create text
text_surface = test_font.render("My game", True, "white")

"""
Import image 
"convert()", and "convert_alpha()" make graphics easier and faster to be handled by pygame
"""
sky_surface = pygame.image.load("graphics/sky(800).jpg").convert()  # Import image
ground_surface = pygame.image.load("graphics/ground(800).jpg").convert()  # Import image
snail_surface = pygame.image.load("graphics/snail/snail_2.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(800, 300))

# snail_x_pos = 750

player_surface = pygame.image.load("graphics/player/player.png").convert_alpha()  # import image
player_rect = player_surface.get_rect(bottomleft=(50, 300))  # set rectanble

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

    # draw all out elements
    screen.blit(text_surface, (0, 0))  # attach image to screen
    screen.blit(sky_surface, (50, 50))  # attach image to screen
    screen.blit(ground_surface, (50, 300))  # attach image to screen
    screen.blit(snail_surface, snail_rect)  # attach image to screen
    screen.blit(player_surface, player_rect)  # attach image to screen

    # snail_x_pos -= 2
    snail_rect.left -=1
    player_rect.left +=1


    if snail_rect.left < 0:
        snail_rect.left = 800

    pygame.display.update()  # update everything
    clock.tick(FLAME_RATE)
