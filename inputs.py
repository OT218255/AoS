import pygame, main
from pygame.locals import *

def getPixelAtClick(direction):
    mouseDownPos = pygame.mouse.get_pos()
    main.checkForQuit()
    mouseUpPos = getPointAtLift()
    direction = mousePositionCompair(mouseDownPos, mouseUpPos, direction)
    return direction

def getPointAtLift():
    mouseUp = False
    while mouseUp == False:
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouseUpPos = pygame.mouse.get_pos()
            mouseUp = True
        main.checkForQuit()
    pygame.event.clear()
    return mouseUpPos

def mousePositionCompair(mouseDown, mouseUp, direction):
    # print("The mouse positions are: ", mouseDown, mouseUp)
    if abs(mouseUp[0] - mouseDown[0]) > abs(mouseUp[1] - mouseDown[1]):
        if abs(mouseUp[0] - mouseDown[0]) > 100:
            if mouseDown[0] > mouseUp[0]:
                direction = 3
            else:
                direction = 1
        else:
            print('click')
    else:
        if abs(mouseUp[1] - mouseDown[1]) > 100:
            if mouseDown[1] > mouseUp[1]:
                direction = 0
            else:
                direction = 2
        else:
            print("click")
    return direction

def getDirection(directions, currentDirection):
    if currentDirection in directions:
        facingDirections = directions[currentDirection]
        return facingDirections
