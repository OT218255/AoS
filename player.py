import pygame, const
from pygame.locals import *
from const import *


class Player(object):
    def loadSprite(self, direction): # This just loads the spites dummy
        playerSprite = pygame.image.load("Assets/Art/BasicBoiUp.PNG")
        if direction == "UP":
            playerSprite = pygame.image.load("Assets/Art/BasicBoiUp.PNG")
        elif direction == "RIGHT":
            playerSprite = pygame.image.load("Assets/Art/BasicBoiRight.PNG")
        elif direction == "DOWN":
            playerSprite = pygame.image.load("Assets/Art/BasicBoiDown.PNG")
        elif direction == "LEFT":
            playerSprite = pygame.image.load("Assets/Art/BasicBoiLeft.PNG")
        return playerSprite

def moveUpdate(glideX, glideY, x, y):
    if x > glideX: # If x is greater than glide x subtract SPEED from x
        x -= SPEED
    elif x < glideX: # If x is lower than glide x add SPEED from x
        x += SPEED

    if y > glideY: # If y is greater than glide y subtract SPEED from y
        y -= SPEED
    elif y < glideY: # If y is lower than glide y add SPEED to y
        y += SPEED
    return x, y

def changeXandY(x, y, movementDirection):
    glideX, glideY = x, y # sets the destination x and y to the current x and y
    if movementDirection == "UP": # If movemntDirection is set to up subtract TILESIZE from glide y
        glideY -= TILESIZE
    elif movementDirection == "RIGHT": # If movementDirection is set to RIGHT add TILESIZE to glide x
        glideX += TILESIZE
    elif movementDirection == "DOWN": # If movementDirection is set to DOWN add TILESIZE to glide y
        glideY += TILESIZE
    elif movementDirection == "LEFT": # If movementDirection is set to LEFT subtract TILESIZE to glide x
        glideX -= TILESIZE
    return glideX, glideY