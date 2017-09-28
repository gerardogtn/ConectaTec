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

class ConectaTecMiniMax(BoundedMiniMax):

  def __init__(self, MAX_DEPTH, id, opponent):
    BoundedMiniMax.__init__(self, MAX_DEPTH, id, opponent)
    self.id = id
    self.opponent = opponent

  def evaluate(self, state, depth):
    if (state.board.won(self.id)):
      return 100 - depth
    elif (state.board.won(self.opponent)):
      return -100 + depth
    else:
      val = state.board.score(depth, self.id, self.opponent)
      return val
