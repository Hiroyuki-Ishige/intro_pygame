import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

FLAME_RATE = 60  # set refreash times/second

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # Create text
text_surf = test_font.render("My game", True, "#ffffff")
score_surf = test_font.render("Score", True, "white")
score_rect = score_surf.get_rect(midbottom=(400, 50))
"""
Import image 
"convert()", and "convert_alpha()" make graphics easier and faster to be handled by pygame
"""
sky_surface = pygame.image.load("graphics/sky(800).jpg").convert()  # Import image
ground_surface = pygame.image.load("graphics/ground(800).jpg").convert()  # Import image
snail_surf = pygame.image.load("graphics/snail/snail_2.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(800, 300))

# snail_x_pos = 750

player_surf = pygame.image.load("graphics/player/player.png").convert_alpha()  # import image
player_rect = player_surf.get_rect(bottomleft=(50, 300))  # set rectangle

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

        # if event.type == pygame.MOUSEMOTION: #Check if mouse is moved
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

    # draw all out elements
    screen.blit(text_surf, (0, 0))  # attach image to screen
    screen.blit(sky_surface, (50, 50))  # attach image to screen
    screen.blit(ground_surface, (50, 300))  # attach image to screen
    screen.blit(snail_surf, snail_rect)  # attach image to screen
    screen.blit(player_surf, player_rect)  # attach image to screen
    pygame.draw.rect(screen, "#c0e8ec", score_rect)

    # pygame.draw.line(screen, "white", start_pos=(50, 50), end_pos=pygame.mouse.get_pos(), width=5) #Draw line
    screen.blit(score_surf, score_rect)

    # print(snail_rect.left)
    snail_rect.x -= 3
    player_rect.x += 1

    if snail_rect.left < 50: snail_rect.left = 800

    # if player_rect.colliderect(snail_rect): #This will return 0(False) if no collide, 1 if collide (True)
    #     print("collision")

#TODO to set jump when space key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump")

    # mouse position ------------------------------
    mouse_pos = pygame.mouse.get_pos()  # Get position of the mouse
    if player_rect.collidepoint(mouse_pos):
        print("collision")
        print(pygame.mouse.get_pressed())  # Check if any button of mouse if pressed
    #-----------------------------------------------

    pygame.display.update()  # update everything
    clock.tick(FLAME_RATE)
