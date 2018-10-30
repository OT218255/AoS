"""Holds function for creating the array used as the maze."""
import random


def create_room(width, height, spawnside):
    """
    Create an array of random numbers to act as the maze.
    
    Takes in width, height, and spawnside as variables to use when creating
    the maze. width and height determine its dimentions, while spawnside is
    used to generate the spawn tile and location of the exit door.
    
    :param width:           Width of the maze.
    :param height:          Height of the maze.
    :param spawnside:       Side the player spawns on.
    :return:                Returns the generated array.
    """
    a = [[0 for i in range(width)] for j in range(height)]
    # create an array full of 0

    ''' Creates walls, pits and floors  '''
    for x in range(height):
        for y in range(width):
            if x == 0 or x == height-1 or y == 0 or y == width-1:
                a[x][y] = 1  # if the tile is on the border, make it a wall
            else:
                makepit = random.randint(0, 4)
                if makepit == 0:        # a 25% chance to be a tile blocker
                    makepit = random.randint(0, 1)
                    if makepit == 0:    # a 50% chance to be a impassable wall
                        a[x][y] = 2
                    else:               # a 50% chance to be a pit obstacle
                        a[x][y] = 1
                else:              # a 3 in 4 chance to be a normal floor tile
                    a[x][y] = 0

    ''' Creates a door along a random wall  '''
    doorwall = random.randint(0, 3)  # chooses a random wall to place the door
    while doorwall == spawnside:  # makes sure that the wall doesnt appear on
        # the same side the player spawn
        doorwall = random.randint(0, 3)

    if doorwall == 0:  # top
        doorplace = random.randint(1, width-2)
        a[0][doorplace] = "U"
    elif doorwall == 1:  # right
        doorplace = random.randint(1, height-2)
        a[doorplace][width-1] = "R"
    elif doorwall == 2:  # bottom
        doorplace = random.randint(1, width-2)
        a[height-1][doorplace] = "D"
    else:  # left
        doorplace = random.randint(1, height-2)
        a[doorplace][0] = "L"

    ''' Creates a random spawn tile along chosen wall '''
    if spawnside == 0:  # top
        spawnplace = random.randint(1, width-2)
        a[1][spawnplace] = 'X'
    elif spawnside == 1:  # right
        spawnplace = random.randint(1, height-2)
        a[spawnplace][width - 2] = 'X'
    elif spawnside == 2:  # bottom
        spawnplace = random.randint(1, width-2)
        a[height - 2][spawnplace] = 'X'
    else:  # left
        spawnplace = random.randint(1, height-2)
        a[spawnplace][1] = 'X'

    ''' Prints the array in a nice format, for debugging purposes '''
    for row in a:
        for col in row:
            print(col, end=" ")
        print()

    return a
