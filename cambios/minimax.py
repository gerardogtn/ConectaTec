from gamestate import GameState

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
      print(score, end=" ")
      if (score > nextScore):
        nextScore = score
        nextAction = action
    print("")
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
