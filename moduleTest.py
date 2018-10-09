import pygame # imports the required library for this task
def drawRectangle(display): # defines the function
    green = (0, 255, 0) # sets a green constant
    square = pygame.Rect(0, 0, 44, 44) # stores the square
    pygame.draw.rect(display, green, square) # draws the square on the passed surface.