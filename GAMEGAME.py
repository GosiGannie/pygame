import pygame
import random
import math

pygame.init()

screen_x = 1200
screen_y = 900

display = pygame.display.set_mode([screen_x, screen_y])

player_x = 600
player_y = 400

enemy1_x = 300
enemy1_y = 700

surrounding1_x = random.randint(0, 1500)
surrounding1_y = random.randint(0, 1000)

surrounding2_x = random.randint(0, 1500)
surrounding2_y = random.randint(0, 1000)

color_player = (47, 94, 161)
enemy_color = (102, 3, 3)
surrounding_color = (22, 71, 15)

dx, dy = player_x - enemy1_x, player_y - enemy1_y
dist = math.hypot(dx, dy)
dx, dy = dx / dist, dy / dist

#class Enemy(object):
 #   def __init__(self, x, y, speed):
  #      self.rect = pygame.Rect(x, y, 60, 60)
   #     self.speed = speed

#    def move_towards_player(self, player):
 #       dx, dy = player[0] - self.rect.x, player[1] - self.rect.y
  #      dist = math.hypot(dx, dy)
   #     dx, dy = dx / dist, dy / dist
   #     self.rect.x = dx * self.speed
    #    self.rect.y = dy * self.speed

#enemy1 = Enemy(surrounding1_x, surrounding1_y, 3)

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
    if keys[pygame.K_a]:
        surrounding1_x += 3
        surrounding2_x += 3
        enemy1_x += 3
    if keys[pygame.K_s]:
        surrounding1_y -= 3
        surrounding2_y -= 3
        enemy1_y -= 3
    if keys[pygame.K_w]:
        surrounding1_y += 3
        surrounding2_y += 3
        enemy1_y += 3   

    display.fill((70, 107, 50))

    #enemy1.move_towards_player((player_x, player_y))

    pygame.draw.rect(display, surrounding_color, (surrounding1_x, surrounding1_y, 60, 60))
    pygame.draw.rect(display, surrounding_color, (surrounding2_x, surrounding2_y, 70, 50))
    pygame.draw.rect(display, enemy_color, (enemy1_x, enemy1_y, 30, 30))
    pygame.draw.rect(display, color_player, (player_x, player_y, 40, 40))
   
    pygame.display.update()

    clock.tick(100)

pygame.quit()