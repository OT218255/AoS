import pygame, main
from pygame.locals import *

def getPixelAtClick():
    mouseDownPos = pygame.mouse.get_pos()
    print(mouseDownPos)
    main.checkForQuit()
    mouseUpPos = getPointAtLift()
    mousePositionCompair(mouseDownPos, mouseUpPos, 0)

def getPointAtLift():
    mouseUp = False
    while mouseUp == False:
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouseUpPos = pygame.mouse.get_pos()
            mouseUp = True
            print(mouseUpPos)
        main.checkForQuit()
    pygame.event.clear()
    return(mouseUpPos)

def mousePositionCompair(mouseDown, mouseUp, direction):
    print("The mouse positions are: ", mouseDown, mouseUp)
    if mouseUp[0] > mouseDown[0]:
        direction += 1
    if mouseUp[0] < mouseDown[0]:
        direction -= 1
    print(direction)