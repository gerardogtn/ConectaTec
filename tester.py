import random
from main import MiniMax
from main import GameState
from Minmax import Board
from Minmax import MinMax

class ConsoleTester:

  def __init__(self, agent):
    self.agent = agent

  def run(self, board):
    print("Running")
    from judge import printGame
    v = int(input("Choose the column [0-6]: "))
    print("Selected: ", v)
    return v

class RandomTester:
    def __init__(self, agent):
        self.agent = agent

    def run(self, board):
        return random.randint(0,6)

#Optimized? version
class MinMaxTester:
    def __init__(self, agent):
        #agent, depth
        self.minmax = MinMax(agent, 5)
        self.agent = agent

    def run(self, board, turn):
        print("PC is thinking... ")
        b = Board(board)
        opt = self.minmax.minimax(self.agent, b)
        print("PC played: " + str(opt))
        return opt

class MiniMaxTester:

  def __init__(self, agent):
    self.minmax = MiniMax(agent)
    self.agent = agent

  def run(self, board):
    gameState = GameState(board)
    opt = self.minmax.maxValue(gameState, 1, self.agent, float("-inf"), float("inf"))
    print("PC played: " + str(opt))
    return opt
