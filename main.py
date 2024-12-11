import pygame

pygame.init()

YELLOW = (255, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#muss innerhalb der while loop sein#
# Changing screen color
#screen.fill(YELLOW)

# Player control
player = pygame.Rect(300, 350, 50, 50)
player_speed = 3
player_velocity_y = 0
gravity = 0.1
jump_strength = -10
ground = SCREEN_HEIGHT - player.height

clock = pygame.time.Clock()

# Main game loop
while True:

    # Changing screen color
    screen.fill(YELLOW)
    
    pygame.draw.rect(screen, RED, player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and player.left > 0: 
        player.move_ip(-player_speed, 0)
    if key[pygame.K_d] and player.right < SCREEN_WIDTH:
        player.move_ip(player_speed, 0)
    if key[pygame.K_w] and player.top > 0:  
        player.move_ip(0, -player_speed)
    if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0, player_speed)
    if key[pygame.K_SPACE] and player.bottom >= SCREEN_HEIGHT:
        player_velocity_y = jump_strength

    # Gravity
    player_velocity_y += gravity
    player.y += player_velocity_y

    # Ground Collision
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
        player_velocity_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

    clock.tick(60)