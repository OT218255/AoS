"""Holds function for creating the array used as the maze."""
import random


def create_room(width, height, spawnside):
    """
    Create am array of random numbers to act as the maze.

    Takes in width, height, and spawnside as variables to use when creating
    the maze. width and height determine its dimensions, while spawnside is
    used to generate the spawn tile and location of the exit door.
    """
    array = [[0 for i in range(width)] for j in range(height)]
    # create an array full of 0
    check_routeable = False
    while not check_routeable:
        ''' Creates walls, pits and floors  '''
        for x in range(height):
            for y in range(width):
                if x == 0 or x == height-1 or y == 0 or y == width-1:
                    array[x][y] = 1  # if the tile is on the border, make wall
                else:
                    makepit = random.randint(0, 4)
                    if makepit == 0:        # a 25% chance to be a tile blocker
                        makepit = random.randint(0, 1)
                        if makepit == 0:    # a 50% chance to be a wall
                            array[x][y] = 2
                        else:               # a 50% chance to be a pit obstacle
                            array[x][y] = 1
                    else:              # a 3 in 4 chance to be a  floor tile
                        array[x][y] = 0

        ''' Creates a door along a random wall  '''
        doorwall = random.randint(0, 3)  # chooses a random wall to place door
        while doorwall == spawnside:  # makes sure that the wall doesnt appear
            # on the same side the player spawn
            doorwall = random.randint(0, 3)

        if doorwall == 0:  # top
            doorplace = random.randint(1, width-2)
            array[0][doorplace] = "U"
        elif doorwall == 1:  # right
            doorplace = random.randint(1, height-2)
            array[doorplace][width-1] = "R"
        elif doorwall == 2:  # bottom
            doorplace = random.randint(1, width-2)
            array[height-1][doorplace] = "D"
        else:  # left
            doorplace = random.randint(1, height-2)
            array[doorplace][0] = "L"

        ''' Creates a random spawn tile along chosen wall '''
        if spawnside == 0:  # top
            spawnplace = random.randint(1, width-2)
            array[1][spawnplace] = 'X'
        elif spawnside == 1:  # right
            spawnplace = random.randint(1, height-2)
            array[spawnplace][width - 2] = 'X'
        elif spawnside == 2:  # bottom
            spawnplace = random.randint(1, width-2)
            array[height - 2][spawnplace] = 'X'
        else:  # left
            spawnplace = random.randint(1, height-2)
            array[spawnplace][1] = 'X'

        ''' Prints the array in a nice format, for debugging purposes '''
        for row in array:
            for col in row:
                print(col, end=" ")
            print()

        check_routeable = check_for_route(array)

    return array


def check_for_route(tile_array):
    """
    A function that determines whether or not a given array is routeable.

    Takes in the tile array generated in create_room, and using a routing
    algorithm finds out if there is a successful route from the start to the
    exit door (X is the start, and other letters are the respective exits)

    :param tile_array:  The array generated in create_room, with the locations
                        of each tile in its spaces
    :return:            Returns a Boolean, for whether the given maze has a
                        passable route or not
    """
    array = [[[0 for i in range(4)]
              for j in range(len(tile_array))]
             for k in range(len(tile_array[0]))]
    """For this array, the final lists values will be:
    array[x][y][0] : A Boolean, to show whether the cell has been visited
    array[x][y][1] : An Int, to show distance from spawn tile
    array[x][y][2] : An Int, to show distance from exit tile
    array[x][y][4] : An Int, which is the total of both previous distances
    """

    for y in range(len(array[0])):
        for x in range(len(array)):
            if tile_array[y][x] == 1 or tile_array[y][x] == 2:
                array[x][y][0] = True      # marks as visited
                array[x][y][1] = 99     # walls and pits are made high value
                array[x][y][2] = 99     # distance to this tile is too high and
                array[x][y][3] = 99     # practically unreachable
            elif tile_array[y][x] == 'X':
                array[x][y][0] = False  # marks as unvisited
                spawn_tile_loc = (x, y)  # notes the location of thr spawn
                # array[spawn_tile_loc[0]][spawn_tile_loc[1]] =
            elif tile_array[y][x] == 'U'\
                    or tile_array[y][x] == 'R'\
                    or tile_array[y][x] == 'L'\
                    or tile_array[y][x] == 'D':  # wrapped statements ugly :(
                array[x][y][0] = False
            else:  # tile is a floor tile ( 0 )
                array[x][y][0] = False
                exit_tile_loc = (x, y)  # marks the location of the exit
            print(array[x][y][1], end=" ")
        print()

    # use some kind of tree? recursion would work fine.
    # RECURSION

    return True
