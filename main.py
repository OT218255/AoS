import pygame, sys, inputs, const, player, random  # import the module
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
    glideX, glideY = 0, 0
    moving = False
    while True:
        event = getEvent() # checks to see if the mouse button is down
        if event == MOUSEBUTTONDOWN:
            if moving == False: # If the player is not moving
                playerDirection = inputs.getPixelAtClick(playerDirection, event)
                facingDirection = inputs.getDirection(DIRECTIONS, playerDirection)
                moving = True  # Sets moving to true so that another movement cannot be made
            glideX, glideY = player.changeXandY(x, y, facingDirection) # sets destination x and y for sprite
        if moving: # If moving is true
            while x != glideX or y != glideY: # while the x and y are not the same as the glide x and y
                DISPLAYSURF.fill(background) # fill the background to remove previous drawings
                x, y = player.moveUpdate(glideX, glideY, x, y) # Sets x and y to x and y +/- SPEED
                playerSprite = player.Player.loadSprite(playerClass, facingDirection) # Returns directional sprite
                DISPLAYSURF.blit(playerSprite, (x, y)) # Blits player sprite to screen with updated x and y
                pygame.display.flip()
                FPSCLOCK.tick(FPS)
        moving = False
        checkForQuit(event) # Moved the quit code into a function (feel free to ask me why and I'll explain)
        pygame.display.flip() # Updates the display
        FPSCLOCK.tick(FPS)


def terminate(): # This function just quits
    pygame.quit()
    sys.exit()


def checkForQuit(event): # this function checks if the events for quit are met
    if event == QUIT:
        terminate()

def getEvent():
    for event in pygame.event.get():
        return event.type

if __name__ == "__main__":
    main()
