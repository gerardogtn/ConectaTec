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
      print(str(c+1), end=" ")
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


class GameState:
  def isTerminal(self):
    """ Returns True if the state is terminal, False otherwise """
    raise NotImplementedError("Class %s doesn't implement aMethod()" % (self.__class__.__name__))

  def getActionSuccessors(self, id):
    """ Return a list of the action taken and the successor for such action

    For instance, let's say that actions are defined as a number from [0,3] and
    a successor is a game state in the form of a list of 4 elements with values
    'x', 'o', or 'b'

    Self is: ['b', 'b', 'b', 'b', 'b']
    Returns:
      [
        (0, ['x', 'b', 'b', 'b']),
        (1, ['b', 'x', 'b', 'b']),
        (2, ['b', 'b', 'x', 'b']),
        (3, ['b', 'b', 'b', 'x'])
      ]

    Of course, any subclass would need to know if the successor is being filled with
    an 'x' or a 'o'. This should probably be stored in an instance variable and modified
    accordingly.

    Note that any class that calls this method will only care about the state but shouldn't
    be able to modify it. So state instances could be shared in order to optimize the algorithm
    if need be.
    """
    raise NotImplementedError("Class %s doesn't implement aMethod()" % (self.__class__.__name__))


class ConectaTecGameState(GameState):

  def __init__(self, width, height, board):
    self.board = ConectaTecBoard(width, height)
    self.board.board = board

  def isTerminal(self):
    return self.board.isGameOver()

  def getActionSuccessors(self, _id):
    for i in range(7):
      if self.board.canPlace(i):
        self.board.place(i, _id)
        yield (i, self)
        self.board.remove(i, _id)

class BoundedMiniMax:
  def __init__(self, depth, id, opponent):
    self.MAX_DEPTH = depth
    self.id = id
    self.opponent = opponent

  def successorsScores(self, state, currentDepth, isMinimizer):
    """ Returns the score of each state in states.

    The 'score' is the result of evaluate() in each state.
    """
    scores = []
    for _, next in state.getActionSuccessors(self.id if not isMinimizer else self.opponent):
        scores.append(self.minimax(next, currentDepth + 1, not isMinimizer))
        #boardStr = str(self.id) + str('1' if isMinimizer else '0') + next.board.toString()
        #BoundedMiniMax.hist[boardStr] = scores[-1]
    return scores

  def minimax(self, state, currentDepth, isMinimizer):
    """ Performs a bounded MiniMax Algorithm. """
    if state.isTerminal():
      return self.evaluate(state, currentDepth)
    elif currentDepth == self.MAX_DEPTH:
      return self.evaluate(state, currentDepth)
    elif isMinimizer:
      return min(self.successorsScores(state, currentDepth, isMinimizer))
    else:
      return max(self.successorsScores(state, currentDepth, isMinimizer))

  def run(self, originalState):
    """ Call this method to run minmax on the given state.

    Returns:
    The next action to be taken. (I.e. the next move to play.)
    """
    nextAction = None
    nextScore = float("-inf")
    for action, state in originalState.getActionSuccessors(self.id):
      # Since the opponent is the minimizer, and we are making one move already
      # minmax should be called assuming that is the opponents (minimizer) turn.
      score = self.minimax(state, 1, True)
      #print(score, end=" ")
      if (score > nextScore):
        nextScore = score
        nextAction = action
    #print("")
    return nextAction

  def evaluate(self, state, depth):
    pass

