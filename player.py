import pygame, consts
from pygame.locals import *
from consts import *


class Player(object):
    def move_player(self, direction, x, y):
        if direction == 0: # Up
            y -= TILE_SIZE
        elif direction == 1: # Right
            x += TILE_SIZE
        elif direction == 2: # Down
            y += TILE_SIZE
        elif direction == 3: # Left
            x -= TILE_SIZE
        return (x, y)