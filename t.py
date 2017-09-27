import time
from Minmax import Board
width, height = 7, 6
board = [[0 for y in range(height)]for x in range (width)]

board[6][0] = 1
board[5][1] = 1
board[4][2] = 1
board[6][2] = 1

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
