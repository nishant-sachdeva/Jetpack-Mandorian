import character
import constants

from os import name , system

class Board:
	''' so now we have the character class for our board, 
	the thing to note however is that ,the floor and roof remain as is, it is just the characters that are
	gonna be moving constantly

	So , here is what I am gonna do ,
	before I initialise the jetpack joyrider, I will initialise the board after the welcome message of course
	'''

	def __init__(self):
		self._board_mode = constants.LOAD
		# board ka matrix initalise karo

	def get_board_mode(self):
		return self._board_mode

	def set_board_mode(self , mode):
		self._board_mode = mode

	def clear_screen(self):
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')

	def print_board(self):
		self.clear_screen()
		#print the basic roof and floor parts

		current_mode = self.get_board_mode()

		if current_mode == constants.WELCOME:
			print("WELCOME")
		elif current_mode == constants.LOAD:
			# print the ascii for START in the middle
			print("LOADING")
		elif current_mode == constants.NORMAL:
			# print all the objects as per the list of objects in the board ,
			print("GAME LOOP")



	# these two funcitions are gonna be taking care of getting and setting the modes for the matrix that is the whole board


