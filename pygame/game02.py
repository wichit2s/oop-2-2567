import pygame
from pygame import Color

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game02')
clock = pygame.time.Clock()
running = True
frame = 0
while running:
    # 1. check events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    # 2. update game object
    # 3. draw on screen
    color = Color(255,0,255)
    screen.fill(color)
    clock.tick(30)
    # 4. flip to show in use window
    pygame.display.flip()
    #frame += 1
    #print(frame)
