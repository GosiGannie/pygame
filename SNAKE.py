import pygame
import random

pygame.init()
pygame.font.init()

screen_x = 700
screen_y = 700

display = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption('Hello')

font = pygame.font.Font(None, 36)

counter_text = font.render('Points: 0', True, (255, 255, 255))

color1 = (75, 98, 71)
color2 = (230, 135, 135)

player_x = 300
player_y = 300

circle_x2 = 300
circle_y2 = 200

circle_radius = 23
circle_radius2 = 12

pos = []
pos2 = (circle_x2, circle_y2)

player_xx = player_x
player_yy = player_y
circle_speed_x1 = 0
circle_speed_y1 = 0

points = 0

clock = pygame.time.Clock()

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        circle_speed_x1 = 3
        circle_speed_y1 = 0
    elif keys[pygame.K_LEFT]:
        circle_speed_x1 = -3
        circle_speed_y1 = 0
    elif keys[pygame.K_DOWN]:
        circle_speed_x1 = 0
        circle_speed_y1 = 3
    elif keys[pygame.K_UP]:
        circle_speed_x1 = 0
        circle_speed_y1 = -3

    player_xx += circle_speed_x1
    player_yy += circle_speed_y1

    pos.append([player_xx, player_yy])

    circle_rect = pygame.Rect(player_xx - circle_radius, player_yy - circle_radius, 2 * circle_radius, 2 * circle_radius)
    circle_rect2 = pygame.Rect(circle_x2 - circle_radius2, circle_y2 - circle_radius2, 2 * circle_radius2, 2 * circle_radius2)

    if circle_rect.colliderect(circle_rect2) == True:
        circle_x2 = random.randint(circle_radius2, screen_y - circle_radius2)
        circle_y2 = random.randint(circle_radius2, 700)
        points += 1
        for p in range(7):
            pos.append([player_xx, player_yy])  

    display.fill((153, 217, 137))

    for i in pos:
        pygame.draw.circle(display, color1, i, circle_radius)
    pos.pop(0)

    if player_xx < 0 - circle_radius or player_xx > 700 + circle_radius:
        game_over = True
    if player_yy < 0 - circle_radius or player_yy > 700 + circle_radius:
        game_over = True
    
    pos2 = (circle_x2, circle_y2)

    pygame.draw.circle(display, color2, pos2, circle_radius2)

    counter_text = font.render(f'Points: {points}', True, (28, 31, 27))
    display.blit(counter_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.font.quit()
pygame.quit()