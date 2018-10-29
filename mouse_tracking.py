import pygame, sys
from pygame import *


def get_pixel_at_click():
    mouse_click_position = mouse.get_pos()
    print(mouse_click_position)
    return mouse_click_position


def get_pixel_at_lift():
    mouse_release_position = mouse.get_pos()
    return mouse_release_position


def get_player_facing_direction(mouse_click_position, mouse_release_position):
    if abs(mouse_release_position[0] - mouse_click_position[0]) >\
            abs(mouse_release_position[1] - mouse_click_position[1]): # if X is > than Y
        if abs(mouse_release_position[0] - mouse_click_position[0]) > 100: # if X movement is greater than 100 px
            if mouse_click_position[0] > mouse_release_position[0]: # checks if X movement is left or right
                direction = 3
            else:
                direction = 1
        else:
            print('Click')
    else:
        if abs(mouse_click_position[1] - mouse_release_position[1]) > 100:
            if mouse_click_position[1] > mouse_release_position[1]:
                direction = 0
            else:
                direction = 2
        else:
            print('Click')
    print(direction)
    return direction