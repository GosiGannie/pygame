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
projectile_color = Color(40, 40, 60)
start_button_color = (255, 255, 255)
tutorial_button_color = (255, 255, 255)
return_button_color = (255, 255, 255)
restart_button_color = (255, 255, 255)
quit_button_color = (255, 255, 255)
title_color = (255, 255, 255)
upgrade_screen_background_color = (40, 77, 33)
new_wave_button_color = (255, 255, 255)
strength_buy_color = (255, 255, 255)
defence_buy_color = (255, 255, 255)
max_hp_buy_color = (255, 255, 255)
health_regen_buy_color = (255, 255, 255)
enemy_health_bar_color = Color(148, 38, 100)


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


#Start stats
strength_stat = 10
defence_stat = 10
max_hp_stat = 100
health_regen_stat = 1

enemy_damage = 10

#Start costs
strength_cost = 5
defence_cost = 5
max_hp_cost = 5
health_regen_cost = 10

coins = 0


#Start screen rects
start_button_rect = pygame.Rect(515, 455, 170, 85)
outline_rect = pygame.Rect(30, 30, screen_x - 60, screen_y - 60)
tutorial_rect = pygame.Rect(470, 635, 260, 85)

#Tutorial rects
left_click_rect = pygame.Rect(245, 391, 178, 49)
w_rect = pygame.Rect(731, 391, 51, 49)
a_rect = pygame.Rect(795, 391, 51, 49)
s_rect = pygame.Rect(857, 391, 47, 49)
d_rect = pygame.Rect(915, 391, 49, 49)
return_rect = pygame.Rect(510, 570, 179, 60)

#Game over rects
restart_button_rect = pygame.Rect(280, 454, 243, 90)
quit_button_rect = pygame.Rect(720, 454, 165, 90)

