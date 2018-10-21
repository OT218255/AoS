import pygame
from pygame.locals import *

FPS = 30
def display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list):
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)