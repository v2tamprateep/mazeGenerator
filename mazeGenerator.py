
import sys, getopt
import random
import math
import collections

actions = ['N', 'S', 'E', 'W']
maze = {}
WIDTH = 25
HEIGHT = 25

WALL = '%'
OPEN = ' '

def nextPosition(position, direction):
    if (direction is 'N'): return (position[0], position[1] + 1)
    if (direction is 'E'): return (position[0] + 1, position[1])
    if (direction is 'W'): return (position[0] - 1, position[1])
    if (direction is 'S'): return (position[0], position[1] - 1)

def onBoundary(position): #FIX
    if position[0] is 0: return True
    if position[1] is 0: return True
    if position[0] is WIDTH-1: return True
    if position[1] is HEIGHT-1: return True
    return False

#does the square have at most one open neighbor?
def removable(position):
        
    numOpen = 0
    for bearing in actions:
        square = nextPosition(position, bearing)
        if(maze[square] is OPEN):
            numOpen += 1;

    return not(numOpen > 1)
        
def isLegal(nextSquare):

    if onBoundary(nextSquare): return False
    if(maze[nextSquare] is OPEN): return False
    if not removable(nextSquare): return False
    
    return True

def getLegalActions(position):
    legalMoves = []
    for act in actions:       
        nextPos = nextPosition(position, act)
        if (nextPos[0] < 1 or nextPos[0] >= WIDTH - 1): continue
        if (nextPos[1] < 1 or nextPos[1] >= HEIGHT - 1): continue
        nextSquare = nextPosition(position, act)
        if (isLegal(nextSquare)): legalMoves.append(act)       
    return legalMoves

def printMaze():
    for j in range(HEIGHT-1, -1, -1):
   # for j in range(0,HEIGHT):
        for i in range(0, WIDTH):
            print(maze[(i, j)]),
        print("")

def printToFile(ofile):
    mazeFile = open('./'+ofile, 'w')
    for j in range(HEIGHT-1, -1, -1):
        for i in range(0, WIDTH):
            mazeFile.write(maze[(i, j)])
        mazeFile.write("\n")
        

def main():
    global WIDTH
    global HEIGHT
    WIDTH = 30
    HEIGHT = 30
    output = "default.txt"
    try:
       opts, arg = getopt.getopt(sys.argv[1:], "hx:y:", ["help", "output"])
    except getopt.GetoptError as err:
       sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-x", "--width="):
            WIDTH = str(arg)
        if opt in ("-y", "--height="):
            HEIGHT = str(arg)
        if opt is "--output=":
            output = arg
    if (WIDTH is 0 or HEIGHT is 0):
        print("Invalid Dimensions")
        sys.exit()

    for i in range(0, WIDTH):
       for j in range(0, HEIGHT):
          maze[(i, j)] = WALL

    # start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
    
    start = (1, 1)
    maze[start] = OPEN
    stack = [start]
    position = start

    print("Width: " + str(WIDTH) + ", Height: " + str(HEIGHT) + ", Output file: " + output)
    while (len(stack) is not 0):
        position = stack[-1]
        maze[position] = OPEN
        legalActions = getLegalActions(position)       
        if (len(legalActions) is 0):
            stack.pop()
            continue
        action = random.choice(legalActions)
        position = nextPosition(position, action)
        stack.append(position)

    printMaze()
    printToFile(output)
    sys.exit()

if __name__ == "__main__":
    main()
