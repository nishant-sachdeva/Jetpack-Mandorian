import os
import constants
import graphics
import math

from character import character

class magnet(character):
	# so we have a class that will make all the things including
	# such as player, coins, obstacles
	def __init__(self ,x , y):
		# add the object to the list of all the objects
		self._name = "magnet"
		self._height = 3
		self._width = 3
		self._x_coordinate = x
		self._y_coordinate = y
		char = constants.SHAPES['magnet']

		self.make_matrix(char)


class coins(character):
	def __init__(self, x , y):
		self._name = "coin"
		self._height = 2
		self._width = 2
		self._x_coordinate = x
		self._y_coordinate = y
		char = constants.SHAPES['coins']

		self.make_matrix(char)



class person(character):
	def __init__(self, x_coordinate , y_coordinate):
		#add the object to the list of all objects
		self._name = "mando"
		self._height = 4
		self._width = 4
		self._gravity_constant = 0
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = constants.SHAPES['mando']

		self.make_matrix(char)

	def get_gravity_contant(self):
		return self._gravity_constant

	def set_gravity_constant(self, constant):
		self._gravity_constant = constant

	def move_left(self, amount):
		x , y = self.get_coordinates()
		x = x-amount

		if x < 0:
			x = 0

		self.set_coordinates(x , y)
		return 0 

	def move_right(self, amount):
		x , y = self.get_coordinates()
		x = x + amount

		if x > 60:
			x = 60
		self.set_coordinates(x, y)

	def move_up(self, amount):
		self.set_gravity_constant(0)
		x , y = self.get_coordinates()
		y = y + amount
		# x = x + amount

		if x > 60:
			x = 60

		if y <= 44:
			y = 44

		if y >= 75:
			y = 75

		print(str(x) + "  "+  str(y))
		self.set_coordinates(x , y)


	def fall_down(self):
		x , y = self.get_coordinates()
		y  = math.floor(y - self.get_gravity_contant())

		x = x + int(constants.game_speed)

		if y >= 75:
			y = 75
		if y <= 44:
			y = 44

		self.set_coordinates(x , y)
		self.set_gravity_constant(self.get_gravity_contant() + 0.1)


class horizontal_rod(character):
	def __init__(self, x_coordinate , y_coordinate):

		self._name = "horizontal rod"

		# add the object to the list of all objects
		self._height = 5
		self._width = 2
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = constants.SHAPES['rod']

		self.make_matrix(char)



class vertical_rod(character):
	def __init__(self,  x_coordinate , y_coordinate):

		self._name = "vertica_rod"

		# add the object to the list of all objects
		self._height = 2
		self._width = 5
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = constants.SHAPES['rod']

		self.make_matrix(char)



class bullet(character):
	def __init__(self, x_coordinate , y_coordinate):

		self._name = "bullet"

		# add the object to the list of all objects
		self._height = 1
		self._width = 2
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = ">"

		self.make_matrix(char)


	def move_left(self, amount):
		# here we will simply move our guy :RIGHT: by double the given amount, and they are suppossed to
		# gets destroyed if they collide with any obstacle and that obstacle also dies with it ,
		# every time a bullet collides, we get some score
		x , y = self.get_coordinates()
		x = x + 2

		if x == int(constants.FRAME_WIDTH):
			return -1
		self.set_coordinates(x , y)
		return 0



class final_monster(character):
	def __init__(self, height, width , x_coordinate  , y_coordinate):
		# add the guy to the list of special objects
		# we will import it's graphic and make it's matrix right here, nothing to worry about here, 
		return