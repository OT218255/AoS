import pygame, random
from pygame.locals import *

def get_events(events_list):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            events_list[0] = True
        elif event.type == MOUSEBUTTONUP:
            events_list[1] = True
        elif event.type == QUIT:
            events_list[2] = True
    return events_list