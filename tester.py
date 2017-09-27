
from main import MiniMax
from main import MiniMax2
from main import GameState
import copy

class ConsoleTester:

  def __init__(self, agent):
    self.agent = agent

  def run(self, board):
    print("Running")
    from judge import printGame
    v = int(input("Choose the column [0-6]: "))
    print("Selected: ", v)
    return v

class MiniMaxTester:

  def __init__(self, agent):
    self.minmax = MiniMax(agent)
    self.agent = agent

  def run(self, board):
    gameState = GameState(copy.deepcopy(board),[])
    opt = self.minmax.maxValue(gameState, 1, self.agent, float("-inf"), float("inf"))
    print(len(GameState.stack))
    return opt

class MiniMaxTester2:

  def __init__(self, agent):
    self.minmax = MiniMax2(agent)
    self.agent = agent

  def run(self, board):
    gameState = GameState(copy.deepcopy(board),[])
    opt = self.minmax.maxValue(gameState, 1, self.agent, float("-inf"), float("inf"))
    print(len(GameState.stack))
    return opt
