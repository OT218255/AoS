import pygame, sys, mouse_tracking, event_loop
from pygame.locals import *


def all_states_update(event_list, player_sprites, enemy_sprites, environment_sprites):
    if event_list[0]:
        direction = event_resolve(event_list, player_sprites)
        player_current_sprite = move_player(player_sprites, direction)




def event_resolve(events_list, sprites):
    moving = False
    if events_list[0]:
        mouse_click_position = mouse_tracking.get_pixel_at_click()
        while not events_list[1]:
            if events_list[1]:
                mouse_release_position = mouse_tracking.get_pixel_at_lift()
                direction = mouse_tracking.get_player_facing_direction(mouse_click_position, mouse_release_position)
                moving = True # Above is all messy code but it was the only way I could get it to work.
                return direction, moving
    if events_list[2]:
        terminate()


def move_player(playerSprites, direction):
    if direction == 0:
        playerCurrent = playerSprites[direction].get_rect()
        return playerCurrent
    elif direction == 1:
        playerCurrent = playerSprites[direction].get_rect()
        return playerCurrent
    elif direction == 2:
        playerCurrent = playerSprites[direction].get_rect()
        return playerCurrent
    elif direction == 3:
        playerCurrent = playerSprites[direction].get_rect()
        return playerCurrent


def terminate():
    pygame.quit()
    sys.exit()