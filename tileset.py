import json

import pygame


def load_tileset(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data
class Tile(object):
    def __init__(self, **data):
        self.__dict__.update(data)
class Layer(object):
    def __init__(self, **data):
        self.tiles = []
        for tile in data['tiles']:
            t = Tile(**tile)
            self.tiles.append(t)
        data.pop('tiles')
        self.__dict__.update(data)

import base64, io
from PIL import Image
def strToImage(v):
    b = base64.b64decode(v[22:])
    bb = io.BytesIO(b)
    img = Image.open(bb)
    # img = Image.open(io.BytesIO(base64.b64decode(v[22:])))
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

class Tileset(object):
    def __init__(self, fname='Tiny_Swords.json'):
        data = load_tileset(fname)
        self.layers = [] # list of Tile
        for layer in data['layers']:
            _layer = Layer(**layer)
            self.layers.append(_layer)
        self.spriteSheets = {} # data['spriteSheets']
        #for sprite in data['spriteSheets']:
        #    value = data['spriteSheets']['sprite']
        for k, v in data['spriteSheets'].items():
            self.spriteSheets[k] = strToImage(v)
        self.names = list(self.spriteSheets.keys())
        self.name_index = 0
        data.pop('layers')
        data.pop('spriteSheets')
        self.__dict__.update(data)
    def show_spritesheet_name(self, font, screen):
        name = self.names[self.name_index]
        text = font.render(name, True, 20)
        screen.blit(text, (20, 550))
    def show_fps(self, font, screen, clock):
        message = f'{clock.get_fps():.2f} FPS'
        text = font.render(message, True, 40)
        screen.blit(text, (800-text.get_width(), 550))
    def draw(self, screen):
        name = self.names[self.name_index]
        screen.blit(self.spriteSheets[name], (10, 20) )
    def up(self):
        self.name_index = (self.name_index+1)%len(self.names)
    def down(self):
        self.name_index = (self.name_index-1)%len(self.names)


from pygame.locals import *
from pygame.font import Font
pygame.init()
screen = pygame.display.set_mode((800, 600))
logo = pygame.image.load('Game05.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Super Mario Game05')
font = Font('Monoton.ttf', 20)
tileset = Tileset()
clock = pygame.time.Clock()
running = True
while running:
    # 1. check events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        elif e.type == pygame.KEYDOWN:
            if e.key in [K_LEFT, K_DOWN]:
                tileset.down()
            elif e.key in [K_RIGHT, K_UP]:
                tileset.up()
    # 2. update game objects
    # 3. draw onto screen
    screen.fill((160, 160, 160))
    tileset.show_spritesheet_name(font, screen)
    tileset.show_fps(font, screen, clock)
    tileset.draw(screen)
    # 4. flip screen to display
    clock.tick(60)
    pygame.display.flip()

