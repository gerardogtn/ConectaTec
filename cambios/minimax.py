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
      if (score > nextScore):
        nextScore = score
        nextAction = action
    return nextAction

  def evaluate(self, state, depth):
    pass

class AlphaBetaMiniMax(BoundedMiniMax):
  def __init__(self, depth, _id, opponent):
    BoundedMiniMax.__init__(self, depth, _id, opponent)
    self.c = 1

  def successorsScores(self, state, currentDepth, isMinimizer, alpha, beta):
    """ Returns the score of each state in states.

    The 'score' is the result of evaluate() in each state.
    """
    raise NotImplementedError()

  def minimax(self, state, currentDepth, isMinimizer, alpha, beta):
    if state.isTerminal():
      score = self.evaluate(state, currentDepth)
      return (score, alpha, beta)
    elif currentDepth == self.MAX_DEPTH:
      score = self.evaluate(state, currentDepth)
      return (score, alpha, beta)

    v = float("-inf") if not isMinimizer else float("inf")
    s = False
    for action, next in state.getActionSuccessors(self.id if not isMinimizer else self.opponent):
      if not s: 
        score = self.minimax(next, currentDepth + 1, not isMinimizer, alpha, beta)[0]
        if not isMinimizer:
          v = max(v, score)
          alpha = max(v, alpha)
          if beta <= alpha:
            s = True
    
        else: 
          v = min(v, score)
          beta = min(beta, v)
          if beta <= alpha:
            s = True
    return (v, alpha, beta)

  def run(self, originalState):
    nextAction = None
    v = float("-inf")
    # print("Turn: ", self.id)

    nextAction = None
    alpha = float("-inf")
    beta = float("inf")
    s = False
    for action, state in originalState.getActionSuccessors(self.id):
      # Since the opponent is the minimizer, and we are making one move already
      # minmax should be called assuming that is the opponents (minimizer) turn.
      if not s: 
        score, alpha2, beta2 = self.minimax(state, 1, True, alpha, beta)
        if score > v:
          v = score
          nextAction = action
        v = max(v, score)
        alpha = max(v, alpha2)
    self.c += 2

    print("NEXT ACTION: ", nextAction)
    return nextAction

class ConectaTecMiniMax(AlphaBetaMiniMax):

  def __init__(self, MAX_DEPTH, id, opponent):
    AlphaBetaMiniMax.__init__(self, MAX_DEPTH, id, opponent)
    self.id = id
    self.opponent = opponent

  def evaluate(self, state, depth):
    total = 0
    if (state.board.won(self.id)):
      total += 1000 - depth
      return total
    elif (state.board.won(self.opponent)):
      total += -1000 + depth
      return total
    total += state.board.score(depth, self.id, self.opponent)

    return total
