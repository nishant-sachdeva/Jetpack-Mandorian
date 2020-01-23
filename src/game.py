import os
import time
import random
from random import randrange

import graphics
import character
from board import Board
from input import *

#so that I initalise all the objects here and import them from here itself

from objects import *


import notify2

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

    def move_game_objects(self, amount):
        list_of_characters = self.get_game_list_of_characters()
        for obj in list_of_characters:
            response = obj.move_left(amount)
            
            if response == -1:
                list_of_characters.remove(obj)

            if obj.get_name() == "mando":
                    obj.fall_down()


        self.set_game_list_of_characters(list_of_characters)

        return

    def generate_obstacles(self, offset):
        list_of_characters = self.get_game_list_of_characters()

        if offset % int(constants.window_for_running) == 0:
            random_number = randrange(0,4)
            x = offset + int(constants.FRAME_WIDTH) - 110
            y =  randrange(44, 75)

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

        return

    def get_quit_status(self):
        return self._game_quit
    def set_quit_status(self, status):
        self._game_quit = status

    def deal_with_user_input(self):
        character = get_input()
        mando_object = person(0 , 0)
        list_of_characters = self.get_game_list_of_characters()
        for obj in list_of_characters:
            if obj.get_name() == "mando":
                mando_object = obj
                break


        if character == 'a':
            # print("move left")
            mando_object.move_left(2*self.get_game_speed())

        elif character == 'd':
            # print("move right")
            mando_object.move_right(2*self.get_game_speed())

        elif character == 'w':
            # print("fly around")
            mando_object.move_up(2)

        elif character == 'b':
            self.boost_mode_activate()

        elif character == 'm':
            self.want_to_deal_with_magnets()


        elif character == ' ' :
            x , y = mando_object.get_coordinates()
            h, w = mando_object.get_dimensions()
            bullet_object = bullet(x + w -1 , y + h -2)
            list_of_characters.append(bullet_object)
            self.set_game_list_of_characters(list_of_characters)
            # here , we initalise a bullet for the mando
        elif character == 'q':
            self.set_quit_status(1)# quit the game 

        elif character == 's':
            self.activate_shield()
            # we activate the shield for 20 seconds if it's timer is currently at -100

        return

    def activate_shield(self):
        if self._shield_timer == int(constants.shield_off_time):
            self._shield_timer = int(constants.shield_on_time)
            self._shield_status = 1
        else:
            print("shield cannot be activated yet")

    def get_game_score(self):
        return self._game_score

    def set_game_score(self, score):
        self._game_score = score

    def get_game_lives(self):
        return self._game_lives

    def set_game_lives(self, lives):
        self._game_lives = lives

    def get_game_time(self):
        return int(constants.LENGTH_OF_GAME) - int(self.get_game_offset())

    def set_game_time(self, time):
        self._game_time = time

    def get_shield_status(self):
        return self._shield_status

    def want_to_deal_with_magnets(self):
        self._deal_with_magnet = 1 - self._deal_with_magnet

    def is_magnet(self):
        return self._deal_with_magnet

    def __init__(self):

        self._game_lives = 5
        self._game_score = 0
        self._game_time = int(constants.LENGTH_OF_GAME) - int(constants.game_offset)

        self._deal_with_magnet = 0
        self._speed_boost = 0
        self._game_quit = 0
        self._game_offset = constants.game_offset
        self._game_speed = constants.game_speed
        self._game_frame_speed = constants.frame_speed

        self._shield_timer = int(constants.shield_off_time)
        self._shield_available = 1
        self._shield_status = 0

        self._game_list_of_characters = []

        self._boss_mode = 0

        game_board = Board()

        game_board.set_board_mode(constants.WELCOME)

        game_board.print_board(self._game_offset, self.get_game_list_of_characters(), "")

        time.sleep(2)

        game_board.set_board_mode(constants.LOAD)

        game_board.print_board(self._game_offset,  self.get_game_list_of_characters(), "")

        time.sleep(2)

        game_board.set_board_mode(constants.NORMAL)

        game_board.print_board(self._game_offset, self.get_game_list_of_characters(), "")

        self.run_game_loop(game_board)


    def boost_mode_activate(self):
        self._speed_boost = 1  - self._speed_boost

    def is_boost_mode(self):
        return self._speed_boost

    def print_status(self):
        return ("\tScore = ", self.get_game_score() , '\t Magnetic Attraction = ' , self.is_magnet() , '\t Lives = ', self.get_game_lives(), '\t Time = ', self.get_game_time() ,  '\tSHIELD AVAILABLE = ', self._shield_available ,  '\t SHIELD STATUS : ',  self.get_shield_status() , '\t BOOST ' , self.is_boost_mode())

    def adjust_for_collisions(self):
        # return
        # so here we need the list of all objects
        list_of_characters = self.get_game_list_of_characters()
        # return
        for item in list_of_characters:
            if item.get_name() == "mando":
                # check for collisions with everyone
                for obj in list_of_characters:
                    if obj.get_name() != "bullet" and obj.get_name() != "mando" and self.get_shield_status() == 0:
                        # now get the collision conditions
                        itemx , itemy = item.get_coordinates()
                        objx , objy =  obj.get_coordinates()

                        if abs(objx - itemx) <= 3 and abs(itemy - objy) <= 3 :
                            # then we have a collision
                            # print(obj.get_name())
                            if obj.get_name() == "coin":
                                self.set_game_score(self.get_game_score() + 5)
                            else:
                                self.set_game_lives(self.get_game_lives() -1)

                            list_of_characters.remove(obj)

            elif item.get_name() == "bullet":

                for obj in list_of_characters:
                    if obj.get_name() != "bullet" and obj.get_name() != "mando" and obj.get_name() != "coin":
                        
                        itemx , itemy = item.get_coordinates()
                        objx , objy = obj.get_coordinates()
                        if abs(objx - itemx) <= 3 and abs(itemy - objy) <= 3 :
                            # then" we have a collision
                            # print("bullet just hit " + obj.get_name())

                            self.set_game_score(self.get_game_score() + 5)

                            try:
                                list_of_characters.remove(obj)
                                list_of_characters.remove(item)
                                
                            except:
                                pass

        self.set_game_list_of_characters(list_of_characters)


    def do_we_need_to_quit(self):
        if self.get_game_time() <= 0:
            return 1
        elif self.get_game_lives() <= 0:
            return 1

        # so far these are the conditions when the game should end

        return 0

    def deal_with_magnets(self):
        list_of_characters = self.get_game_list_of_characters()
        mando_object = person(0 ,0)
        for item in list_of_characters:
            if item.get_name() == "mando":
                mando_object = item
                break

        # so now we have the mando object, and now we will take every magent and deal with it's effect
        mandox, mandoy = mando_object.get_coordinates()

        for item in list_of_characters:
            if item.get_name() == "magnet":
                x , y = item.get_coordinates()

                # now we apply the small changes
                changex = int(x - mandox)/40
                changey = int(y - mandoy)/40

                mando_object.move_right(changex)
                mando_object.move_up(changey)


    def run_game_loop(self , game_board):
        list_of_characters = self.get_game_list_of_characters()
        x = self.get_game_offset() + 30
        y = constants.HEIGHT  + 1
        obj = person(x ,y)
        list_of_characters.append(obj)
        self.set_game_list_of_characters(list_of_characters)

        while 1:
           
            offset = self.get_game_offset()

            list_of_characters = self.get_game_list_of_characters()

            print_string = self.print_status()

            
            game_board.print_board(offset, self.get_game_list_of_characters() , print_string)

            if self._boss_mode == 0:
                if self.is_boost_mode() == 1:
                    self.move_game_objects(5 * self.get_game_speed())
                else:
                    self.move_game_objects(1* self.get_game_speed())
                
                self.generate_obstacles(offset)            

                if self.is_magnet() == 1 and self.get_shield_status() == 0:
                    self.deal_with_magnets()
    

            self.deal_with_user_input()

            
            self.adjust_for_collisions()

            response = self.do_we_need_to_quit()

            if self.get_quit_status() == 1 or response == 1:
                game_board.set_board_mode(constants.END)
                empty_list_of_characters = []
                game_board.print_board(offset, empty_list_of_characters, "")
                break
            ######################################################

            time.sleep(self.get_frame_speed())

            ## this section is to deal with the ending portions of the game

            if self._shield_timer > int(constants.shield_off_time):
                self._shield_timer = self._shield_timer - 1
            else:
                self._shield_available = 1

            if self._shield_timer == 0:
                self._shield_status = 0
                self._shield_available = 0

            if offset >= int(constants.LENGTH_OF_GAME) - 100 : # in other words , when the game is ending
                monster = final_monster(offset + 50 , 55 , 7)
                mando_object = person(offset + 10, constants.HEIGHT + 1)
                new_list = []
                new_list.append(monster)
                new_list.append(mando_object)
                self.set_game_list_of_characters(new_list)
                game_board.set_board_mode(constants.ENDGAME)
                game_board.print_board(offset,  self.get_game_list_of_characters(), "ENDGAME  NOW!!")
                self._boss_mode = 1
            else:
                if self.is_boost_mode() == 1:
                    self.set_game_offset(offset + self.get_game_speed())
                else:
                    self.set_game_offset(offset + self.get_game_speed())




