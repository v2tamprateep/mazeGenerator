
import sys, getopt
import random
import math
import collections

actions = ['N', 'S', 'E', 'W']
maze = {}
<<<<<<< HEAD
WIDTH = 0
HEIGHT = 0
WALL = '%'
OPEN = ' '
distribution = [1,1,55,55]

=======
WIDTH = 25
HEIGHT = 25

WALL = '%'
OPEN = ' '
>>>>>>> 27570132a4843e1c2c7c28242cbf1a36ad528731

def randElt(ls, distribution):
        
    n = len(ls)
    S = sum(distribution)
    r = random.uniform(0,S)
    for i in range(0,n):
        r -= distribution[i]
        if r <= 0: return ls[i]
        
    return ls[0]

def nextAction(legalActions):
    newDist = list([0,0,0,0])
    newDist[0] = 0
    for i in range(0,len(actions)):
        if actions[i] in legalActions:
            newDist[i] = distribution[i]
        else:
            newDist[i] = 0
    return randElt(actions,newDist)
         
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
<<<<<<< HEAD

    for j in range(0,HEIGHT):
      for i in range(0, WIDTH):
         print(maze[(i, j)], end=""),
      print("")

def printToFile():
    mazeFile = open('./test.txt', 'w')
=======
    for j in range(HEIGHT-1, -1, -1):
   # for j in range(0,HEIGHT):
        for i in range(0, WIDTH):
            print(maze[(i, j)]),
        print("")

def printToFile(ofile):
    mazeFile = open('./'+ofile, 'w')
>>>>>>> 27570132a4843e1c2c7c28242cbf1a36ad528731
    for j in range(HEIGHT-1, -1, -1):
        for i in range(0, WIDTH):
            mazeFile.write(maze[(i, j)])
        mazeFile.write("\n")
        

def main():
    global WIDTH
    global HEIGHT
<<<<<<< HEAD
    WIDTH = 40
    HEIGHT = 40
=======
    WIDTH = 30
    HEIGHT = 30
    output = "default.txt"
>>>>>>> 27570132a4843e1c2c7c28242cbf1a36ad528731
    try:
       opts, args = getopt.getopt(sys.argv[1:], "hx:y:", ["help", "output="])
    except getopt.GetoptError as err:
       sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-x", "--width"):
            WIDTH = int(arg)
        if opt in ("-y", "--height"):
            HEIGHT = int(arg)
        if opt == "--output":
            output = str(arg)

    if (WIDTH is 0 or HEIGHT is 0):
        print("Invalid Dimensions")
        sys.exit()

    for i in range(0, WIDTH):
       for j in range(0, HEIGHT):
          maze[(i, j)] = WALL

    # start = (round(random.uniform(1, x)), round(random.uniform(1, y)))
    
    start = (1, 1)
    maze[start] = OPEN
    terminal = []
    stack = [start]
    position = start

    print("Width: " + str(WIDTH) + ", Height: " + str(HEIGHT) + ", Output file: " + output)
    while (len(stack) is not 0):
        position = stack[-1]
        maze[position] = OPEN
        legalActions = getLegalActions(position)       
        if (len(legalActions) is 0):
            terminal.append(position)
            stack.pop()
            continue
 #       action = random.choice(legalActions)
        action = nextAction(legalActions)
        #print(action)
        position = nextPosition(position, action)
        stack.append(position)

<<<<<<< HEAD
    printMaze()
    
=======
    maze[start] = "S"
    maze[random.choice(terminal)] = "T"
    printMaze()
    printToFile(output)
>>>>>>> 27570132a4843e1c2c7c28242cbf1a36ad528731
    sys.exit()

if __name__ == "__main__":
    main()
