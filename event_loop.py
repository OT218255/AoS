import pygame, random
from pygame.locals import *


def get_events(events_list):
    for event in pygame.event.get():
        if event.type == K_w:
            events_list[0] = True
        elif event.type == K_a:
            events_list[1] = True
        elif event.type == K_s:
            events_list[2] = True
        elif event.type == K_d:
            events_list[3] = True
        elif event.type == QUIT:
            events_list[4] = True
    return events_list
    # 0 = w 1 = a 2 = s 3 = d 4 = Quit
