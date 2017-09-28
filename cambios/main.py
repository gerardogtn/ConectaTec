from minimax import *
from gamestate import *
from conecta_tec import *

class MiniMaxPlayer(Player):
  def __init__(self, _id, width, height):
    Player.__init__(self, _id)
    DEPTH = 5
    self.minimax = ConectaTecMiniMax(DEPTH, _id, 2 if _id == 1 else 1)
    self.width = width
    self.height = height

  def play(self, board):
    state = ConectaTecGameState(self.width, self.height, board)
    return self.minimax.run(state)

class ConsolePlayer(Player):
  def __init__(self, id):
    Player.__init__(self, id)

  def play(self, board):
    v = int(input("Select the column [1-7]: "))
    return v - 1

class MiConectaTec(ConectaTec):
  def __init__(self, width, height):
    ConectaTec.__init__(self, width, height)

  def getPlayerOne(self, id):
    #return MiniMaxPlayer(id, self.width, self.height)
    return ConsolePlayer(id)

  def getPlayerTwo(self, id):
    return MiniMaxPlayer(id, self.width, self.height)
    #return ConsolePlayer(id)

def main():
  WIDTH = 7
  HEIGHT = 6

  conectaTec = MiConectaTec(WIDTH, HEIGHT)
  conectaTec.play()

if __name__ == '__main__':
  main()
