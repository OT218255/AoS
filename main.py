import pygame, sys, inputs, const, player  # import the module
from pygame.locals import *
from const import *


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Main surface
    FPSCLOCK = pygame.time.Clock() # clock
    playerDirection = 0
    facingDirection = ""
    DIRECTIONS = {0: "UP", 1: "RIGHT", 2: "DOWN", 3: "LEFT"}
    playerClass = player.Player()
    x, y = 0, 0
    moving = False
    while True:
        for event in pygame.event.get(MOUSEBUTTONDOWN): # checks to see if the mouse button is down
            if moving == False:
                playerDirection = inputs.getPixelAtClick(playerDirection)
                facingDirection = inputs.getDirection(DIRECTIONS, playerDirection) # returns string direction from dict
            x, y = changeXandY(x, y, facingDirection)
            moving = True
        if moving:
            DISPLAYSURF.fill(background)
            playerSprite = player.Player.loadSprite(playerClass, facingDirection)
            DISPLAYSURF.blit(playerSprite, (x, y))
            moving = False
        checkForQuit() # Moved the quit code into a function (feel free to ask me why and I'll explain)
        pygame.display.flip() # Updates the display
        FPSCLOCK.tick(FPS)


def changeXandY(x, y, movementDirection):
    if movementDirection == "UP":
        y -= 44
    elif movementDirection == "RIGHT":
        x += 44
    elif movementDirection == "DOWN":
        y += 44
    elif movementDirection == "LEFT":
        x -= 44
    return x, y

def terminate(): # This function just quits
    pygame.quit()
    sys.exit()


def checkForQuit(): # this function checks if the events for quit are met
    for event in pygame.event.get(QUIT):
        terminate()


if __name__ == "__main__":
    main()
