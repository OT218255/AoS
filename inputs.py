import pygame, main
from pygame.locals import *


def getPixelAtClick(direction, event):
    mouseDownPos = pygame.mouse.get_pos()
    mouseUpPos = getPointAtLift(event)
    direction = mousePositionCompair(mouseDownPos, mouseUpPos, direction)
    return direction


def getPointAtLift(event):
    mouseUp = False
    while mouseUp == False:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouseUpPos = pygame.mouse.get_pos()
                mouseUp = True
    return mouseUpPos


def mousePositionCompair(mouseDown, mouseUp, direction):
    if abs(mouseUp[0] - mouseDown[0]) > abs(mouseUp[1] - mouseDown[1]):#if X movement is greater than Y movement
        if abs(mouseUp[0] - mouseDown[0]) > 100: #if X movement if greater than 100 pixels (swipe, not a click)
            if mouseDown[0] > mouseUp[0]: #checks if X movement is left or right
                direction = 3
            else:
                direction = 1
        else:
            print('click')
    else:
        if abs(mouseUp[1] - mouseDown[1]) > 100: #if Y movement is greater than 100
            if mouseDown[1] > mouseUp[1]: #checks is the Y movement is up or down
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

