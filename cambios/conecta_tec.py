import time

class Player:
  def __init__(self, id):
    self.id = id

  def play(self):
    pass

class TChecker:

  def __init__(self, id, board, width, height):
    self.board = board
    self.id = id
    self.WIDTH = width
    self.HEIGHT = height

  def check(self):
    for c in range(self.WIDTH):
      for r in range(self.HEIGHT):
        if self.checkHorizontal(c, r) or self.checkVertical(c, r) or \
          self.checkUpperDiagonal(c, r) or self.checkLowerDiagonal(c, r):
          return True

    return False

  def checkHorizontal(self, c, r):
    down = False
    up = False
    if (c > 1 and r > 0):
      down = self.board[c - 2][r] == self.id and self.board[c - 1][r] == self.id and self.board[c][r] == self.id \
        and self.board[c - 1][r - 1] == self.id

    if (c > 1 and r < self.HEIGHT - 1):
      up = self.board[c - 2][r] == self.id and self.board[c - 1][r] == self.id and self.board[c][r] == self.id \
        and self.board[c - 1][r + 1] == self.id
    return down or up

  def checkVertical(self, c, r):
    """
    x o o
    x x o
    t o o

    """
    left = False
    right = False

    if (c < self.WIDTH - 1 and r < self.HEIGHT - 2):
      left = self.board[c][r] == self.id and self.board[c][r + 1] == self.id and self.board[c][r + 2] == self.id \
        and self.board[c + 1][r + 1] == self.id

    if (c > 0 and r < self.HEIGHT - 2):
      right = self.board[c][r] == self.id and self.board[c][r + 1] == self.id and self.board[c][r + 2] == self.id \
        and self.board[c - 1][r + 1] == self.id

    return left or right

  def checkUpperDiagonal(self, c, r):
    """
    o o x
    o x o
    x o t
    """
    if (c > 1 and r < self.HEIGHT - 2):
      return self.board[c - 2][r] == self.id and self.board[c - 1][r + 1] == self.id and self.board[c][r + 2] == self.id \
        and (self.board[c][r] == self.id or self.board[c - 2][r + 2] == self.id)
    return False

  def checkLowerDiagonal(self, c, r):
    """
    x o t
    o x o
    o o x

    """
    if (c > 1 and r > 1):
      return self.board[c - 2][r] == self.id and self.board[c - 1][r - 1] == self.id and self.board[c][r - 2] == self.id \
        and (self.board[c][r] == self.id or self.board[c - 2][r - 2] == self.id)



class ConectaTecBoard:

  def __init__(self, width, height):
    self.WIDTH = width
    self.HEIGHT = height
    self.board = [[0 for y in range(height)]for x in range (width)]

  def place(self, column, id):
    """ Given the player and the column of the play, put a tile in the board """
    for i in range(self.HEIGHT):
      if self.board[column][i] == 0:
        self.board[column][i] = id
        break

  def canPlace(self, column):
    return self.board[column][-1] == 0

  def remove(self, column, player):
    for i in range(self.HEIGHT):
      if self.board[column][self.HEIGHT - i - 1] != 0:
        self.board[column][self.HEIGHT - i - 1] = 0
        break

  def printGame(self):
    print("\n")
    for r in range(self.HEIGHT):
      for c in range(self.WIDTH):
        print(self.mapChar(self.board[c][self.HEIGHT - r - 1]), end= " ")
      print("")
    for c in range(self.WIDTH):
      print("_", end=" ")
    print("")
    for c in range(self.WIDTH):
      print(str(c), end=" ")
    print("")

  def mapChar(self, inpt):
    if inpt == 0:
      return " "
    elif inpt == 1:
      return "X"
    elif inpt == 2:
      return "O"

  def toString(self):
      out = ""
      for r in range(self.HEIGHT):
        for c in range(self.WIDTH):
          out += str(self.board[c][self.HEIGHT - r - 1])
      return out

  def isGameOver(self):
    return self.won(1) or self.won(2) or self.isTie()

  def won(self, id):
    tchecker = TChecker(id, self.board, self.WIDTH, self.HEIGHT)
    return tchecker.check()

  def isTie(self):
    for col in self.board:
      for e in col:
        if e == 0:
          return False
    return True


class ConectaTec:

  def __init__(self, width, height):
    self.board = ConectaTecBoard(width, height)
    self.width = width
    self.height = height

  def getPlayerOne(self, id):
    return Player(id)

  def getPlayerTwo(self, id):
    return Player(id)

  def isGameOver(self):
    return self.board.isGameOver()

  def onGameOver(self):
    if (self.board.won(1)):
      print("Player ", 1, " won!!")
    elif (self.board.won(2)):
      print("Player ", 2, " won!!")
    else:
      print("Its a tie !!")

  def play(self):
    playerOne = self.getPlayerOne(1)
    playerTwo = self.getPlayerTwo(2)

    while True:
      from copy import deepcopy
      board = deepcopy(self.board.board)
      start = time.time()
      val = playerOne.play(board)
      end = time.time()
      print("Time taken: " + str(end - start) + "s")
      self.board.place(val, playerOne.id)
      if (self.isGameOver()):
        break
      self.board.printGame()

      board = deepcopy(self.board.board)
      start = time.time()
      val = playerTwo.play(board)
      end = time.time()
      print("Time taken: " + str(end - start) + "s")
      self.board.place(val, playerTwo.id)
      if (self.isGameOver()):
        break
      self.board.printGame()
    self.board.printGame()
    self.onGameOver()
