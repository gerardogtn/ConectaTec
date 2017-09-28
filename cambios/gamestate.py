
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
    from conecta_tec import ConectaTecBoard
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









