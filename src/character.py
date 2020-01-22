import constants
import graphics


class character:
	''' everything is a character that has length , breadth, left x , bottom y '''

	def __init__(self, x , y):
		self._height = 3
		self._width = 3
		self._x_coordinate = x
		self._y_coordinate = y
		self._name = "none yet"

	def get_coordinates(self):
		return (int(self._x_coordinate) , int(self._y_coordinate))

	def set_coordinates(self, x, y):
		self._x_coordinate = x
		self._y_coordinate = y

	def get_dimensions(self):
		return (int(self._height) , int(self._width))

	def get_name(self):
		return (self._name)


	def move_right(self):
		# function to move right by a certain step
		return

	def move_up(self):
		return

	def move_left(self):
		return 
	
	def make_matrix(self, character):
		# now this character will be made into a proper character
		height, width = self.get_coordinates()
		matrix = []

		for _ in range(0, height):
			matrix.append([character] * width)

		self._matrix = matrix

	def set_matrix(self, matrix):
		self._matrix = matrix

	def get_matrix(self):
		return self._matrix
