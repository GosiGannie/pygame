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
class Display_scroll:
    x: int
    y: int

display_scroll = Display_scroll(0, 0)

#Colors
color_player = Color(47, 94, 161)
enemy_color = Color(102, 3, 3)
surrounding_color = (22, 71, 15)
wall_color = (72, 74, 72)
inside_color = (65, 122, 54)
health_color_red = Color(100, 0, 0)
health_color_green = Color(38, 196, 8)
projectile_color = Color(47, 94, 161)
start_button_color = (255, 255, 255)
restart_button_color = (255, 255, 255)
quit_button_color = (255, 255, 255)
title_color = (255, 255, 255)


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


inside_x = -100
inside_y = -100


#Start screen rects
start_button_rect = pygame.Rect(515, 455, 170, 85)
outline_rect = pygame.Rect(30, 30, screen_x - 60, screen_y - 60)

#Game over rects
restart_button_rect = pygame.Rect(280, 454, 243, 90)
quit_button_rect = pygame.Rect(720, 454, 165, 90)


class Player:
    def __init__(self, x: int, y: int, width: int, height: int, player_color: Color, max_hp: int, current_hp: int, health_bar_length: int, health_bar_color: Color, display_scroll: Display_scroll):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_color = player_color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.health_bar_lenth = health_bar_length
        self.health_ratio = self.max_hp / self.health_bar_lenth
        self.health_bar_color = health_bar_color
        self.display_scroll = display_scroll
    
    def draw(self, display):
        pygame.draw.rect(display, (self.player_color.r, self.player_color.g, self.player_color.b), self.rect)
        
    def take_damage(self, amount: int):
        if self.current_hp > 0:
            self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0

    def get_healing(self, amount: float):
        if self.current_hp < self.max_hp:
            self.current_hp += amount
        if self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp

    def draw_health_bar(self, display):
        pygame.draw.rect(display, (self.health_bar_color.r, self.health_bar_color.g, self.health_bar_color.b), (20, 20, self.current_hp / self.health_ratio, 35))
        pygame.draw.rect(display, (255, 255, 255), (20, 20, self.health_bar_lenth, 35), 4)

player = Player(600, 450, 50, 50, color_player, 400, 400, 400, health_color_green, display_scroll)

RELOAD_DELAY_TYPE3 = 2000
last_healing = pygame.time.get_ticks()


class Enemy():
    def __init__(self, x: int, y: int, width: int, height: int, color: Color, direction: float, speed: int, display_scroll: Display_scroll):
        self.x = x + display_scroll.x
        self.y = y + display_scroll.y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = direction
        self.speed = speed
        self.display_scroll = display_scroll

    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), self.hitbox)
        return self

    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x -= diff_x
        self.hitbox.y -= diff_y
        return self

enemies: List[Enemy] = []

RELOAD_DELAY_TYPE2 = 1000
last_enemy_spawn = pygame.time.get_ticks()


class Projectile():
    def __init__(self, x: int, y: int, direction: float, speed: float, color: Color):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.color = color
        self.hitbox = pygame.rect.Rect((self.x, self.y, 15, 15))
    
    def draw(self, display):
        pygame.draw.rect(display, (self.color.r, self.color.g, self.color.b), self.hitbox)
        return self
    
    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x += diff_x
        self.hitbox.y += diff_y
        return self

projectiles: List[Projectile] = []  

RELOAD_DELAY_TYPE1 = 600
last_shot = pygame.time.get_ticks()


#Time
FPS = 90

clock = pygame.time.Clock()


def draw_start_screen():
    display.fill(inside_color)
    font_title = pygame.font.SysFont(None, 130)
    font_start_button = pygame.font.SysFont(None, 90)
    title = font_title.render('GAMEGAME', True, (255, 255, 255))
    start_button_txt = font_start_button.render('Start', True, start_button_color)
    display.blit(title, (screen_x / 2 - title.get_width() / 2, screen_y / 2 - title.get_height() / 2 - 170))
    display.blit(start_button_txt, (screen_x / 2 - start_button_txt.get_width() / 2, screen_y / 2 - start_button_txt.get_height() / 2 + 50))

def draw_game_over_screen():
    display.fill((0, 0, 0))
    font_game_over = pygame.font.SysFont(None, 130)
    font_restart_quit = pygame.font.SysFont(None, 90)
    title_game_over = font_game_over.render('Game Over', True, (255, 255, 255))
    restart_button_txt = font_restart_quit.render('Restart', True, restart_button_color)
    quit_button_txt = font_restart_quit.render('Quit', True, quit_button_color)
    display.blit(title_game_over, (screen_x / 2 - title_game_over.get_width() / 2, screen_y / 2 - title_game_over.get_height() / 2 - 170))
    display.blit(restart_button_txt, (screen_x / 2 - restart_button_txt.get_width() / 2 - 200, screen_y / 2 - restart_button_txt.get_height() / 2 + 50))
    display.blit(quit_button_txt, (screen_x / 2 - quit_button_txt.get_width() / 2 + 200, screen_y / 2 - quit_button_txt.get_height() / 2 + 50))


