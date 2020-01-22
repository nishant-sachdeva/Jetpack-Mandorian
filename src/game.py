import os
import time

import graphics
import character
from board import Board

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

    def __init__(self):
        self._game_offset = constants.game_offset
        self._game_speed = constants.game_speed
        self._game_frame_speed = constants.frame_speed
        game_board = Board()

        game_board.set_board_mode(constants.WELCOME)

        game_board.print_board(self._game_offset)

        time.sleep(2)

        game_board.set_board_mode(constants.LOAD)

        game_board.print_board(self._game_offset)

        time.sleep(2)

        game_board.set_board_mode(constants.NORMAL)

        game_board.print_board(self._game_offset)

        self.run_game_loop(game_board)


    def run_game_loop(self , game_board):

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

            game_board.print_board(offset)


            time.sleep(self.get_frame_speed())

            if offset == 500 :
                game_board.set_board_mode(constants.END)
                game_board.print_board(offset)
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