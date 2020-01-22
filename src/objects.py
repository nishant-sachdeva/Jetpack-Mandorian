import os
import constants
import graphics
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
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = constants.SHAPES['mando']

		self.make_matrix(char)




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
	def __init__(self, height , width , x_coordinate , y_coordinate):

		self._name = "horizontal rod"

		# add the object to the list of all objects
		self._height = 1
		self._width = 2
		self._x_coordinate = x_coordinate
		self._y_coordinate = y_coordinate
		char = ">"

		self.make_matrix(char)



class final_monster(character):
	def __init__(self, height, width , x_coordinate  , y_coordinate):
		# add the guy to the list of special objects
		# we will import it's graphic and make it's matrix right here, nothing to worry about here, 
		return