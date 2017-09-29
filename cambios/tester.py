
class ConsoleTester:

  def __init__(self, agent):
    self.agent = agent

  def run(self, board):
    print("Running")
    from judge import printGame
    v = int(input("Choose the column [0-6]: "))
    print("Selected: ", v)
    return v
