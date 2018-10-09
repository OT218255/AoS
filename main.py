import pygame, sys, moduleTest # import the module
from pygame.locals import *


def main():
    pygame.init()
    FPS = 30
    WINDOWWIDTH = 1334 # Window width constant
    WINDOWHEIGHT = 750 # Window height constant
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Main surface
    FPSCLOCK = pygame.time.Clock() # clock
    while True:
        moduleTest.drawRectangle(DISPLAYSURF) # Example of calling a function from a module.
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
