import pygame
from sys import exit
import time


def display_score():
    current_time = int(
        pygame.time.get_ticks() / 1000) - start_time  # "pygame.time.get_tickes() count time spent from when "pygame.init()""
    score_surf = test_font.render(f"{current_time}", False, "white")
    score_rect = score_surf.get_rect(midbottom=(400, 50))
    screen.blit(score_surf, score_rect)

    score_f_surf = test_font.render(f"Score:", False, "white")
    score_f_rect = score_f_surf.get_rect(midbottom=(300, 50))
    screen.blit(score_f_surf, score_f_rect)

    return current_time  # or we can use "global current_time"


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
start_time = 0
current_time = 0

FLAME_RATE = 60  # set refreash times/second

# set text and rectangle
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # Create text

# set text "My game"
game_title_surf = test_font.render("Pixel Runner", True, "#ffffff")  # ("text", smooth(T/F), "font color")
game_title_rect = game_title_surf.get_rect(midbottom=(100, 50))

# set text "Game over"
game_over_surf = test_font.render("Game over", True, "white")
game_over_rect = game_over_surf.get_rect(midbottom=(700, 50))  # original (400, 250)

"""
Import image 
"convert()", and "convert_alpha()" make graphics easier and faster to be handled by pygame
"""
# Import image and rectangle
# TODO to change file to png which has transparent of background. Then, add ".convert_alpha()"
sky_surface = pygame.image.load("graphics/sky_800.jpg").convert()
ground_surface = pygame.image.load("graphics/ground_800.jpg").convert()
bg_surface = pygame.image.load("graphics/bg_black.jpg").convert()

# Obstacles
snail_surf = pygame.image.load("graphics/snail/snail_2.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(800, 300))
#TODO create list of obstacles


player_surf = pygame.image.load("graphics/player/player.png").convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(50, 300))  # set rectangle

# Intro screen
player_stand = pygame.image.load("graphics/player/mario_initial_SC.png").convert_alpha()
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand, -45, 1)  # (image, rotation, scale)
player_stand_rect = player_stand.get_rect(center=(400, 200))

start_inst_surf = test_font.render("Press 'S' to start game", True, "white")
start_inst_rect = start_inst_surf.get_rect(center=(400, 300))

player_gravity = 0
game_active = False

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

        if game_active:
            # (Method 1) event by key press
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
                    # player_rect.y += player_gravity

            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:  # Check if mouse buttom is pressed
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
                    # print(event.pos)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    snail_rect.x = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True

        if event.type == obstacle_timer and game_active:

            print(f'test')


    if game_active:
        # attach image to screen
        screen.blit(bg_surface, (0, 0))
        screen.blit(sky_surface, (50, 50))
        screen.blit(ground_surface, (50, 300))
        screen.blit(game_title_surf, game_title_rect)
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)
        # pygame.draw.line(screen, "white", start_pos=(50, 50), end_pos=pygame.mouse.get_pos(), width=5) #Draw line

        current_time = display_score()


        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300  # set floor of player
        if player_rect.top < 50:
            player_rect.top = 50

        snail_rect.x -= 3
        if snail_rect.left < 50:
            snail_rect.left = 800

        if player_rect.colliderect(snail_rect):  # This will return 0(False) if no collide, 1 if collide (True)
            game_active = False

    else:  # Game_active is False
        # screen.blit(game_over_surf, game_over_rect) #TODO to wait for a while and change screen to initial
        # time.sleep(3)
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)
        if current_time == 0:
            screen.blit(start_inst_surf, start_inst_rect)
        else:
            # set text for score
            ini_score_surf = test_font.render(f"Your last score: {current_time}", False, "white")
            ini_score_rect = ini_score_surf.get_rect(center=(400, 300))

            screen.blit(start_inst_surf, start_inst_surf.get_rect(center=(400, 350)))
            screen.blit(ini_score_surf, ini_score_rect)  # TODO to fix to show score correctly in the initial screen

        # (Method 2) event by a key is pressed
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")
        #
        # # mouse position ------------------------------
        # mouse_pos = pygame.mouse.get_pos()  # Get position of the mouse
        # if player_rect.collidepoint(mouse_pos):
        #     print("collision")
        #     print(pygame.mouse.get_pressed())  # Check if any button of mouse if pressed
        # #-----------------------------------------------

    pygame.display.update()  # update everything
    clock.tick(FLAME_RATE)
