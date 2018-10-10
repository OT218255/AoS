import pygame, sys, inputs # import the module
from pygame.locals import *


def main():
    pygame.init()
    FPS = 30
    WINDOWWIDTH = 1334 # Window width constant
    WINDOWHEIGHT = 750 # Window height constant
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Main surface
    FPSCLOCK = pygame.time.Clock() # clock
    playerDirection = 0
    DIRECTIONS = {0: "UP", 1: "RIGHT", 2: "DOWN", 3: "LEFT"}
    while True:
        for event in pygame.event.get(MOUSEBUTTONDOWN):
            playerDirection = inputs.getPixelAtClick(playerDirection)
            print(playerDirection)
        checkForQuit() # Moved the quit code into a function (feel free to ask me why and I'll explain)
        pygame.display.flip() # Updates the display
        FPSCLOCK.tick(FPS)


def terminate(): # This function just quits
    pygame.quit()
    sys.exit()


def checkForQuit(): # this function checks if the events for quit are met
    for event in pygame.event.get(QUIT):
        terminate()


if __name__ == "__main__":
    main()
