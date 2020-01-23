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
		print('\033[0;0H', end='')
		
		for i in matrix:
			for j in i[offset:(offset + int(constants.FRAME_WIDTH))]:
				print(j, end='')
			print('')




	def print_board(self, offset, list_of_objects, print_string):
		# self.clear_screen()
		print('\033[0;0H', end='')
		#print the basic roof and floor parts

		current_mode = self.get_board_mode()
		self.initalise_board_matrix()
		matrix = self.get_matrix()
		
		if current_mode == constants.WELCOME:

			offset = int(offset)
			height = int(constants.HEIGHT/2)
			word = list("WELCOME")
			for i in range(len(word)):	
				matrix[height][offset + 20 + i] = word[i]

		elif current_mode == constants.LOAD :
			
			height = int(constants.HEIGHT/2)
			word = list("LOADING")
			for i in range(len(word)):	
				matrix[height][offset + 20 + i] = word[i]

		elif current_mode == constants.END:

			l = list("GAME HAS ENDED    ")
			for i in range(len(l)):
				matrix[5][offset+10 + i] = l[i]

		elif current_mode == constants.NORMAL:
			l = list(print_string)
			for i in range(len(l)):
				matrix[5][offset+ 10 + i] = l[i]


			for obj in list_of_objects:
				try:
					x , y = obj.get_coordinates()
					height , width = obj.get_dimensions()
					object_matrix = obj.get_matrix()

					for i in range(x , x+width):
						for j in range(y , y + height):
							matrix[int(constants.HEIGHT) - int(constants.FLOOR) -j][offset + x + i] = object_matrix[j-y][i-x]
				except:
					# print("could not display object")
					pass

		
		self.set_board_matrix(matrix)
		self.print_floor_and_roof(offset)



