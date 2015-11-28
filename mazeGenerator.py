
import sys, getopt
import random
import math
import collections

actions = ['N', 'S', 'E', 'W']
maze = {}
x = 0
y = 0

def nextPosition(position, direction):
	if (direction is 'N'): return (position[0], position[1] + 1)
	if (direction is 'E'): return (position[0] + 1, position[1])
	if (direction is 'W'): return (position[0] - 1, position[1])
	if (direction is 'S'): return (position[0], position[1] - 1)

def isLegal(position, action):
	x = position[0]
	y = position[1]

	if (action is not 'W'):
		# if East is path
		if  (maze[(x+1, y)] is not '%'): return False

	if (action is not 'E'):
		# if West is path
		if  (maze[(x-1, y)] is not '%'): return False

	if (action is not 'N'):
		# if South is path
		if  (maze[(x, y-1)] is not '%'): return False

	if (action is not 'S'):
		# if North is path
		if  (maze[(x, y+1)] is not '%'): return False

	return True

def getLegalActions(position, stack, terminal):
	legalMoves = []
	for act in actions:
		nextPos = nextPosition(position, act)
		if (nextPos in terminal): continue
		if (nextPos in stack): continue
		if (nextPos[0] < 1 or nextPos[0] >= x - 1): continue
		if (nextPos[1] < 1 or nextPos[1] >= y - 1): continue

		if (isLegal(nextPos, act)): legalMoves.append(act)
	return legalMoves

def backtrack(stack, terminal):
	position = stack[-1]
	while (len(getLegalActions(position, stack, terminal)) is 0 or len(stack) is 0):
		stack.pop()
		if (len(stack) is 0):
			break
		position = stack[-1]

def main():
	global maze
	global x
	global y

	try:
		opts, arg = getopt.getopt(sys.argv[1:], "hx:y:", ["help", "output=", "x=", "y="])
	except getopt.GetoptError as err:
		sys.exit(2)

	output = "defaultMazeOutput.txt"

	for opt, arg in opts:
		if opt in ("-x", "--x"):
			x = int(arg)
		if opt in ("-y", "--y"):
			y = int(arg)
		if opt == "--output":
			output = arg
	if (x <= 0 or y <= 0):
		print("Invalid Dimensions")
		sys.exit()

	for i in range(0, x):
		for j in range(0, y):
			maze[(i, j)] = '%'

	terminal = []
	# start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
	start = (1, 1)
	maze[start] = 'S'
	stack = [start]
	while (len(stack) is not 0):
		position = stack[-1]
		legalActions = getLegalActions(position, stack, terminal)

		if (len(legalActions) is 0):
			terminal.append(position)
			backtrack(stack, terminal)
		else:
			action = random.choice(legalActions)
			position = nextPosition(position, action)
			maze[position] = ' '
			stack.append(position)

	maze[random.choice(terminal)] = 'T'
	#"""
	mazeFile = open("./" + output, 'w')
	for j in range(y-1, -1, -1):
		for i in range(0, x):
			mazeFile.write(maze[(i, j)])
		mazeFile.write("\n")
	#"""
	#"""
	for j in range(y-1, -1, -1):
		for i in range(0, x):
			print(maze[(i, j)]),
		print("")
	#"""
	print("Complete")
	sys.exit()

if __name__ == "__main__":
	main()

