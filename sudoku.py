import tkinter as tk
import random
import numpy as np
import math


class sudoku(tk.Frame):
	def __init__(self, master=None):

		# master window
		super().__init__(master)
		self.master = master

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

		# making field/block of sudoku
		self.sudokuGridBlock = []

		# the order of the blocks are followed
		# 0 1 2
		# 3 4 5
		# 6 7 8

		for row in range(3):
			startingRow = row * 3

			for column in range(3):
				startingColumn = column * 3

				self.sudokuGridSubBlock = []

				for advancingValue in range(3):
					for value in self.sudokuGrid[startingRow+advancingValue][startingColumn:startingColumn+3]:
						self.sudokuGridSubBlock.append( value )

				self.sudokuGridBlock.append(self.sudokuGridSubBlock)




		# widgets config
		self.buttonWidth = 2
		self.buttonHeight = int(self.buttonWidth / 2)

		# sequential
		self.pack()
		self.createManyButtons()


		#debug section		
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
		row, column, block = self.findPosition(0,0)
		print(self.checkAll(row, column, block))
		self.checkAll(row, column, block)
		#print(self.sudokuGridBlock[0])
		

	def shuffleSection(self, section):
		for value in section:
			#value = random.randint(1,9)
			pass

	def checkRow(self, row):
		if len(set(self.sudokuGrid[row])) < 9:
			return 0

		else: 
			return 1

	def checkColumn(self, column):
		selectedColumn = []

		for row in range(9):
			selectedColumn.append(self.sudokuGrid[row][column])

		if len(set(selectedColumn)) < 9:
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


	def findPosition(self, row, column):

		block = ( math.floor(row / 3) ) * 3 + math.floor(column / 3)

		return row, column, block

	def checkAll(self, row, column, block):

		checkedRow = self.checkRow(row)
		checkedColumn = self.checkColumn(column)
		checkedBlock = self.checkBlock(block)

		return checkedRow, checkedColumn, checkedBlock


		

	def createManyButtons(self):
		for row in range(9):
			for column in range(9):
				tk.Button(self, text=self.sudokuGrid[row][column], width=self.buttonWidth, height=self.buttonHeight).grid(row=row, column=column)



window = tk.Tk()
game = sudoku(master=window)
game.mainloop()