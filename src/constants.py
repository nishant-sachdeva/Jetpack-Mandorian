import os
''' here I am looking to define all the constants from the game, like

length , breadth  , height etc

'''
rows, coloumns = os.popen('stty size', 'r').read().split()


ROOF = max( 1, int(rows)/10)
FLOOR = max(1 , int(rows)/10)
# these are the dimensions of the floor and the roof

HEIGHT = 40 # approx length of the screen at the current full screen size
LENGTH_OF_GAME = 700 # intended width ( basically the intended length of the game in terms of coloumns) 
FRAME_WIDTH = int(coloumns)


# board modes
NORMAL = 0
LOAD = 1
WELCOME = 2
END = 3



#game parameters

game_offset = 1
game_speed = 1
frame_speed = 0.1

# now we will make an array for getting the various shapes

SHAPES= {}
SHAPES['board'] = ' '
SHAPES['brick'] = '\033[2;43;33m#\033[22;49;39m'