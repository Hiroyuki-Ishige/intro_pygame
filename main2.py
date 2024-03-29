"""
This is code written using class for player and obstacles
"""
import random
import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        self.player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_walk = [self.player_walk_1, self.player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 300))
        self.gravity = 0

        # Sound
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210  # original 210
        if type == "snail":
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))  # original (900, 1100)

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):  # Erase obstacles when it's beyond certail X point
        if self.rect.x <= 50:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

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

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
#
#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surf, obstacle_rect)
#             elif obstacle_rect.bottom == 200:
#                 screen.blit(fly_surf, obstacle_rect)
#
#         obstacle_list = [obstacle for obstacle in obstacle_list if
#                          obstacle.x > 50]  # delete obstacle when is out of screen
#
#         return obstacle_list
#
#     else:
#         return []
#
#
# def collisions(player, obstacles):
#     if obstacles:  # if there is obstacles in the list
#         for obstacle_rect in obstacles:
#             if player.colliderect(obstacle_rect):
#                 return False
#
#     return True

def collitions_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False): #This line create list. Argument "False" does NOT erase obstacles. "True" erase obstacles
        obstacle_group.empty()
        return False
    else:
        return True

# def player_animation():
#     global player_surf, player_index
#     # play walking animation if the player is on floor
#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.05
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]

    # display the jump surface when playe is not on floor


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
start_time = 0
current_time = 0
bg_sound = pygame.mixer.Sound("audio/music.wav")
bg_sound.set_volume(0.1)
bg_sound.play(loops=-1) # -1 is to loop forever

FLAME_RATE = 60  # set refreash times/second

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

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
sky_surface = pygame.image.load("graphics/sky_800.jpg").convert()
ground_surface = pygame.image.load("graphics/ground_800.jpg").convert()
bg_surface = pygame.image.load("graphics/bg_black.jpg").convert()

# Snail
# snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surf = snail_frames[snail_frame_index]
#
# # Fly
# fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
# fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surf = fly_frames[fly_frame_index]
#
# obstacle_rect_list = []
#
# # Player (surf -> rect -> blit)
# player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
# player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()
#
# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(bottomleft=(50, 300))  # set rectangle

# Intro screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand, 0, 1)  # (image, rotation, scale)
player_stand_rect = player_stand.get_rect(center=(400, 200))

start_inst_surf = test_font.render("Press 'S' to start game", True, "white")
start_inst_rect = start_inst_surf.get_rect(center=(400, 300))

# player_gravity = 0
game_active = False

# Timer
obstacle_timer = pygame.USEREVENT + 1  # create custom user event. Ref https://coderslegacy.com/python/pygame-userevents/
pygame.time.set_timer(obstacle_timer, 1500)  # tell pygame to trigger the obstacle_timer event constantly

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:  # This while roop is important to keep screen showing
    for event in pygame.event.get():  # Keep looking all event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # stop system and exit while roop

        # if game_active:
            # (Method 1) event by key press
            # if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
            #     if event.key == pygame.K_SPACE:
            #         player_gravity = -20
            #         # player_rect.y += player_gravity
            #
            # if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:  # Check if mouse buttom is pressed
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity = -20
            #         # print(event.pos)
        # else:
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True

        if game_active:
            if event.type == obstacle_timer:
                obstacles = ["fly", "snail", "snail", "snail"]
                rand_obstacle = random.choice(obstacles)
                obstacle_group.add(Obstacle(rand_obstacle))

                # create obstacles NOT using class
                # if randint(0, 2):  # generate randum 0 = false or 1 = True and judge if True
                #     obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(800, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(800, 1100), 200)))

            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0:
            #         snail_frame_index = 1
            #     else:
            #         snail_frame_index = 0
            #     snail_surf = snail_frames[snail_frame_index]
            #
            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0:
            #         fly_frame_index = 1
            #     else:
            #         fly_frame_index = 0
            #     fly_surf = fly_frames[fly_frame_index]

    if game_active:
        # attach image to screen
        screen.blit(bg_surface, (0, 0))
        screen.blit(sky_surface, (50, 50))
        screen.blit(ground_surface, (50, 300))
        screen.blit(game_title_surf, game_title_rect)
        # screen.blit(snail_surf, snail_rect)

        # pygame.draw.line(screen, "white", start_pos=(50, 50), end_pos=pygame.mouse.get_pos(), width=5) #Draw line

        current_time = display_score()

        # Player
        # Create player by NOT using Class
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom > 300:
        #     player_rect.bottom = 300  # set floor of player
        # if player_rect.top < 50:
        #     player_rect.top = 50
        #
        # player_animation()
        # screen.blit(player_surf, player_rect)

        player.draw(screen)
        player.update()

        # Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collitions_sprite()
        # if player_rect.colliderect(snail_rect):  # This will return 0(False) if no collide, 1 if collide (True)
        #     game_active = False
        # game_active = collisions(player=player_rect,
        #                          obstacles=obstacle_rect_list)  # This will return 0(False) if no collide, 1 if collide (True)

    else:  # Game_active is False
        # TODO to wait for a while and change screen to initial

        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)

        # set obstacles and player at initial position
        # obstacle_rect_list.clear()

        # player_rect.bottomleft = (50, 300)
        #
        if current_time == 0:
            screen.blit(start_inst_surf, start_inst_rect)
        else:
            # set text for score
            ini_score_surf = test_font.render(f"Your last score: {current_time}", False, "white")
            ini_score_rect = ini_score_surf.get_rect(center=(400, 300))

            screen.blit(start_inst_surf, start_inst_surf.get_rect(center=(400, 350)))
            screen.blit(ini_score_surf, ini_score_rect)

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

# TODO clear up code in main2.py file
