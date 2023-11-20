import pygame
import random
import math
from dataclasses import dataclass
from typing import List

pygame.init()

@dataclass
class Color():
    r: int
    g: int
    b: int

    def get_color(self) -> (int, int, int):
        return (self.r, self.g, self.b)
    
@dataclass
class Coordinate:
    x: int
    y: int

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

RELOAD_DELAY_TYPE1 = 600
last_shot = pygame.time.get_ticks()

class Projectile():
    def __init__(self, start_pos: Coordinate, direction: float, speed: int, color: Color):
        self.size = (15, 15)
        self.direction = direction
        self.speed = speed
        self.color = color
        self.hitbox = pygame.Rect(start_pos, self.size)

    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x += diff_x
        self.hitbox.y += diff_y
        return self
    
    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), self.hitbox)
        return self
    
    def move(self, diff_x, diff_y):
        self.hitbox.x += diff_x
        self.hitbox.y += diff_y

projectiles: List[Projectile] = []


color_player = (47, 94, 161)
enemy_color = (102, 3, 3)
surrounding_color = (22, 71, 15)
wall_color = (72, 74, 72)
inside_color = (65, 122, 54)
health_color_red = (100, 0, 0)
health_color_green = (38, 196, 8)
projectile_color = Color(47, 94, 161)

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
        [p.move(-3, 0) for p in projectiles]

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
        [p.move(3, 0) for p in projectiles]

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
        [p.move(0, -3) for p in projectiles]

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
        [p.move(0, 3) for p in projectiles]


    enemy_dx, enemy_dy = player_x - enemy1_x, player_y - enemy1_y
    enemy_dist = math.hypot(enemy_dx, enemy_dy)
    enemy_dx, enemy_dy = enemy_dx / enemy_dist, enemy_dy / enemy_dist

    enemy1_x += enemy_dx
    enemy1_y += enemy_dy

    enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    inside_rect = pygame.Rect(inside_x, inside_y, 1200, 1100)
    
    cursor_x, cursor_y = pygame.mouse.get_pos()
    cursor_rect = pygame.Rect(cursor_x - 10, cursor_y - 10, 20, 20)

    

    if player_rect.colliderect(enemy_rect):
        player_health_width -= 0.35
    if player_health_width < 35:
        health_color_green = (182, 191, 0)
    if player_health_width < 20:
        health_color_green = (204, 22, 2)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed():
            now = pygame.time.get_ticks()
            if (now > last_shot + RELOAD_DELAY_TYPE1):
                (dx, dy) = pygame.mouse.get_pos() - pygame.Vector2(player_rect.center)
                angle = math.atan2(dy, dx)
                projectile = Projectile(player_rect.center, angle, 6, projectile_color)
                projectiles.append(projectile)
                last_shot = now
            else:
                pass

    
    player_health_rect = pygame.Rect(player_health_x, player_health_y, player_health_width, player_health_height)

    display.fill((30, 20, 0))

    pygame.draw.rect(display, inside_color, inside_rect)
    pygame.draw.rect(display, surrounding_color, (surrounding1_x, surrounding1_y, 60, 60))
    pygame.draw.rect(display, surrounding_color, (surrounding2_x, surrounding2_y, 70, 70))
    pygame.draw.rect(display, enemy_color, enemy_rect)
    pygame.draw.rect(display, color_player, player_rect)
    pygame.draw.line(display, wall_color, (left_wall_top_x, left_wall_top_y), (left_wall_bottom_x, left_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (top_wall_left_x, top_wall_left_y), (top_wall_right_x, top_wall_right_y), 10)
    pygame.draw.line(display, wall_color, (right_wall_top_x, right_wall_top_y), (right_wall_bottom_x, right_wall_bottom_y), 10)
    pygame.draw.line(display, wall_color, (bottom_wall_left_x, bottom_wall_left_y), (bottom_wall_right_x, bottom_wall_right_y), 10)
    pygame.draw.rect(display, health_color_red, player_health_rect_red)
    pygame.draw.rect(display, health_color_green, player_health_rect)
    [p.update().draw(display) for p in projectiles]

    pygame.display.update()

    clock.tick(90)

pygame.quit()