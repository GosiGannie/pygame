import pygame
import random
import math
from dataclasses import dataclass
from typing import List

pygame.init()

screen_x = 1200
screen_y = 900

display = pygame.display.set_mode([screen_x, screen_y])

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


#Colors
color_player = Color(47, 94, 161)
enemy_color = Color(102, 3, 3)
surrounding_color = (22, 71, 15)
wall_color = (72, 74, 72)
inside_color = (65, 122, 54)
health_color_red = (100, 0, 0)
health_color_green = (38, 196, 8)
projectile_color = Color(47, 94, 161)


#playerwhatewe


#Surroundings
surrounding1_x = random.randint(-100, 1240)
surrounding1_y = random.randint(-100, 940)

surrounding2_x = random.randint(-100, 1230)
surrounding2_y = random.randint(-100, 930)

surrounding3_x = random.randint(-100, 1240)
surrounding3_y = random.randint(-100, 940)

surrounding4_x = random.randint(-100, 1230)
surrounding4_y = random.randint(-100, 930)

surrounding5_x = random.randint(-100, 1240)
surrounding5_y = random.randint(-100, 940)

surrounding6_x = random.randint(-100, 1230)
surrounding6_y = random.randint(-100, 930)

#Walls
left_wall_top_x = -100
left_wall_top_y = -100
left_wall_bottom_x = -100
left_wall_bottom_y = 1000

top_wall_left_x = -100
top_wall_left_y = -100
top_wall_right_x = 1300
top_wall_right_y = -100

right_wall_top_x = 1300
right_wall_top_y = -100
right_wall_bottom_x = 1300
right_wall_bottom_y = 1000

bottom_wall_left_x = -100
bottom_wall_left_y = 1000
bottom_wall_right_x = 1300
bottom_wall_right_y = 1000


inside_x = -100
inside_y = -100


class Player:
    def __init__(self, x: int, y: int, width: int, height: int, color: Color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), self.rect)

player = Player(600, 450, 40, 40, color_player)


class Enemy():
    def __init__(self, x: int, y: int, width: int, height: int, color: Color, direction: float, speed: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = direction
        self.speed = speed

    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), (self.hitbox.x + display_scroll[0], self.hitbox.y + display_scroll[1], self.width, self.height))
        return self

    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x -= diff_x
        self.hitbox.y -= diff_y
        return self
    
    def move(self, diff_x, diff_y):
        self.hitbox.x -= diff_x
        self.hitbox.y -= diff_y

enemies: List[Enemy] = []

RELOAD_DELAY_TYPE2 = 1000
last_enemy_spawn = pygame.time.get_ticks()


class Projectile():
    def __init__(self, start_pos: Coordinate, direction: float, speed: int, color: Color):
        self.size = (15, 15)
        self.direction = direction
        self.speed = speed
        self.color = color
        self.hitbox = pygame.rect.Rect(start_pos, self.size)
    
    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), self.hitbox)
        return self
    
    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x += diff_x
        self.hitbox.y += diff_y
        return self

    def move(self, diff_x, diff_y):
        self.hitbox.x += diff_x
        self.hitbox.y += diff_y

projectiles: List[Projectile] = []  

RELOAD_DELAY_TYPE1 = 600
last_shot = pygame.time.get_ticks()


#Time
FPS = 90

clock = pygame.time.Clock()


display_scroll = [0, 0]

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #General movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        display_scroll[0] -=3

    if keys[pygame.K_a]:
        display_scroll[0] += 3

    if keys[pygame.K_s]:
        display_scroll[1] -= 3

    if keys[pygame.K_w]:
        display_scroll[1] += 3
    

    now = pygame.time.get_ticks()

    #Enemy moveent
    if RELOAD_DELAY_TYPE2 < now + last_enemy_spawn:
        enemy = Enemy(random.randint(-100, 1200), random.randint(-100, 900), 30, 30, enemy_color, 0.0, 3)
        (enemy_dx, enemy_dy) = (enemy.x, enemy.y) - pygame.Vector2(600, 450)
        enemy_angle = math.atan2(enemy_dy, enemy_dx)
        enemy.direction = enemy_angle
        #enemy = Enemy(random.randint(-100, 1200), random.randint(-100, 900), 30, 30, enemy_color, enemy_angle, 3)
        enemies.append(enemy)
        now = last_enemy_spawn

    else:
        pass



    inside_rect = pygame.Rect(inside_x + display_scroll[0], inside_y + display_scroll[1], 1400, 1100)

    #if player_rect.colliderect(enemy_rect):
    #    player_health_width -= 0.35
    #if player_health_width < 35:
     #   health_color_green = (182, 191, 0)
    #if player_health_width < 20:
        #health_color_green = (204, 22, 2)



    #prijectile movement


    #Draws
    display.fill((30, 20, 0))
    pygame.draw.rect(display, inside_color, inside_rect)
    pygame.draw.rect(display, surrounding_color, (surrounding1_x + display_scroll[0], surrounding1_y + display_scroll[1], 60, 60))
    pygame.draw.rect(display, surrounding_color, (surrounding2_x + display_scroll[0], surrounding2_y + display_scroll[1], 70, 70))
    pygame.draw.rect(display, surrounding_color, (surrounding3_x + display_scroll[0], surrounding3_y + display_scroll[1], 30, 30))
    pygame.draw.rect(display, surrounding_color, (surrounding4_x + display_scroll[0], surrounding4_y + display_scroll[1], 40, 40))   
    pygame.draw.rect(display, surrounding_color, (surrounding5_x + display_scroll[0], surrounding5_y + display_scroll[1], 50, 50))
    pygame.draw.rect(display, surrounding_color, (surrounding6_x + display_scroll[0], surrounding6_y + display_scroll[1], 70, 70))
    for enemy in enemies:
        enemy.update().draw(display)
    player.draw(display)
    pygame.draw.line(display, wall_color, (left_wall_top_x + display_scroll[0], left_wall_top_y + display_scroll[1]), (left_wall_bottom_x + display_scroll[0], left_wall_bottom_y + display_scroll[1]), 10)
    pygame.draw.line(display, wall_color, (top_wall_left_x + display_scroll[0], top_wall_left_y + display_scroll[1]), (top_wall_right_x + display_scroll[0], top_wall_right_y + display_scroll[1]), 10)
    pygame.draw.line(display, wall_color, (right_wall_top_x + display_scroll[0], right_wall_top_y + display_scroll[1]), (right_wall_bottom_x + display_scroll[0], right_wall_bottom_y + display_scroll[1]), 10)
    pygame.draw.line(display, wall_color, (bottom_wall_left_x + display_scroll[0], bottom_wall_left_y + display_scroll[1]), (bottom_wall_right_x + display_scroll[0], bottom_wall_right_y + display_scroll[1]), 10)
   # pygame.draw.rect(display, health_color_red, player_health_rect_red)
   # pygame.draw.rect(display, health_color_green, player_health_rect)
    [p.update().draw(display) for p in projectiles]


    pygame.display.update()

    clock.tick(FPS)

pygame.quit()