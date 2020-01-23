import os
import colorama
''' here I am looking to define all the constants from the game, like

length , breadth  , height etc

'''
rows, coloumns = os.popen('stty size', 'r').read().split()

shield_off_time = -100
shield_on_time = 50

window_for_running = 8

ROOF = 4
FLOOR = 4
# these are the dimensions of the floor and the roof

HEIGHT = 43 # approx length of the screen at the current full screen size
LENGTH_OF_GAME = 1500 # intended width ( basically the intended length of the game in terms of coloumns) 
FRAME_WIDTH = int(coloumns)


# board modes
NORMAL = 0
LOAD = 1
WELCOME = 2
END = 3
ENDGAME = 4



#game parameters

game_offset = 1
game_speed = 1
frame_speed = 0.1

# now we will make an array for getting the various shapes

SHAPES= {}
SHAPES['board'] = ' '
SHAPES['brick'] = '\033[2;43;33m#\033[22;49;39m'
SHAPES['mando'] = '\033[44;35mM\033[49;39m'
SHAPES['coins'] = '\033[39m$\033[39m'
SHAPES['rod'] = '\033[1;96m\\\033[22;39m'
SHAPES['brick'] = '\033[2;43;33m^\033[22;49;39m'
SHAPES['magnet'] = '\033[1;92mM\033[22;39m'


