import character
import numpy
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


	def initalise_board_matrix(self):
		matrix = []

		main_board_char = constants.SHAPES['board']
		roof_and_floor_char = constants.SHAPES['brick']

		for _ in range(0, int(constants.ROOF)):
			matrix.append([roof_and_floor_char] * constants.LENGTH_OF_GAME)

		for _ in range(int(constants.ROOF) , int(constants.HEIGHT - constants.FLOOR)):
			matrix.append([main_board_char] * constants.LENGTH_OF_GAME)

		for _ in range( int(constants.HEIGHT) - int(constants.FLOOR) ,  int(constants.HEIGHT)):
			matrix.append( [roof_and_floor_char] * constants.LENGTH_OF_GAME)


		self._board_matrix = matrix
		# board ka matrix initalise karo

	def get_board_mode(self):
		return self._board_mode

	def set_board_matrix(self , matrix):
		self._board_matrix = matrix

	def set_board_mode(self , mode):
		self._board_mode = mode

	def get_matrix(self):
		return self._board_matrix

	def clear_screen(self):
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')

	def print_floor_and_roof(self, offset):
		''' renders the board frame by frame '''
		matrix = self.get_matrix()
		# so now we have the matrix , and we will simly render later
		print("\033c", end="")
		
		for i in matrix:
			for j in i[offset:offset + constants.FRAME_WIDTH]:
				print(j, end='')
			print('')




	def print_board(self, offset):
		# self.clear_screen()
		print("\033c", end="")
		#print the basic roof and floor parts

		current_mode = self.get_board_mode()
		if current_mode == constants.WELCOME:
			self.initalise_board_matrix()
			matrix = self.get_matrix()
			offset = int(offset)
			height = int(constants.HEIGHT/2)
			
			word = [list("WELCOME")]
			for i in range(len(word)):	
				matrix[offset + 5][height] = word[i]

			self.set_board_matrix(matrix)
		elif current_mode == constants.LOAD :

			self.initalise_board_matrix()
			matrix = self.get_matrix()

			height = int(constants.HEIGHT/2)
			
			word = [list("LOADING")]
			for i in range(len(word)):	
				matrix[offset + 5][height] = word[i]

			self.set_board_matrix(matrix)
		elif current_mode == constants.END:
			print("									GAME LOOP HAS ENDED")
		elif current_mode == constants.NORMAL:
			# print all the objects as per the list of objects in the board ,
			self.initalise_board_matrix()
			matrix = self.get_matrix()
			matrix[int(constants.HEIGHT/2)][offset:offset + 21] = [list("GAME LOOP IS GOING ON")]
			self.set_board_matrix(matrix)


		self.print_floor_and_roof(offset)

	# these two funcitions are gonna be taking care of getting and setting the modes for the matrix that is the whole board