game_status = 'start_screen'

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    if game_status == 'start_screen':
        draw_start_screen()
        pygame.draw.rect(display, start_button_color, start_button_rect, 6)
        pygame.draw.rect(display, surrounding_color, outline_rect, 20)

        mouse_coordinate_start_screen = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_coordinate_start_screen):
            start_button_color = (180, 180, 180)
        else:
            start_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 515 <= mouse_coordinate_start_screen[0] <= 515 + 170 and 455 <= mouse_coordinate_start_screen[1] <= 455 + 85:
                game_status = 'game'

        pygame.display.update()
    

    if game_status == 'game_over':
        draw_game_over_screen()
        pygame.draw.rect(display, restart_button_color, restart_button_rect, 6)
        pygame.draw.rect(display, quit_button_color, quit_button_rect, 6)

        player.current_hp = player.max_hp
        enemies.clear()

        mouse_coordinate_game_over = pygame.mouse.get_pos()
        if restart_button_rect.collidepoint(mouse_coordinate_game_over):
            restart_button_color = (150, 150, 150)
        else:
            restart_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 280 <= mouse_coordinate_game_over[0] <= 280 + 243 and 454 <= mouse_coordinate_game_over[1] <= 454 + 90:
                game_status = 'start_screen'

        if quit_button_rect.collidepoint(mouse_coordinate_game_over):
            quit_button_color = (150, 150, 150)
        else:
            quit_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 720 <= mouse_coordinate_game_over[0] <= 720 + 165 and 454 <= mouse_coordinate_game_over[1] <= 454 + 90:
                game_over = True

        pygame.display.update()


    if game_status == 'game':
            
        #General movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            display_scroll.x -=3

        if keys[pygame.K_a]:
            display_scroll.x += 3

        if keys[pygame.K_s]:
            display_scroll.y -= 3

        if keys[pygame.K_w]:
            display_scroll.y += 3
        

        now = pygame.time.get_ticks()

        #Enemy movement
        if now - last_enemy_spawn > RELOAD_DELAY_TYPE2:        
            enemy = Enemy(random.randint(-100, 1200), random.randint(-100, 900), 30, 30, enemy_color, 0.0, 2, display_scroll)
            (enemy_dx, enemy_dy) = (enemy.x, enemy.y) - pygame.Vector2(player.rect.center)
            enemy_angle = math.atan2(enemy_dy, enemy_dx)
            enemy.direction = enemy_angle
            enemies.append(enemy)
            last_enemy_spawn = now


        inside_rect = pygame.Rect(inside_x + display_scroll.x, inside_y + display_scroll.y, 1400, 1100)

        for enemy in enemies:
            if player.rect.colliderect(enemy.hitbox):
                player.take_damage(1)
                player.draw_health_bar(display)
            
        if now - last_healing > RELOAD_DELAY_TYPE3:
            player.get_healing(0.1)

        if player.current_hp < 300:
            health_color_green = (204, 22, 2)

        #if player_rect.colliderect(enemy_rect):
        #    player_health_width -= 0.35
        #if player_health_width < 35:
        #   health_color_green = (182, 191, 0)
        #if player_health_width < 20:
            #health_color_green = (204, 22, 2)



        #Projectile movement
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                now = pygame.time.get_ticks()
                if (now > last_shot + RELOAD_DELAY_TYPE1):
                    (dx, dy) = pygame.mouse.get_pos() - pygame.Vector2(player.rect.center)
                    angle = math.atan2(dy, dx)
                    projectile = Projectile(player.rect.x, player.rect.y, angle, 3, projectile_color)
                    projectiles.append(projectile)
                    last_shot = now
                    print(player.draw(display))


        if player.current_hp < 0.5:
            game_status = 'game_over'


        #Draws
        display.fill((30, 20, 0))
        pygame.draw.rect(display, inside_color, inside_rect)
        pygame.draw.rect(display, surrounding_color, (surrounding1_x + display_scroll.x, surrounding1_y + display_scroll.y, 60, 60))
        pygame.draw.rect(display, surrounding_color, (surrounding2_x + display_scroll.x, surrounding2_y + display_scroll.y, 70, 70))
        pygame.draw.rect(display, surrounding_color, (surrounding3_x + display_scroll.x, surrounding3_y + display_scroll.y, 30, 30))
        pygame.draw.rect(display, surrounding_color, (surrounding4_x + display_scroll.x, surrounding4_y + display_scroll.y, 40, 40))   
        pygame.draw.rect(display, surrounding_color, (surrounding5_x + display_scroll.x, surrounding5_y + display_scroll.y, 50, 50))
        pygame.draw.rect(display, surrounding_color, (surrounding6_x + display_scroll.x, surrounding6_y + display_scroll.y, 70, 70))
        for enemy in enemies:
            enemy.update().draw(display)
        player.draw(display)
        pygame.draw.rect(display, wall_color, (-100 + display_scroll.x, -100 + display_scroll.y, 1400, 1100), 10)
        pygame.draw.rect(display, (255, 0, 0), (20, 20, 400, 35))
        player.draw_health_bar(display)
        for p in projectiles:
            p.update().draw(display)

        pygame.display.update()

        clock.tick(FPS)

pygame.quit()