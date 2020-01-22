import os
import time
import random
from random import randrange

import graphics
import character
from board import Board

#so that I initalise all the objects here and import them from here itself

from objects import *


import constants


class jetpack_joyrider:
    

    def get_game_offset(self):
        return self._game_offset
    
    def get_game_speed(self):
        return self._game_speed

    def get_frame_speed(self):
        return self._game_frame_speed

    def set_game_offset(self, offset):
        self._game_offset = offset

    def set_game_speed(self, speed):
        self._game_speed = speed

    def set_game_frame_speed(self, frame_speed):
        self._game_frame_speed = frame_speed


    def get_game_list_of_characters(self):
        return self._game_list_of_characters

    def set_game_list_of_characters(self, list_of_characters):
        self._game_list_of_characters = list_of_characters

    def __init__(self):
        self._game_offset = constants.game_offset
        self._game_speed = constants.game_speed
        self._game_frame_speed = constants.frame_speed

        self._game_list_of_characters = []

        game_board = Board()

        game_board.set_board_mode(constants.WELCOME)

        game_board.print_board(self._game_offset, self.get_game_list_of_characters())

        time.sleep(2)

        game_board.set_board_mode(constants.LOAD)

        game_board.print_board(self._game_offset,  self.get_game_list_of_characters())

        time.sleep(2)

        game_board.set_board_mode(constants.NORMAL)

        game_board.print_board(self._game_offset, self.get_game_list_of_characters())

        self.run_game_loop(game_board)


    def run_game_loop(self , game_board):
        list_of_characters = self.get_game_list_of_characters()
        x = self.get_game_offset() + 30
        y = constants.HEIGHT  + 1
        obj = person(x ,y)
        list_of_characters.append(obj)
        self.set_game_list_of_characters(list_of_characters)

        while 1:
            # # get the current status of the board and print the full board output
            # now what all does the board contain
            # 1. the roof
            # 2. the floor
            # 3. person
            # 4. coins / rods / magets ( collisons have to be detected with all of them and the scores modified accordingly)
            # 5. The moving background irrespective of the status of the present player 
            # 6. Bullets from the joyrider : kill magent in two bullets and the rods in one bullet 
            # 7. once we reach the last 100 of the game , we make the bad dragon active 
            # 8. once the bad dragon is active, he will shoot the big bullets, and that will be released at a massive speed

            # for starters, make all of this then we shall see what to do with the rest of the game

            offset = self.get_game_offset()


            ######################################################
            # this section we update all the object coordinates smhw and then we pass the list and get it into that matrix

            list_of_characters = self.get_game_list_of_characters()
            # now that we have the list of characters
            game_board.print_board(offset, list_of_characters)

            # time.sleep(self.get_game_speed())


            for obj in list_of_characters:
                # change coordinates generally then change coordinates object wise
                x , y = obj.get_coordinates()
                obj.set_coordinates(x - int(self.get_game_speed()), y)

                if obj.get_name() == "mando":
                    x, y = obj.get_coordinates()
                    print(x,offset,end=",")
                    if x < 0:
                        x = 0 
                    obj.set_coordinates(x , y)
                    x, y = obj.get_coordinates()
                    print(x)


                # now that we have set our coordinates ,we will incorporate it into our matrix for being drawn



            # now write code to make sure a new object spawns every 5 seconds
            if offset % 30 == 0:
                random_number = randrange(0,4)

                x = offset + int(constants.FRAME_WIDTH) - 100
                y =  randrange(10, 30)

                if random_number == 0:
                    obj = magnet(x , y)
                elif random_number == 1:
                    obj = coins(x , y)
                    obj2 = coins(x + 2 , y)
                    obj3 = coins(x + 4 , y)
                    list_of_characters.append(obj2)
                    list_of_characters.append(obj3)
                elif random_number == 2:
                    obj = horizontal_rod(x , y)
                elif random_number == 3:
                    obj = vertical_rod(x, y)

                list_of_characters.append(obj)


            self.set_game_list_of_characters(list_of_characters)
            ######################################################




            time.sleep(self.get_frame_speed())

            if offset == int(constants.LENGTH_OF_GAME) - 100 : # in other words , when the game is ending
                game_board.set_board_mode(constants.END)
                game_board.print_board(offset,  list_of_characters)
                break
            else:
                self.set_game_offset(offset + self.get_game_speed())


            # now we update the offset


            '''
    		1. Figure out a way to keep the board moving anyway, if input occurs then fine, else just m
            move the whole board forward and wait for input again. 

            2. once the input has been taken , then we take the appropriate action and move the board forward again
            => now what all actions can be there, 
                a. some collision 
                b. some bullet firing from either side
                c. some obstacle showing up. 
                d. I want a version of every obstacle every kind showing up every 3rd frame, 
            => update status with all of this, and then go back to printing the whole thing


			'''