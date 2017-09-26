class GameState:

    def __init__(self, board, width, height):
        self.board = board
        self.width = width
        self.height = height

    def getLegalActions(agent):
        """ Return an iterable representing the legal actions to take. """
        actions = []
        for indx in range(0, 6):
            if self.board[indx, 0] == 0
                actions.append(indx)
        return actions

    def generateSuccessor(agent, action):
        """ Generates the successor for the given action """
        # TODO
        pass

class MiniMax:
    def __init__(self, agent):
        self.agent = agent

    def maxValue(gameState, depth, agent, alpha, beta):
        if self.terminal(gameState, depth):
            return self.evaluate(gameState)

        maximum = float("-inf")
        nextAgent = self.getNextAgent(gameState, agent)

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


    def minValue(gameState, depth, agent, alpha, beta):
        if self.terminal(gameState,depth):
            return self.evaluate(gameState)

        minimum = float("inf")
        nextAgent = self.getNextAgent(agent)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            minimum = min(minimum,maxValue(successor, depth + 1, nextAgent, alpha, beta))

            if minimum < alpha:
                return minimum

            beta = min(beta, minimum)

        return minimum

    def getNextAgent(agent):
        """ Returns the agent representing the other player.

        ASSUMES: agent is either 1 or 2.
        """
        if agent == 1:
            return 2
        else:
            return 1


    def evaluate(gameState):
        """ Returns the 'score' for the given state """
        if checkAnyT(self.agent):
            return 10
        else if checkAnyT(self.getNextAgent(self.agent)):
            return -10
        else
            return 0

    def terminal(gameState, depth):
        return depth > 4 or not gameState.getLegalActions(agent) or checkAnyT(1) or checkAnyT(2)
