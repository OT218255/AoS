import main, pygame
from pygame.locals import *

class Enemy(object):
    def loadSprite(self, direction): # This just loads the spites dummy
        enemySprite = pygame.image.load("Assets/Art/BadBoiUp.PNG")
        if direction == "UP":
            enemySprite = pygame.image.load("Assets/Art/BadBoiUp.PNG")
        elif direction == "RIGHT":
            enemySprite = pygame.image.load("Assets/Art/BadBoiRight.PNG")
        elif direction == "DOWN":
            enemySprite = pygame.image.load("Assets/Art/BadBoiDown.PNG")
        elif direction == "LEFT":
            enemySprite = pygame.image.load("Assets/Art/BadBoiLeft.PNG")
        return enemySprite
