import pygame
from pygame.locals import *

class Player(object):
    def loadSprite(self, direction):
        playerSprite = pygame.image.load("Assets/Art/SandDoorUp.PNG")
        if direction == "UP":
            playerSprite = pygame.image.load("Assets/Art/SandDoorUp.PNG")
        elif direction == "RIGHT":
            playerSprite = pygame.image.load("Assets/Art/SandDoorRight.PNG")
        elif direction == "DOWN":
            playerSprite = pygame.image.load("Assets/Art/SandDoorDown.PNG")
        elif direction == "LEFT":
            playerSprite = pygame.image.load("Assets/Art/SandDoorLeft.PNG")
        return playerSprite

#    def drawSprite(self, sprite):
