import tkinter as tk
import random
import numpy as np
import math


class sudoku(tk.Frame):
	def __init__(self, master=None):

		# master window
		super().__init__(master)
		self.master = master

		# color
		self.highlightedColor = 'yellow'
		self.unHighlightedColor = 'white'

		# sudoku attributes
		#self.sudokuGrid = np.zeros( (9, 9) , dtype=np.int32 )
		self.sudokuGrid = [
		[1,2,3,4,5,6,7,8,9],
		[4,5,6,6,5,3,7,8,9],
		[7,8,9,4,5,6,7,8,9],
		[2,2,3,4,5,6,7,8,9],
		[3,2,3,1,5,6,7,8,9],
		[5,2,3,4,5,4,7,8,9],
		[8,2,3,4,5,6,7,8,9],
		[6,2,3,4,5,6,7,8,9],
		[9,2,3,4,5,6,4,8,9]
		]

		self.gridButtonIdentityList = []

		# making field/block of sudoku
		self.sudokuGridBlock = []

		# the order of the blocks are followed
		# 0 1 2
		# 3 4 5
		# 6 7 8

		for row in range(3):
			startingRow = row * 3

			for col in range(3):
				startingCol = col * 3

				self.sudokuGridSubBlock = []

				for advancingValue in range(3):
					for value in self.sudokuGrid[startingRow+advancingValue][startingCol:startingCol+3]:
						self.sudokuGridSubBlock.append( value )

				self.sudokuGridBlock.append(self.sudokuGridSubBlock)

		# input (keyboard)
		self.pressedKey = None

		# widgets config
		self.buttonWidth = 4
		self.buttonHeight = int(self.buttonWidth / 2)

		# sequential
		self.convertGridFromIntToStr()
		self.pack()
		self.createGrid()

		#debug
		#self.debugFunction()


	def debugFunction(self):
		self.convertGridFromIntToStr()
		print(self.sudokuGrid)
	
		#self.sudokuGrid[1][0] = 1
		#self.sudokuGrid[1][1] = 2
		#self.sudokuGrid[1][2] = 3
		#self.sudokuGrid[1][3] = 4
		#self.sudokuGrid[1][4] = 5
		#self.sudokuGrid[1][5] = 6
		#self.sudokuGrid[1][6] = 7
		#self.sudokuGrid[1][7] = 8
		#self.sudokuGrid[1][8] = 9

		#print(self.findPosition(3,0))

		#row, col, block = self.findPosition(0,0)
		#print(self.checkCombination(row, col, block))
		#self.checkCombination(row, col, block)
		#print(button2)
		#print(self.sudokuGridBlock[0])


	def convertGridFromIntToStr(self):
		for row in range(9):
			for col in range(9):
				self.sudokuGrid[row][col] = str(self.sudokuGrid[row][col])
		
	def shuffleSection(self, section):
		for value in section:
			#value = random.randint(1,9)
			pass

	def checkRow(self, row):
		if len(set(self.sudokuGrid[row])) < 9:
			return 0

		else: 
			return 1

	def checkCol(self, col):
		selectedCol = []

		for row in range(9):
			selectedCol.append(self.sudokuGrid[row][col])

		if len(set(selectedCol)) < 9:
			return 0

		else:
			return 1

	def checkBlock(self, block):

		#debug
		#print(len(set(self.sudokuGridBlock[block])))
		#print((set(self.sudokuGridBlock[block])))
		#end debug

		if len(set(self.sudokuGridBlock[block])) < 9:
			return 0

		else:
			return 1


	def findPosition(self, row, col):
		block = ( math.floor(row / 3) ) * 3 + math.floor(col / 3)
		return row, col, block

	def findButtonPosition(self, row, col):
		pos = ( row * 9 ) + col
		return pos

	def findButtonID(self, pos):
		return self.gridButtonIdentityList[pos]

	def findButtonIDCombination(self, row, col):
		return self.findButtonID(self.findButtonPosition(row, col))

	def checkCombination(self, row, col, block):
		checkedRow = self.checkRow(row)
		checkedCol = self.checkCol(col)
		checkedBlock = self.checkBlock(block)
		return checkedRow, checkedCol, checkedBlock

	def createGrid(self):
		for row in range(9):
			for col in range(9):
				# create a button variable for use
				selectedCoordinate = self.sudokuGrid[row][col]

				gridButtonIdentity = tk.Button(self, text=selectedCoordinate, command=lambda row=row, col=col : self.buttonPressedCommand(row, col), width=self.buttonWidth, height=self.buttonHeight, bg = self.unHighlightedColor)
				self.gridButtonIdentityList.append(gridButtonIdentity)

				#this creates a grid
				gridButtonIdentity.grid(row=row, column=col)

				#debug /// this is just example, you will get error  for an unrefered variable
				#gridButtonIdentity = tk.Button(self, text=selectedCoordinate, command=lambda row=row, col=col : self.buttonPressedCommandDebug(row, col), width=self.buttonWidth, height=self.buttonHeight, bg = self.unHighlightedColor)

	def changeSudokuGridNumber(self, event, row, col, buttonID):
		#define key
		key = event.char

		#clear what is written before
		self.sudokuGrid[row][col] = ''
		buttonID.config(text = '')

		if key not in '0123456789':
			pass

		else:
			self.sudokuGrid[row][col] = key
			buttonID.config(text = self.sudokuGrid[row][col], bg = self.unHighlightedColor)

			self.master.unbind('<Key>')

		#print(self.sudokuGrid)


	def buttonPressedCommand(self, row, col):
		buttonID = self.findButtonIDCombination(row, col)
		try:
			buttonID.config(bg = self.highlightedColor )
			self.master.bind('<Key>', lambda event : self.changeSudokuGridNumber( event , row, col , buttonID))

		except Exception as e:
			print(e)
			buttonID.config(bg = self.unHighlightedColor )




	def buttonPressedCommandDebug(self, row, col):
		buttonID = self.findButtonIDCombination(row, col)
		#buttonID.config(text=changedText)


window = tk.Tk()
game = sudoku(master=window)
game.mainloop()
#game.update()