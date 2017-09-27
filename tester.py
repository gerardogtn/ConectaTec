import random
from main import MiniMax
from main import GameState

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

class MiniMaxTester:

  def __init__(self, agent):
    self.minmax = MiniMax(agent)
    self.agent = agent

  def run(self, board):
    gameState = GameState(board)
    opt = self.minmax.maxValue(gameState, 1, self.agent, float("-inf"), float("inf"))
    print("PC played: " + str(opt))
    return opt

if __name__ == '__main__':
    from judge import main
    main()
