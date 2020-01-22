import constants
import graphics


class character:
	''' everything is a character that has length , breadth, left x , bottom y '''

	def __init__(self, height, width , x , y):
		self._height = height
		self._width = width
		self._x_coordinate = x
		self._y_coordinate = y

	def get_coordinates(self):
		return (self._x_coordinate , self._y_coordinate)

	def get_dimensions(self):
		return (self._height , self._width)

	def move_right(self):
		# function to move right by a certain step
		return

	def move_left (self):
		# function to move left by a certain step
		return

	def render_on_screen(self):
		return
		# to place the thing on the screen, I will have to learn how to do this part, I am not very clear on this