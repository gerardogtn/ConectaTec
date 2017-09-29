from gamestate import GameState

class BoundedMiniMax:
  def __init__(self, depth, id, opponent):
    self.MAX_DEPTH = depth
    self.id = id
    self.opponent = opponent

  def successorsScores22(self, state, currentDepth, isMinimizer):
    """ Returns the score of each state in states.

    The 'score' is the result of evaluate() in each state.
    """
    scores = []
    for _, next in state.getActionSuccessors(self.id if not isMinimizer else self.opponent):
      boardStr = str(self.id) + str('1' if isMinimizer else '0') + next.board.toString()
      if boardStr in BoundedMiniMax.hist:
        scores.append(BoundedMiniMax.hist[boardStr])
      else:
        val = self.minimax(next, currentDepth + 1, not isMinimizer)
        #BoundedMiniMax.hist[boardStr] = val
        scores.append(val)
    return scores

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
        total += state.board.score(depth, self.id, self.opponent)
      ConectaTecMiniMax.hist[boardStr] = total
      return total

  def evaluate(self, state, depth):
    boardStr = str(self.id) + state.board.toString()
    if boardStr in ConectaTecMiniMax.hist:
      #print("Recovered")
      return ConectaTecMiniMax.hist[boardStr]
    else:
      total = - state.board.countChecks()*100
      if (state.board.won(self.id)):
        #total += 1000 - depth
        total += 10000 + state.board.score(depth, self.id, self.opponent)
      elif (state.board.won(self.opponent)):
        #total += -1000 + depth
        total += -10000 + state.board.countChecks()*200
      else:
        total += state.board.score(depth, self.id, self.opponent)
      ConectaTecMiniMax.hist[boardStr] = total
      return total

  def evaluate3(self, state, depth):
    total = - state.board.countChecks()*100
    if (state.board.won(self.id)):
      #total += 1000 - depth
      total += 10000 + state.board.score(depth, self.id, self.opponent)
    elif (state.board.won(self.opponent)):
      #total += -1000 + depth
      total += -10000 + state.board.countChecks()*200
    else:
      total += state.board.score(depth, self.id, self.opponent)
    return total
