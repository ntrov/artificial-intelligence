import numpy as np


class treeNode:
	def __init__(self, state):
		self.up = None
		self.down = None
		self.left = None
		self.right = None
		self.state = state


class fifteenPuzzle:
	def __init__(self, initState):
		self.goal = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], dtype=np.int16)
		self.root = treeNode(initState)

	def checkPolarity(self, row):
		'''checks the polarity of the row in which blank is present \n
		returns False if odd\n
		returns True if even'''
		if row % 2 == 0:
			return True
		else:
			return False

	def swap(self, state, pos, direction):
		'''moves the blank in the direction specified'''

		a, b = pos
		# print(state)
		if direction == 'up':
			state[a][b], state[a-1][b] = state[a-1][b], state[a][b]
		elif direction == 'down':
			state[a][b], state[a+1][b] = state[a+1][b], state[a][b]
		elif direction == 'right':
			state[a][b], state[a][b+1] = state[a][b+1], state[a][b]
		elif direction == 'left':
			state[a][b], state[a][b-1] = state[a][b-1], state[a][b]

		return state

	def inversions(self, state):
		'''returns the total number of inversions in a state.'''

		lst = state.reshape(-1)
		inversions = 0
		for i in range(len(lst)):
			for j in range(i+1, len(lst)):
				if lst[i] == 0 or lst[j] == 0:  # ignore the blank
					continue

				if lst[i] > lst[j]:
					inversions += 1

		return(inversions)

	def solvePuzzle(self, current = root):
		'''solves the puzzle'''
		
		if current.state == goal:
			print("Goal Reached!")
			print(current.state)
		
		#check Solvebility
		temp = np.where(current.state == 0)
		blankPos = list(zip(temp[0], temp[1]))[0]  # position of the blank
		if self.checkPolarity(blankPos[0]):
			if self.checkPolarity(self.inversions(current.state)) == False:
				print('unreachable message')
				return
		else:
			if self.checkPolarity(self.inversions(current.state)) == False:
				print('unreachable message')
				return

		if blankPos[0]==0 and blankPos[1]==0:
			current.right = swap(current.state, blankPos, 'right')
			current.down = swap(current.state, blankPos, 'down')
		elif blankPos[0]==3 and blankPos[1]==3:
			current.left = swap(current.state, blankPos, 'left')
			current.up = swap(current.state, blankPos, 'up')
		elif blankPos[0]==3 and blankPos[1]==0:
			current.up = swap(current.state, blankPos, 'up')
			current.rihgt = swap(current.state, blankPos, 'right')
		elif blankPos[0]==0 and blankPos[1]==3:
			current.left = swap(current.state, blankPos, 'left')
			current.down = swap(current.state, blankPos, 'down')
		elif blankPos[0]==0:
			current.right = swap(current.state, blankPos, 'right')
			current.down = swap(current.state, blankPos, 'down')
			current.left = swap(current.state, blankPos, 'left')
		elif blankPos[0]==3:
			current.right = swap(current.state, blankPos, 'right')
			current.up = swap(current.state, blankPos, 'up')
			current.left = swap(current.state, blankPos, 'left')
		elif blankPos[1]==0:
			current.right = swap(current.state, blankPos, 'right')
			current.down = swap(current.state, blankPos, 'down')
			current.up = swap(current.state, blankPos, 'up')
		elif blankPos[1]==3:
			current.up = swap(current.state, blankPos, 'up')
			current.down = swap(current.state, blankPos, 'down')
			current.left = swap(current.state, blankPos, 'left')
		else:
			current.right = swap(current.state, blankPos, 'right')
			current.down = swap(current.state, blankPos, 'down')
			current.left = swap(current.state, blankPos, 'left')
			current.up = swap(current.state, blankPos, 'up')

if __name__ == "__main__":
	agent = fifteenPuzzle()
	lst = []
	for i in range(4):
		lowerLst = []
		for j in range(4):
			temp = int(input("Enter the number for a box:"))
			lowerLst.append(temp)

		lst.append(lowerLst)
	myArray = np.array(lst, dtype=np.int16)

	agent.solvePuzzle(myArray)
