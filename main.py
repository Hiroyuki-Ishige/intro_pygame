import pygame
from sys import exit


def display_score():
    current_time = int(
        pygame.time.get_ticks() / 1000) - start_time  # "pygame.time.get_tickes() count time spent from when "pygame.init()""
    score_surf = test_font.render(f"{current_time}", False, "white")
    score_rect = score_surf.get_rect(midbottom=(400, 50))
    screen.blit(score_surf, score_rect)

    score_f_surf = test_font.render(f"Score:", False, "white")
    score_f_rect = score_f_surf.get_rect(midbottom=(300, 50))
    screen.blit(score_f_surf, score_f_rect)

    print(current_time)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
start_time = 0

FLAME_RATE = 60  # set refreash times/second

# set text and rectangle
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # Create text

# set text "My game"
text_surf = test_font.render("My game", True, "#ffffff")
text_rect = text_surf.get_rect(midbottom=(100, 50))

# set text "Game over"
game_over_surf = test_font.render("Game over", True, "white")
game_over_rect = game_over_surf.get_rect(midbottom=(400, 250))

"""
Import image 
"convert()", and "convert_alpha()" make graphics easier and faster to be handled by pygame
"""
# Import image and rectangle
sky_surface = pygame.image.load("graphics/sky_800.jpg").convert()
ground_surface = pygame.image.load("graphics/ground_800.jpg").convert()
bg_surface = pygame.image.load("graphics/bg_black.jpg").convert()

snail_surf = pygame.image.load("graphics/snail/snail_2.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(800, 300))

player_surf = pygame.image.load("graphics/player/player.png").convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(50, 300))  # set rectangle

player_gravity = 0

game_active = True

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

    if game_active:
        # attach image to screen
        screen.blit(bg_surface, (0, 0))
        screen.blit(sky_surface, (50, 50))
        screen.blit(ground_surface, (50, 300))
        screen.blit(text_surf, text_rect)
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)
        # pygame.draw.line(screen, "white", start_pos=(50, 50), end_pos=pygame.mouse.get_pos(), width=5) #Draw line

        display_score()

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

    else:
        screen.blit(game_over_surf, game_over_rect) #TODO to wait for a while and change screen to initial

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
