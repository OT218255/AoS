import pygame, random
from pygame.locals import *


def get_events(events_list, player, player_location, array):
    """
    Check each possible event in the game in order to be resolved in the game loop.

    :param events_list:         List of each possible event in game.
    :return:                    Returns event list to be passed to game loop.
    """
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            bools = player.collision_detection(player_location, array)
            if event.key == K_w and bools[0]:
                events_list[0] = True
                player_location[1] -= 1
            elif event.key == K_a and bools[3]:
                events_list[1] = True
                player_location[0] -= 1
            elif event.key == K_s and bools[2]:
                events_list[2] = True
                player_location[1] += 1
            elif event.key == K_d and bools[1]:
                events_list[3] = True
                player_location[0] += 1
        elif event.type == QUIT:
            events_list[4] = True
    return events_list, player_location
    # 0 = w 1 = a 2 = s 3 = d 4 = Quit
