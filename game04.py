import pygame
from pygame import Color
from pygame.locals import *

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game02')
clock = pygame.time.Clock()
sheet = pygame.image.load('spritesheet.png')
running = True
frame = 0
x, y = 20, 40
speed = 10
while running:
    # 1. check events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        #if e.type == KEYDOWN:
        #    #if e.key == K_a or e.key == K_LEFT: # left
        #    if e.key in [K_a, K_LEFT]:    x -= speed
        #    elif e.key in [K_d, K_RIGHT]: x += speed
        #    elif e.key in [K_s, K_DOWN]:  y += speed
        #    elif e.key in [K_w, K_UP]:    y -= speed
    # จิี้มค้างงง
    keys = pygame.key.get_pressed()
    if keys[K_a] or keys[K_LEFT]:    x -= speed
    elif keys[K_d] or keys[K_RIGHT]: x += speed
    elif keys[K_s] or keys[K_DOWN]:  y += speed
    elif keys[K_w] or keys[K_UP]:    y -= speed
    # 2. update game object
    # 3. draw on screen
    # www.spritefusion.com
    screen.fill((0,0,0))
    screen.blit(sheet, (x, y))
    clock.tick(30)
    # 4. flip to show in use window
    pygame.display.flip()
    #frame += 1
    #print(frame)
