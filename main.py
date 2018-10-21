import pygame, sys, random, event_loop, game_loop, render_loop, consts, load_assets, player
from pygame.locals import *
from consts import *


def main():
    mouse_down = False
    mouse_up = False
    quit_event = False
    events_list = [mouse_down, mouse_up, quit_event]
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    FPS_CLOCK = pygame.time.Clock()
    player_sprites, enemy_sprites, environment_sprites = load_assets.load_sprites()
    player_sprites, enemy_sprites, environment_sprites = convert_images(player_sprites,
                                                                        enemy_sprites,
                                                                        environment_sprites)
    while True:
        events_list = event_loop.get_events(events_list)
        game_state_list = game_loop.all_states_update(events_list, player_sprites, enemy_sprites, environment_sprites)
        render_loop.display_update(DISPLAY_SURFACE, FPS_CLOCK, game_state_list)
        events_list = clear_events(events_list)


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