class ConectaTecMiniMax(BoundedMiniMax):
  hist = {}
  def __init__(self, MAX_DEPTH, id, opponent):
    BoundedMiniMax.__init__(self, MAX_DEPTH, id, opponent)
    self.id = id
    self.opponent = opponent

  def evaluate2(self, state, depth):
    boardStr = str(self.id) + state.board.toString()
    #print(boardStr)
    if boardStr in ConectaTecMiniMax.hist:
      #print("Recovered")
      return ConectaTecMiniMax.hist[boardStr]
    else:
      #print("Calculated")
      total = 0
      if (state.board.won(self.id)):
        total += 1000 - depth
      elif (state.board.won(self.opponent)):
        total += -1000 + depth
      else:
        total += self.score(board, depth, self.id, self.opponent)
      ConectaTecMiniMax.hist[boardStr] = total
      return total

  def evaluate(self, state, depth):
    boardStr = str(self.id) + state.board.toString()
    if boardStr in ConectaTecMiniMax.hist:
      #print("Recovered")
      return ConectaTecMiniMax.hist[boardStr]
    else:
      total = - self.countChecks(state.board) * 100
      if (state.board.won(self.id)):
        #total += 1000 - depth
        total += 10000 + self.score(state.board, depth, self.id, self.opponent)
      elif (state.board.won(self.opponent)):
        #total += -1000 + depth
        total += -10000 + self.countChecks(state.board)*200
      else:
        total += self.score(state.board, depth, self.id, self.opponent)
      ConectaTecMiniMax.hist[boardStr] = total
      return total

  def evaluate3(self, state, depth):
    total = - self.countChecks(state.board)*100
    if (state.board.won(self.id)):
      #total += 1000 - depth
      total += 10000 + self.score(board, depth, self.id, self.opponent)
    elif (state.board.won(self.opponent)):
      #total += -1000 + depth
      total += -10000 + self.countChecks(state.board)*200
    else:
      total += self.score(board, depth, self.id, self.opponent)
    return total

  def score(self, board, depth, agent, aa):
    #antiagent
    scoreS = 0
    scoreN = 0
    scoreE = 0
    scoreW = 0
    scoreNW = 0
    scoreNE = 0
    scoreSW = 0
    scoreSE = 0
    #check South
    for x in range(0, 5):
      for y in range (0,5):
        if (board.board[x][y] == aa or board.board[x+1][y] == aa or board.board[x+2][y] == aa or board.board[x+1][y+1] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x+1][y] == agent:
          t += 1
        if board.board[x+2][y] == agent:
          t += 1
        if board.board[x+1][y+1] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreS += t

    # check North (this is the T)
    for x in range(0,5):
      for y in range (1,6):
        if (board.board[x][y] == aa or board.board[x+1][y] == aa or board.board[x+2][y] == aa or board.board[x+1][y-1] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x+1][y] == agent:
          t += 1
        if board.board[x+2][y] == agent:
          t += 1
        if board.board[x+1][y-1] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreN += t

    # check West
    for x in range(0,6):
      for y in range (0,4):
        if (board.board[x][y] == aa or board.board[x][y+1] == aa or board.board[x][y+2] == aa or board.board[x+1][y+1] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x][y+1] == agent:
          t += 1
        if board.board[x][y+2] == agent:
          t += 1
        if board.board[x+1][y+1] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreW += t

    # check East
    for x in range(1,7):
      for y in range (0,4):
        if (board.board[x][y] == aa or board.board[x][y+1] == aa or board.board[x][y+2] == aa or board.board[x-1][y+1] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x][y+1] == agent:
          t += 1
        if board.board[x][y+2] == agent:
          t += 1
        if board.board[x-1][y+1] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreE += t

    # check NW
    for x in range(0,5):
      for y in range (0,4):
        if (board.board[x][y] == aa or board.board[x+1][y+1] == aa or board.board[x+2][y+2] == aa or board.board[x+2][y] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x+1][y+1] == agent:
          t += 1
        if board.board[x+2][y+2] == agent:
          t += 1
        if board.board[x+2][y] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreNW += t

    # check NE
    for x in range(0,5):
      for y in range (0,4):
        if (board.board[x][y] == aa or board.board[x][y+2] == aa or board.board[x+1][y+1] == aa or board.board[x+2][y] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x][y+2] == agent:
          t += 1
        if board.board[x+1][y+1] == agent:
          t += 1
        if board.board[x+2][y] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreNE += t

    # check SW
    for x in range(0,5):
      for y in range (2,6):
        if (board.board[x][y] == aa or board.board[x+1][y-1] == aa or board.board[x+2][y-2] == aa or board.board[x+2][y] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x+1][y-1] == agent:
          t += 1
        if board.board[x+2][y-2] == agent:
          t += 1
        if board.board[x+2][y] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreSW += t

    # check SE
    for x in range(0,5):
      for y in range (0,4):
        if (board.board[x][y] == aa or board.board[x+1][y+1] == aa or board.board[x+2][y+2] == aa or board.board[x][y+2] == aa):
          continue
        t = 0
        if board.board[x][y] == agent:
          t += 1
        if board.board[x+1][y+1] == agent:
          t += 1
        if board.board[x+2][y+2] == agent:
          t += 1
        if board.board[x][y+2] == agent:
          t += 1
        #t -= depth
        if t < 0:
          t = 0
        scoreSE += t

    score = scoreN + scoreS + scoreE + scoreW + scoreNW + scoreNE + scoreSW + scoreSE
    #self.printGame()
    #print("Score: " + str(score))
    return score

  def countChecks(self, board):
    count = 0;
    for x in range(0,7):
      for y in range (0,6):
        if board.board[x][y] != 0:
          count += 1
    return count


class Player:
  def __init__(self, id):
    self.id = id

  def play(self):
    pass

class MiniMaxPlayer(Player):
  def __init__(self, _id, width, height, depth):
    Player.__init__(self, _id)
    self.minimax = ConectaTecMiniMax(depth, _id, 2 if _id == 1 else 1)
    self.width = width
    self.height = height

  def play(self, board):
    state = ConectaTecGameState(self.width, self.height, board)
    return self.minimax.run(state)

firstRun = True
player = None

def play42(turn, board):
    global firstRun, player
    if firstRun:
        ConectaTecMiniMax.hist = eval(open('scores.txt', 'r').read())
        firstRun = False
        player = MiniMaxPlayer(turn, 7, 6, 5)
    return player.play(board)
