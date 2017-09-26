
class GameState:

    def __init__(self, board):
        self.board = board

    def getLegalActions(self, agent):
        """ Return an iterable representing the legal actions to take. """
        actions = []
        for indx in range(0, 6):
            if self.board[indx][0] == 0:
                actions.append(indx)
        return actions

    def generateSuccessor(self, agent, action):
        """ Generates the successor for the given action """
        successor = GameState(self.board[:])
        for i,pos in enumerate(self.board[action]):
            if pos != 0 or i == len(self.board[action]):
                successor.board[action][i-1] = agent
        return successor

class MiniMax:
    def __init__(self, agent):
        self.agent = agent

    def maxValue(self, gameState, depth, agent, alpha, beta):
        if self.terminal(gameState, depth):
            return self.evaluate(gameState)

        maximum = float("-inf")
        nextAgent = self.getNextAgent(agent)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            value = self.minValue(successor, depth, nextAgent, alpha, beta)

            if maximum < value:
                maximum = value
                maxAction = action

            if maximum > beta:
                return maximum

            alpha = max(alpha, maximum)

        if depth == 1:
            return maxAction
        else:
            return maximum


    def minValue(self, gameState, depth, agent, alpha, beta):
        if self.terminal(gameState,depth):
            return self.evaluate(gameState)

        minimum = float("inf")
        nextAgent = self.getNextAgent(agent)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            minimum = min(minimum, self.maxValue(successor, depth + 1, nextAgent, alpha, beta))

            if minimum < alpha:
                return minimum

            beta = min(beta, minimum)

        return minimum

    def getNextAgent(self, agent):
        """ Returns the agent representing the other player.

        ASSUMES: agent is either 1 or 2.
        """
        if agent == 1:
            return 2
        else:
            return 1


    def evaluate(self, gameState):
        """ Returns the 'score' for the given state """
        from judge import checkAnyT
        if checkAnyT(self.agent):
            return 10
        elif checkAnyT(self.getNextAgent(self.agent)):
            return -10
        else:
            return 0

    def terminal(self, gameState, depth):
        from judge import checkAnyT
        return depth > 4 or not gameState.getLegalActions(self.agent) or checkAnyT(1) or checkAnyT(2)
