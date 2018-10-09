import pygame,sys
from pygame.locals import *

def main():
    pygame.init()
    FPS = 30
    WINDOWWIDTH = 1334
    WINDOWHEIGHT = 750
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()


