
import sys, getopt
import random
import math

reverseAct = {"N": "S", "S": "N", "W": "E", "E": "W"}
actions = ['N', 'S', 'E', 'W']

maze = {}
# fill maze with walls ('%')
for i in range(0, x):
	for j in range(0, y):
		maze[(i, j)] = '%'

def nextPosition(position, direction):
	if (direction is 'N'): return (position[0], position[1] + 1)
	if (direction is 'E'): return (position[0] + 1, position[1])
	if (direction is 'W'): return (position[0] - 1, position[1])
	if (direction is 'S'): return (position[0], position[1] - 1)

def isLegal(position, maze):
	x = position[0]
	y = position[1]

	if  (maze[(x+1, y-1)] is ' '): return False
	if  (maze[(x+1, y+1)] is ' '): return False
	if  (maze[(x-1, y-1)] is ' '): return False
	if  (maze[(x-1, y+1)] is ' '): return False

	return True

def getLegalActions(position):
	legalMoves = []
	for act in actions:
		nextPos = nextPosition(position, act)
		if isLegal(nextPos): legalMoves.append(act)
	return legalMoves

def backtrack():
	position = stack[len(maze)-1]
	while (len(getLegalActions(position)) is not 0 or len(stack) is 0):
		stack.pop()
		position = stack[len(stack)-1]	

def main():
	try:
		opts, arg = getopt.getopt(sys.arg[1:], "hx:y:", ["help"])
	except getopt.GetoptError as err:
		sys.exit(2)

	x = 0
	y = 0
	for opt, arg in opts:
		if opt == "x":
			x = arg
		if opt == "y":
			y = arg

	start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
	maze[start] = ' '
	stack = [start]

	while (len(stack) is 0):
		position = stack[len(stack)-1]

		legalActions = getLegalActions(position)
		if (len(legalActions) is 0):
			backtrack()
			continue

		action = random.choice(legalActions)
		position = nextPosition(position, action)
		maze[position] = ' '
		stack.append(position)

	print("end")
	sys.exit()

if __name__ == "__main__":
	main()

