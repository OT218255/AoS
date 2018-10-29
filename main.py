import pygame, sys, random, event_loop, game_loop, render_loop, consts, load_assets, entity
from pygame.locals import *
from consts import *

def main():
    events_list = intialise_events()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    FPS_CLOCK = pygame.time.Clock()
    player_sprites, enemy_sprites, environment_sprites = load_assets.load_sprites()
    player_sprites, enemy_sprites, environment_sprites = convert_images(player_sprites,
                                                                        enemy_sprites,
                                                                        environment_sprites)
    player = entity.Entity("player", player_sprites, 0, 0)

    while True:
        events_list = event_loop.get_events(events_list)
        game_state_list = game_loop.event_resolve(events_list)
        render_loop.display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list)
        events_list = clear_events(events_list)


def intialise_events():
    w_key_press = False
    a_key_press = False
    s_key_press = False
    d_key_press = False
    quit_event = False
    events_list = [w_key_press, a_key_press, s_key_press, d_key_press, quit_event]
    return events_list


def convert_images(player_sprites, enemy_sprites, environment_sprites):
    for i in range(len(player_sprites)):
        player_sprites[i].convert()
    for i in range(len(enemy_sprites)):
        enemy_sprites[i].convert()
    for i in range(len(environment_sprites)):
        environment_sprites[i].convert()
    return player_sprites, enemy_sprites, environment_sprites


def clear_events(events_list):
    for i in range(len(events_list)):
        events_list[i] = False
    return events_list

if __name__ == "__main__":
    main()
