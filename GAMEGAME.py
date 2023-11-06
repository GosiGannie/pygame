import pygame
import random
import math

pygame.init()

screen_x = 1200
screen_y = 900

display = pygame.display.set_mode([screen_x, screen_y])

player_x = 600
player_y = 400
player_rect = pygame.Rect(player_x, player_y, 40, 40)

enemy1_x = 300
enemy1_y = 700
enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)

surrounding1_x = random.randint(0, 1140)
surrounding1_y = random.randint(0, 1040)

surrounding2_x = random.randint(0, 1130)
surrounding2_y = random.randint(0, 1300)

left_wall_top_x = 0
left_wall_top_y = 0
left_wall_bottom_x = 0
left_wall_bottom_y = 1100

top_wall_left_x = 0
top_wall_left_y = 0
top_wall_right_x = 1200
top_wall_right_y = 0

right_wall_top_x = 1200
right_wall_top_y = 0
right_wall_bottom_x = 1200
right_wall_bottom_y = 1100

bottom_wall_left_x = 0
bottom_wall_left_y = 1100
bottom_wall_right_x = 1200
bottom_wall_right_y = 1100

inside_x = 0
inside_y = 0
inside_rect = pygame.Rect(inside_x, inside_y, 1200, 1100)



color_player = (47, 94, 161)
enemy_color = (102, 3, 3)
surrounding_color = (22, 71, 15)
wall_color = (72, 74, 72)
inside_color = (70, 107, 50)
bullet_color = (40, 58, 156)

clock = pygame.time.Clock()

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        surrounding1_x -= 3
        surrounding2_x -= 3
        enemy1_x -= 3
        left_wall_top_x -= 3
        left_wall_bottom_x -= 3
        top_wall_right_x -= 3
        top_wall_left_x -= 3
        right_wall_top_x -= 3
        right_wall_bottom_x -= 3
        bottom_wall_right_x -= 3
        bottom_wall_left_x -= 3
        inside_x -= 3
    if keys[pygame.K_a]:
        surrounding1_x += 3
        surrounding2_x += 3
        enemy1_x += 3
        left_wall_top_x += 3
        left_wall_bottom_x += 3
        top_wall_right_x += 3
        top_wall_left_x += 3
        right_wall_top_x += 3
        right_wall_bottom_x += 3
        bottom_wall_right_x += 3
        bottom_wall_left_x += 3
        inside_x += 3
    if keys[pygame.K_s]:
        surrounding1_y -= 3
        surrounding2_y -= 3
        enemy1_y -= 3
        left_wall_top_y -= 3
        left_wall_bottom_y -= 3
        top_wall_right_y -= 3
        top_wall_left_y -= 3
        right_wall_top_y -= 3
        right_wall_bottom_y -= 3
        bottom_wall_right_y -= 3
        bottom_wall_left_y -= 3
        inside_y -= 3
    if keys[pygame.K_w]:
        surrounding1_y += 3
        surrounding2_y += 3
        enemy1_y += 3   
        left_wall_top_y += 3
        left_wall_bottom_y += 3
        top_wall_right_y += 3
        top_wall_left_y += 3
        right_wall_top_y += 3
        right_wall_bottom_y += 3
        bottom_wall_right_y += 3
        bottom_wall_left_y += 3
        inside_y += 3

    dx, dy = player_x - enemy1_x, player_y - enemy1_y
    dist = math.hypot(dx, dy)
    dx, dy = dx / dist, dy / dist

    enemy1_x += dx
    enemy1_y += dy

    enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    inside_rect = pygame.Rect(inside_x, inside_y, 1200, 1100)
    cursor_x, cursor_y = pygame.mouse.get_pos()

    display.fill((30, 20, 0))

    pygame.draw.rect(display, inside_color, inside_rect)
    pygame.draw.rect(display, surrounding_color, (surrounding1_x, surrounding1_y, 60, 60))
    pygame.draw.rect(display, surrounding_color, (surrounding2_x, surrounding2_y, 70, 70))
    pygame.draw.rect(display, enemy_color, enemy_rect)
    pygame.draw.line(display, bullet_color, (player_x + 20, player_y + 20), (cursor_x, cursor_y), 5)
    pygame.draw.rect(display, color_player, player_rect)
    pygame.draw.line(display, wall_color, (left_wall_top_x, left_wall_top_y), (left_wall_bottom_x, left_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (top_wall_left_x, top_wall_left_y), (top_wall_right_x, top_wall_right_y), 10)
    pygame.draw.line(display, wall_color, (right_wall_top_x, right_wall_top_y), (right_wall_bottom_x, right_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (bottom_wall_left_x, bottom_wall_left_y), (bottom_wall_right_x, bottom_wall_right_y), 10)

    pygame.display.update()

    clock.tick(100)

pygame.quit()