#Upgrade rects
new_wave_button_rect = pygame.Rect(880, 70, 263, 65)
strength_buy_rect = pygame.Rect(250, 381, 99, 53)
defence_buy_rect = pygame.Rect(850, 381, 99, 53)
max_hp_buy_rect = pygame.Rect(250, 631, 99, 53)
health_regen_buy_rect = pygame.Rect(850, 631, 99, 53)


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
        self.health_bar_length = health_bar_length
        self.health_ratio = self.max_hp / self.health_bar_length
        self.health_bar_color = health_bar_color
        self.display_scroll = display_scroll
    
    def draw(self, display):
        #pygame.draw.rect(display, (self.player_color.r, self.player_color.g, self.player_color.b), self.rect)
        player_img = pygame.image.load('Sprites/Hero/idle_down (1).png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (135, 125))
        display.blit(player_img, (self.rect.centerx - 67, self.rect.centery - 64, self.width, self.height))

        
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
        pygame.draw.rect(display, (255, 255, 255), (20, 20, self.health_bar_length, 35), 4)

player = Player(575, 425, 45, 45, color_player, max_hp_stat, 100, 400, health_color_green, display_scroll)


class Enemy():
    def __init__(self, x: int, y: int, width: int, height: int, color: Color, direction: float, speed: int, display_scroll: Display_scroll, max_hp: int, current_hp: int, health_bar_length: int, health_bar_color: Color):
        self.x = x + display_scroll.x
        self.y = y + display_scroll.y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = direction
        self.speed = speed
        self.display_scroll = display_scroll
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.health_bar_length = health_bar_length
        self.health_ratio = self.max_hp / self.health_bar_length
        self.health_bar_color = health_bar_color

    def draw(self, display):
        enemy_img_path = pygame.image.load('Sprites/Monster/idle_down (1).png')
        enemy_img = pygame.transform.scale(enemy_img_path, (90, 90))
        display.blit(enemy_img, (self.hitbox.x - 30, self.hitbox.y - 30, self.width, self.height))
        return self

    def update(self):
        diff_x = math.cos(self.direction) * self.speed
        diff_y = math.sin(self.direction) * self.speed
        self.hitbox.x -= diff_x
        self.hitbox.y -= diff_y
        return self
    
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
        pygame.draw.rect(display, (self.health_bar_color.r, self.health_bar_color.g, self.health_bar_color.b), (self.x - 5, self.y - self.height - 5, self.current_hp / self.health_ratio, 10))
        pygame.draw.rect(display, (255, 255, 255), (self.x - 5, self.y - self.height - 5, self.health_bar_length, 10), 1)

enemies: List[Enemy] = []


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


#Time
FPS = 90

RELOAD_DELAY_TYPE1 = 600
RELOAD_DELAY_TYPE2 = 2000
RELOAD_DELAY_TYPE3 = 500
RELOAD_DELAY_TYPE4 = 400

last_damage_take = pygame.time.get_ticks()
last_shot = pygame.time.get_ticks()
last_enemy_spawn = pygame.time.get_ticks()
wave_start = pygame.time.get_ticks()
last_healing = pygame.time.get_ticks()
completed_wave_timer = pygame.time.get_ticks()

clock = pygame.time.Clock()


#Text and screens
def draw_start_screen():
    display.fill(inside_color)
    font_title = pygame.font.SysFont(None, 130)
    font_start_button = pygame.font.SysFont(None, 90)
    font_tutorial_button = pygame.font.SysFont(None, 90)

    title = font_title.render('GAMEGAME', True, (255, 255, 255))
    start_button_txt = font_start_button.render('Start', True, start_button_color)
    tutorial_button_txt = font_tutorial_button.render('Tutorial', True, tutorial_button_color)

    display.blit(title, (screen_x / 2 - title.get_width() / 2, screen_y / 2 - title.get_height() / 2 - 170))
    display.blit(start_button_txt, (screen_x / 2 - start_button_txt.get_width() / 2, screen_y / 2 - start_button_txt.get_height() / 2 + 50))
    display.blit(tutorial_button_txt, (screen_x / 2 - tutorial_button_txt.get_width() / 2, 650))

def tutorial_screen():
    display.fill(inside_color)
    font_tutorial = pygame.font.SysFont(None, 130)
    font_attack = pygame.font.SysFont(None, 90)
    font_left_click = pygame.font.SysFont(None, 50)
    font_move = pygame.font.SysFont(None, 90)
    font_wasd = pygame.font.SysFont(None, 50)
    font_return = pygame.font.SysFont(None, 70)

    tutorial_txt = font_tutorial.render('Tutorial', True, (255, 255, 255))
    attack_txt = font_attack.render('Attack', True, (255, 255, 255))
    left_click_txt = font_left_click.render('Left Click', True, (255, 255, 255))
    move_txt = font_move.render('Move', True, (255, 255, 255))
    wasd_txt = font_wasd.render('W    A    S    D', True, (255, 255, 255))
    return_txt = font_return.render('Return', True, return_button_color)

    display.blit(tutorial_txt, (screen_x / 2 - tutorial_txt.get_width() / 2, 100))
    display.blit(attack_txt, (240, 300))
    display.blit(left_click_txt, (255, 400))
    display.blit(move_txt, (760, 300))
    display.blit(wasd_txt, (740, 400))
    display.blit(return_txt, (screen_x / 2 - return_txt.get_width() / 2, 579))

def draw_game_over_screen():
    display.fill((0, 0, 0))
    font_game_over = pygame.font.SysFont(None, 130)
    font_restart_quit = pygame.font.SysFont(None, 90)
    font_wave_completion = pygame.font.SysFont(None, 100)

    title_game_over = font_game_over.render('Game Over', True, (255, 255, 255))
    restart_button_txt = font_restart_quit.render('Restart', True, restart_button_color)
    quit_button_txt = font_restart_quit.render('Quit', True, quit_button_color)
    wave_completion_txt = font_wave_completion.render('Waves Completed: {}'.format(new_wave_clicks), True, (255, 255, 255))

    display.blit(title_game_over, (screen_x / 2 - title_game_over.get_width() / 2, screen_y / 2 - title_game_over.get_height() / 2 - 240))
    display.blit(restart_button_txt, (screen_x / 2 - restart_button_txt.get_width() / 2 - 200, screen_y / 2 - restart_button_txt.get_height() / 2 + 50))
    display.blit(quit_button_txt, (screen_x / 2 - quit_button_txt.get_width() / 2 + 200, screen_y / 2 - quit_button_txt.get_height() / 2 + 50))
    display.blit(wave_completion_txt, (screen_x / 2- wave_completion_txt.get_width() / 2, 300))

def upgrade_screen():
    display.fill(upgrade_screen_background_color)
    font_title_upgrades = pygame.font.SysFont(None, 130)
    font_coins = pygame.font.SysFont(None, 60)
    font_upgrade_button = pygame.font.SysFont(None, 70)
    font_stats = pygame.font.SysFont(None, 45)
    font_new_wave_button = pygame.font.SysFont(None, 70)
    font_cost = pygame.font.SysFont(None, 50)
    font_buy = pygame.font.SysFont(None, 55)

    title_upgrades = font_title_upgrades.render('Upgrades', True, (255, 255, 255))
    coins_display = font_coins.render('Coins: {}'.format(coins), True, (255,215,0))
    strength_upgrade_button = font_upgrade_button.render('Strength', True, (255, 255, 255))
    defence_upgrade_button = font_upgrade_button.render('Defence', True, (255, 255, 255))
    health_upgrade_button = font_upgrade_button.render('Health', True, (255, 255, 255))
    health_regen_upgrade_button = font_upgrade_button.render('Health Regen', True, (255, 255, 255))
    stats_strength_display = font_stats.render('Strength:           {}'.format(strength_stat), True, (255, 255, 255))
    stats_defence_display = font_stats.render('Defence:            {}'.format(defence_stat), True, (255, 255, 255))
    stats_max_hp_display = font_stats.render('Health:               {}'.format(max_hp_stat), True, (255, 255, 255))
    stats_health_regen_display = font_stats.render('Health Regen:   {}'.format(health_regen_stat), True, (255, 255, 255))
    new_wave_button = font_new_wave_button.render('New Wave', True, new_wave_button_color)
    cost_strength_display = font_cost.render('Cost: {}'.format(strength_cost), True, (255, 255, 255))
    cost_defence_display = font_cost.render('Cost: {}'.format(defence_cost), True, (255, 255, 255))
    cost_mx_hp_display = font_cost.render('Cost: {}'.format(max_hp_cost), True, (255, 255, 255))
    cost_health_regen_display = font_cost.render('Cost: {}'.format(health_regen_cost), True, (255, 255, 255))
    strength_buy = font_buy.render('BUY', True, strength_buy_color)
    defence_buy = font_buy.render('BUY', True, defence_buy_color)
    max_hp_buy = font_buy.render('BUY', True, max_hp_buy_color)
    health_regen_buy = font_buy.render('BUY', True, health_regen_buy_color)

    display.blit(title_upgrades, (screen_x / 2 - title_upgrades.get_width() / 2, screen_y / 2 - title_upgrades.get_height() / 2 - 350))
    display.blit(coins_display, (screen_x / 2 - coins_display.get_width() / 2, screen_y / 2 - coins_display.get_height() / 2 - 270))
    display.blit(strength_upgrade_button, (screen_x / 4 - strength_upgrade_button.get_width() / 2, screen_y / 2 - strength_upgrade_button.get_height() / 2 - 170))
    display.blit(defence_upgrade_button, ((screen_x / 4) * 3 - defence_upgrade_button.get_width() / 2, screen_y / 2 - defence_upgrade_button.get_height() / 2 - 170))
    display.blit(health_upgrade_button, (screen_x / 4 - health_upgrade_button.get_width() / 2, screen_y / 2 - health_upgrade_button.get_height() / 2 + 80))
    display.blit(health_regen_upgrade_button, ((screen_x / 4) * 3 - health_regen_upgrade_button.get_width() / 2, screen_y / 2 - health_regen_upgrade_button.get_height() / 2 + 80))
    display.blit(stats_strength_display, (30, 30, stats_strength_display.get_width() / 2, stats_strength_display.get_height() / 2))
    display.blit(stats_defence_display, (30, 70, stats_defence_display.get_width() / 2, stats_defence_display.get_height() / 2))
    display.blit(stats_max_hp_display, (30, 110, stats_max_hp_display.get_width() / 2, stats_max_hp_display.get_height() / 2))
    display.blit(stats_health_regen_display, (30, 150, stats_health_regen_display.get_width() / 2, stats_health_regen_display.get_height() / 2))
    display.blit(new_wave_button, (screen_x - new_wave_button.get_width() - 70, 80))
    display.blit(cost_strength_display, (screen_x / 4 - cost_strength_display.get_width() / 2, screen_y / 2 - cost_strength_display.get_height() / 2 - 110))
    display.blit(cost_defence_display, ((screen_x / 4) * 3 - cost_defence_display.get_width() / 2, screen_y / 2 - cost_defence_display.get_height() / 2 - 110))
    display.blit(cost_mx_hp_display, (screen_x / 4 - cost_mx_hp_display.get_width() / 2, screen_y / 2 - cost_mx_hp_display.get_height() / 2 + 140))
    display.blit(cost_health_regen_display, ((screen_x / 4) * 3 - cost_health_regen_display.get_width() / 2, screen_y / 2 - cost_health_regen_display.get_height() / 2 + 140))
    display.blit(strength_buy, (screen_x / 4 - strength_buy.get_width() / 2, screen_y / 2 - strength_buy.get_height() / 2 - 40))
    display.blit(defence_buy, ((screen_x / 4) * 3 - defence_buy.get_width() / 2, screen_y / 2 - defence_buy.get_height() / 2 - 40))
    display.blit(max_hp_buy, (screen_x / 4 - max_hp_buy.get_width() / 2, screen_y / 2 - max_hp_buy.get_height() / 2 + 210))
    display.blit(health_regen_buy, ((screen_x / 4) * 3 - health_regen_buy.get_width() / 2, screen_y / 2 - health_regen_buy.get_height() / 2 + 210))

def game_screen():
    font_coin_counter = pygame.font.SysFont(None, 60)
    font_game_timer = pygame.font.SysFont(None, 60)
    font_max_hp = pygame.font.SysFont(None, 50)
    font_wave_counter = pygame.font.SysFont(None, 60)

    coin_count = font_coin_counter.render('Coins: {}'.format(coins), True, (255,215,0))
    game_timer = font_game_timer.render('Wave Time: {}'.format(last_wave_start / 1000), True, (255, 255, 255))
    max_hp_txt = font_max_hp.render('HP: {} / {}'.format(player.current_hp, player.max_hp), True, (255, 255, 255))
    wave_counter_txt = font_wave_counter.render('Wave: {}'.format(new_wave_clicks + 1), True, (255, 255, 255))

    display.blit(coin_count, (screen_x - 250, 20))
    display.blit(game_timer, (screen_x / 2 - 150, 20))
    display.blit(max_hp_txt, (25, 60))
    display.blit(wave_counter_txt, (25, 100))
    pygame.display.update()



game_status = 'start_screen'

new_wave_clicks = 0

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    #Start screen
    if game_status == 'start_screen':
        draw_start_screen()
        pygame.draw.rect(display, start_button_color, start_button_rect, 6)
        pygame.draw.rect(display, surrounding_color, outline_rect, 20)
        pygame.draw.rect(display, tutorial_button_color, tutorial_rect, 6)


        #Start button
        mouse_coordinate_start_screen = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse_coordinate_start_screen):
            start_button_color = (180, 180, 180)
        else:
            start_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 515 <= mouse_coordinate_start_screen[0] <= 515 + 170 and 455 <= mouse_coordinate_start_screen[1] <= 455 + 85:
                game_status = 'game'

        #Tutorial button
        if tutorial_rect.collidepoint(mouse_coordinate_start_screen):
            tutorial_button_color = (180, 180, 180)
        else:
            tutorial_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 470 <= mouse_coordinate_start_screen[0] <= 470 + 260 and 635 <= mouse_coordinate_start_screen[1] <= 635 + 85:
                game_status = 'tutorial'


        pygame.display.update()


    if game_status == 'tutorial':
        tutorial_screen()
        pygame.draw.rect(display, surrounding_color, outline_rect, 20)
        pygame.draw.rect(display, (255, 255, 255), left_click_rect, 4)
        pygame.draw.rect(display, (255, 255, 255), w_rect, 4)
        pygame.draw.rect(display, (255, 255, 255), a_rect, 4)
        pygame.draw.rect(display, (255, 255, 255), s_rect, 4)
        pygame.draw.rect(display, (255, 255, 255), d_rect, 4)
        pygame.draw.rect(display, return_button_color, return_rect, 4)


        #Return button
        mouse_coordinate_tutorial = pygame.mouse.get_pos()
        if return_rect.collidepoint(mouse_coordinate_tutorial):
            return_button_color = (180, 180, 180)
        else:
            return_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 510 <= mouse_coordinate_tutorial[0] <= 510 + 179 and 570 <= mouse_coordinate_tutorial[1] <= 570 + 60:
                game_status = 'start_screen'


        pygame.display.update()

    
    #Game over screen
    if game_status == 'game_over':
        draw_game_over_screen()
        pygame.draw.rect(display, restart_button_color, restart_button_rect, 6)
        pygame.draw.rect(display, quit_button_color, quit_button_rect, 6)

        player.current_hp = player.max_hp
        enemies.clear()

        mouse_coordinate_game_over = pygame.mouse.get_pos()

        #Restart button
        if restart_button_rect.collidepoint(mouse_coordinate_game_over):
            restart_button_color = (150, 150, 150)
        else:
            restart_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 280 <= mouse_coordinate_game_over[0] <= 280 + 243 and 454 <= mouse_coordinate_game_over[1] <= 454 + 90:
                game_status = 'start_screen'

        #Quit button
        if quit_button_rect.collidepoint(mouse_coordinate_game_over):
            quit_button_color = (150, 150, 150)
        else:
            quit_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 720 <= mouse_coordinate_game_over[0] <= 720 + 165 and 454 <= mouse_coordinate_game_over[1] <= 454 + 90:
                game_over = True

        pygame.display.update()

    #Upgrades screen
    if game_status == 'upgrades':
        upgrade_screen()
        pygame.draw.rect(display, new_wave_button_color, new_wave_button_rect, 5)
        pygame.draw.rect(display, strength_buy_color, strength_buy_rect, 5)
        pygame.draw.rect(display, defence_buy_color, defence_buy_rect, 5)
        pygame.draw.rect(display, max_hp_buy_color, max_hp_buy_rect, 5)
        pygame.draw.rect(display, health_regen_buy_color, health_regen_buy_rect, 5)
        coquette_img_path = pygame.image.load('Sprites/coquette_copy.png').convert_alpha()
        coquette_img = pygame.transform.scale(coquette_img_path, (100, 100))
        display.blit(coquette_img, (630, 34, 50, 50))


        mouse_coordinate_upgrades = pygame.mouse.get_pos()

        #New wave button
        if new_wave_button_rect.collidepoint(mouse_coordinate_upgrades):
            new_wave_button_color = (180, 180, 180)
        else:
            new_wave_button_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONUP:
            if 880 <= mouse_coordinate_upgrades[0] <= 880 + 263 and 70 <= mouse_coordinate_upgrades[1] <= 70 + 65:
                game_status = 'game'
                wave_start = now
                last_wave_start = now
                new_wave_clicks += 1
                for enemy in enemies:
                    enemies.clear()
                player.max_hp = max_hp_stat
                player.current_hp = player.max_hp
                player.health_bar_length = 400
                

        #Buy buttons
        if strength_buy_rect.collidepoint(mouse_coordinate_upgrades):
            strength_buy_color = (180, 180, 180)
        elif defence_buy_rect.collidepoint(mouse_coordinate_upgrades):
            defence_buy_color = (180, 180, 180)
        elif max_hp_buy_rect.collidepoint(mouse_coordinate_upgrades):
            max_hp_buy_color = (180, 180, 180)
        elif health_regen_buy_rect.collidepoint(mouse_coordinate_upgrades):
            health_regen_buy_color = (180, 180, 180)
        else:
            strength_buy_color = (255, 255, 255)
            defence_buy_color = (255, 255, 255)
            max_hp_buy_color = (255, 255, 255)
            health_regen_buy_color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if coins >= strength_cost:
                if strength_buy_rect.x <= mouse_coordinate_upgrades[0] <= strength_buy_rect.x + strength_buy_rect.width and strength_buy_rect.y <= mouse_coordinate_upgrades[1] <= strength_buy_rect.y + strength_buy_rect.width:
                    strength_stat += 1
                    coins -= strength_cost
                    strength_cost += strength_cost - new_wave_clicks * 4
            if coins >= defence_cost:
                if defence_buy_rect.x <= mouse_coordinate_upgrades[0] <= defence_buy_rect.x + defence_buy_rect.width and defence_buy_rect.y <= mouse_coordinate_upgrades[1] <= defence_buy_rect.y + defence_buy_rect.width:
                    defence_stat += 1
                    coins -= defence_cost
                    defence_cost += defence_cost / 2
            if coins >= max_hp_cost:
                if max_hp_buy_rect.x <= mouse_coordinate_upgrades[0] <= max_hp_buy_rect.x + max_hp_buy_rect.width and max_hp_buy_rect.y <= mouse_coordinate_upgrades[1] <= max_hp_buy_rect.y + max_hp_buy_rect.width:
                    max_hp_stat += 20
                    coins -= max_hp_cost
                    max_hp_cost += max_hp_cost / 2
            if coins >= health_regen_cost:
                if health_regen_buy_rect.x <= mouse_coordinate_upgrades[0] <= health_regen_buy_rect.x + health_regen_buy_rect.width and health_regen_buy_rect.y <= mouse_coordinate_upgrades[1] <= health_regen_buy_rect.y + health_regen_buy_rect.width:
                    health_regen_stat += 1
                    coins -= health_regen_cost
                    health_regen_cost += health_regen_cost / 2

        pygame.display.update()


    if game_status == 'game':

        now = pygame.time.get_ticks()
        last_wave_start = now - 20000 * new_wave_clicks
        

        #General movement
        keys = pygame.key.get_pressed()
        speed_factor = 3
        
        if keys[pygame.K_d] and player.rect.x < 1245 + display_scroll.x:
            display_scroll.x -= speed_factor

        if keys[pygame.K_a] and player.rect.x > -93 + display_scroll.x:
            display_scroll.x += speed_factor

        if keys[pygame.K_s] and player.rect.y < 945 + display_scroll.y:
            display_scroll.y -= speed_factor

        if keys[pygame.K_w] and player.rect.y > -93 + display_scroll.y:
            display_scroll.y += speed_factor
        


        #Enemy movement
        if now - last_enemy_spawn > RELOAD_DELAY_TYPE2:        
            enemy = Enemy(random.randint(-100, 1200), random.randint(-100, 900), 30, 30, enemy_color, 0.0, 2, display_scroll, 20 + 2 * new_wave_clicks, 20 + 2 * new_wave_clicks, 40, enemy_health_bar_color)
            (enemy_dx, enemy_dy) = (enemy.x, enemy.y) - pygame.Vector2(player.rect.center)
            enemy_angle = math.atan2(enemy_dy, enemy_dx)
            enemy.direction = enemy_angle
            enemies.append(enemy)
            last_enemy_spawn = now


        inside_rect = pygame.Rect(inside_x + display_scroll.x, inside_y + display_scroll.y, 1400, 1100)

        #Enemy damage
        for enemy in enemies:
            if player.rect.colliderect(enemy.hitbox):
                if now > last_damage_take + RELOAD_DELAY_TYPE4:     
                    player.take_damage(enemy_damage + (new_wave_clicks * 5) - defence_stat / 4)
                    player.draw_health_bar(display)
                    last_damage_take = now

        #Healing
        if now > last_healing + RELOAD_DELAY_TYPE3:
            player.get_healing(health_regen_stat)
            last_healing = now
            

        #Projectile movement
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                now = pygame.time.get_ticks()
                if (now > last_shot + RELOAD_DELAY_TYPE1):
                    (dx, dy) = pygame.mouse.get_pos() - pygame.Vector2((player.rect.center))
                    angle = math.atan2(dy, dx)
                    projectile = Projectile(player.rect.centerx, player.rect.centery, angle, 8, projectile_color)
                    projectiles.append(projectile)
                    last_shot = now


        #Enemy projectile collision
        for enemy in enemies:
            if enemy.hitbox.colliderect(projectile.hitbox):
                enemy.current_hp -= strength_stat
                projectiles.remove(projectile)

            if enemy.current_hp == 0:
                enemies.remove(enemy)
                coins += 5

        
        if now - wave_start > 20000:
            game_status = 'wave_completed'
            
                
        if player.current_hp == 0:
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
            enemy.update().draw(display).draw_health_bar(display)

        for projectile in projectiles:
            projectile.update().draw(display)
        player.draw(display)
        pygame.draw.rect(display, wall_color, (-100 + display_scroll.x, -100 + display_scroll.y, 1400, 1100), 10)
        pygame.draw.rect(display, (255, 0, 0), (20, 20, 400, 35))
        player.draw_health_bar(display)
        pygame.draw.rect(display, (0, 0, 0), (screen_x / 2, screen_y / 2, 2, 2))
        game_screen()

        pygame.display.update()

        clock.tick(FPS)

pygame.quit()