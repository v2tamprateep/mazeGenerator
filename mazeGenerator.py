
import sys, getopt
import random
import math
import collections

# reverseAct = {"N": "S", "S": "N", "W": "E", "E": "W"}
actions = ['N', 'S', 'E', 'W']
maze = {}
WIDTH = 30
HEIGHT = 30

WALL = '*'
OPEN = 'O'

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
   #for j in range(HEIGHT-1, -1, -1):
    for j in range(0,HEIGHT):
      for i in range(0, WIDTH):
         print(maze[(i, j)], end=""),
      print("")

def printToFile():
    mazeFile = open('./test.txt', 'w')
    for j in range(HEIGHT-1, -1, -1):
        for i in range(0, WIDTH):
            mazeFile.write(maze[(i, j)])
        mazeFile.write("\n")
        

def main():
    global WIDTH
    global HEIGHT
    WIDTH = 30
    HEIGHT = 30
    try:
       opts, arg = getopt.getopt(sys.argv[1:], "hx:y:", ["help"])
    except getopt.GetoptError as err:
       sys.exit(2)
    
    for opt, arg in opts:
       if opt == "x":
           WIDTH = arg
       if opt == "y":
           HEIGHT = arg
    if (WIDTH is 0 or HEIGHT is 0): sys.exit()

    for i in range(0, WIDTH):
       for j in range(0, HEIGHT):
          maze[(i, j)] = WALL

    # start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
    
    start = (1, 1)
    maze[start] = OPEN
    stack = [start]
    position = stack[len(stack)-1]

    while (len(stack) is not 0):
        position = stack[len(stack)-1]
        maze[position] = OPEN
        legalActions = getLegalActions(position)       
        if (len(legalActions) is 0):
            stack.pop()
            continue
        action = random.choice(legalActions)
        position = nextPosition(position, action)
        stack.append(position)

    printMaze()   
    sys.exit()

if __name__ == "__main__":
    main()

