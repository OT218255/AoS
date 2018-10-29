import pygame, sys, mouse_tracking, event_loop


def event_resolve(events_list, entity_to_update):
    moving = False
    if events_list[0]:
        entity_to_update.y -= 44
        print("up")
    if events_list[1]:
        entity_to_update.x -= 44
        print("Left")
    if events_list[2]:
        entity_to_update.y += 44
        print("Down")
    if events_list[3]:
        entity_to_update.x += 44
        print("Right")
    if events_list[4]:
        terminate()
    game_state_update = [entity_to_update]
    return game_state_update
    # 0 = w 1 = a 2 = s 3 = d 4 = Quit
    # w = -y a = -x s = +y d = +x

def terminate():
    pygame.quit()
    sys.exit()