import time
from Minmax import Board
from Minmax import MinMax
width, height = 7, 6
board = [[0 for y in range(height)]for x in range (width)]

board[2][0] = 1
board[3][0] = 1
board[4][0] = 1
board[3][1] = 1

def printGame():
    global board, width, height
    for x in range(height - 1, -1, -1):
        for y in range(width):
            print (mapChar(board[y][x]), end=" ")
        print ("")
    for x in range(width):
        print("-", end=" ")
    print ("")

def mapChar(inpt):
    if inpt == 0:
        return " "
    elif inpt == 1:
        return "X"
    elif inpt == 2:
        return "O"

b = Board(board)
start = time.time()
b.mprint()
end = time.time()
print(b.checkWin(1))
print("Time: " + str((end - start)*1000) + "ms")
