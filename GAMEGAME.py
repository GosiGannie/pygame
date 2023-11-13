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

player_health_x = player_x - 7
player_health_y = player_y + 46
player_health_width = 54
player_health_height = 7
player_health_rect = pygame.Rect(player_health_x, player_health_y, player_health_width, player_health_height)

player_health_rect_red = pygame.Rect(player_health_x, player_health_y, 54, player_health_height)

enemy1_x = 300
enemy1_y = 700
enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)

surrounding1_x = random.randint(0, 1140)
surrounding1_y = random.randint(0, 1040)

surrounding2_x = random.randint(0, 1130)
surrounding2_y = random.randint(0, 1030)

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

cursor_x, cursor_y = pygame.mouse.get_pos()
projectile_x = cursor_x
projectile_y = cursor_y
projectile_rect = pygame.Rect(projectile_x, projectile_y, 20, 20)

projectile_list = []

click_count = 0

#bullets = []

#class Bullet():
 #   def __init__(self, bullet_x, bullet_y, bullet_speed):    
  #      self.bullet_x = bullet_x
   #     self.bullet_y = bullet_y
    #    self.bullet_speed
    #def draw_bullet(self, surface):
     #   bullet_dx, bullet_dy = cursor_x - player_x, cursor_y - player_y
      #  bullet_dist = math.hypot(bullet_dx, bullet_dy)
       # bullet_dx, bullet_dy = bullet_dx / bullet_dist, bullet_dy / bullet_dist
        #pygame.draw.rect(display, bullet_color, bullet_rect)
#bullet_width_height = 3
#bullet_rect = pygame.Rect(bullet_x + 20, bullet_y + 20, bullet_width_height, bullet_width_height)

color_player = (47, 94, 161)
enemy_color = (102, 3, 3)
surrounding_color = (22, 71, 15)
wall_color = (72, 74, 72)
inside_color = (65, 122, 54)
projectile_color = (40, 58, 156)
health_color_red = (100, 0, 0)
health_color_green = (38, 196, 8)

objects_x = [surrounding1_x, surrounding2_x, enemy1_x, left_wall_top_x, left_wall_bottom_x, top_wall_right_x, top_wall_left_x, right_wall_top_x, right_wall_bottom_x, bottom_wall_right_x, bottom_wall_left_x, inside_x, projectile_x]
objects_y = [surrounding1_y, surrounding2_y, enemy1_y, left_wall_top_y, left_wall_bottom_y, top_wall_right_y, top_wall_left_y, right_wall_top_y, right_wall_bottom_y, bottom_wall_right_y, bottom_wall_left_y, inside_y, projectile_y]

cursor_x, cursor_y = pygame.mouse.get_pos()
cursor_rect = pygame.Rect(cursor_x - 10, cursor_y - 10, 20, 20)
projectile_rect = pygame.Rect(projectile_x, projectile_y, 20, 20)

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
        projectile_x -= 3
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
        projectile_x += 3
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
        projectile_y -= 3
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
        projectile_y += 3

    dx, dy = player_x - enemy1_x, player_y - enemy1_y
    dist = math.hypot(dx, dy)
    dx, dy = dx / dist, dy / dist

    enemy1_x += dx
    enemy1_y += dy

    enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    inside_rect = pygame.Rect(inside_x, inside_y, 1200, 1100)
    

    #cursor_rect = pygame.Rect(cursor_x - 10, cursor_y - 10, 20, 20)

    

    if player_rect.colliderect(enemy_rect):
        player_health_width -= 0.35
    if player_health_width < 35:
        health_color_green = (182, 191, 0)
    if player_health_width < 20:
        health_color_green = (204, 22, 2)
    
#    if event.type == pygame.MOUSEBUTTONDOWN:

        #left = pygame.mouse.get_pressed()
        #if left:
         #   click_count += 1
          #  print('its working', click_count)
           # pygame.draw.rect(display, projectile_color, projectile_rect)

 #   if pygame.MOUSEBUTTONDOWN == True:
  #      bullet.draw_bullet(display)
    
    player_health_rect = pygame.Rect(player_health_x, player_health_y, player_health_width, player_health_height)

    display.fill((30, 20, 0))

    pygame.draw.rect(display, inside_color, inside_rect)
    pygame.draw.rect(display, surrounding_color, (surrounding1_x, surrounding1_y, 60, 60))
    pygame.draw.rect(display, surrounding_color, (surrounding2_x, surrounding2_y, 70, 70))
    pygame.draw.rect(display, enemy_color, enemy_rect)
   # pygame.draw.line(display, bullet_color, (player_x + 20, player_y + 20), (cursor_x, cursor_y), 5)
    #pygame.draw.rect(display, projectile_color, projectile_rect)
    pygame.draw.rect(display, color_player, player_rect)
    pygame.draw.rect(display, health_color_red, player_health_rect_red)
    pygame.draw.rect(display, health_color_green, player_health_rect)
    pygame.draw.line(display, wall_color, (left_wall_top_x, left_wall_top_y), (left_wall_bottom_x, left_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (top_wall_left_x, top_wall_left_y), (top_wall_right_x, top_wall_right_y), 10)
    pygame.draw.line(display, wall_color, (right_wall_top_x, right_wall_top_y), (right_wall_bottom_x, right_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (bottom_wall_left_x, bottom_wall_left_y), (bottom_wall_right_x, bottom_wall_right_y), 10)
    #pygame.draw.rect(display, projectile_color, cursor_rect)
    pygame.draw.rect(display, projectile_color, cursor_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(display, projectile_color, projectile_rect)
            #projectile_list.append(cursor_rect)
            for i in range(2):
                projectile_list.append(cursor_rect)
            print(projectile_list)
            projectile_list.pop(0)
    

    pygame.display.update()

    clock.tick(100)

pygame.quit()