
import sys, getopt
import random
import math
import collections

# reverseAct = {"N": "S", "S": "N", "W": "E", "E": "W"}
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

def getLegalActions(position):
	legalMoves = []
	for act in actions:
		nextPos = nextPosition(position, act)

		if (nextPos[0] < 1 or nextPos[0] >= x - 1): continue
		if (nextPos[1] < 1 or nextPos[1] >= y - 1): continue
	
		if (isLegal(nextPos, act)): legalMoves.append(act)
	return legalMoves

def backtrack(stack):
	position = stack[len(stack)-1]
	while (len(getLegalActions(position)) is not 0 or len(stack) is 0):
		stack.pop()
		position = stack[len(stack)-1]	

def main():
	try:
		opts, arg = getopt.getopt(sys.argv[1:], "hx:y:", ["help"])
	except getopt.GetoptError as err:
		sys.exit(2)

	x = 10
	y = 10
	for opt, arg in opts:
		if opt == "x":
			x = arg
		if opt == "y":
			y = arg
	if (x is 0 or y is 0): sys.exit()

	for i in range(0, x):
		for j in range(0, y):
			maze[(i, j)] = '%'

	# start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
	start = (1, 1)
	maze[start] = ' '
	stack = [start]
	while (len(stack) is not 0):
		position = stack[len(stack)-1]

		legalActions = getLegalActions(position)
		if (len(legalActions) is 0):
			backtrack(stack)
			continue

		action = random.choice(legalActions)
		position = nextPosition(position, action)
		maze[position] = ' '
		stack.append(position)
	"""
	mazeFile = open('./test.txt', 'w')
	for j in range(y-1, -1, -1):
		for i in range(0, x):
			mazeFile.write(maze[(i, j)])
		mazeFile.write("\n")
	"""

	for j in range(y-1, -1, -1):
		for i in range(0, x):
			print(maze[(i, j)]),
		print("")

	print("end")
	sys.exit()

if __name__ == "__main__":
	main()

