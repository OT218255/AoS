import main, pygame,
from pygame.locals import *

    enemyClass = enemy.Enemy()

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

    while True:
        enemySprite = enemy.Enemy.loadSprite(enemyClass, "UP") # Returns directional sprite
        DISPLAYSURF.blit(enemySprite, (750, 580))  # Blits enemy sprite to screen with updated x and y
        pygame.display.flip()