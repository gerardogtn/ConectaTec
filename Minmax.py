import math

class Board:
    def __init__(self, board):
        self.board = board

    def getLegalActions(self, agent):
        # Return an iterable representing the legal actions to take.
        actions = []
        for i in range(0, 7):
            if self.board[i][-1] == 0:
                actions.append(i)
        return actions

    def insertCoin(self, col, agent):
        # Hardcoded height here
        for num in range(0,7):
            if self.board[col][num] == 0:
                self.board[col][num] = agent
                return
    def removeCoin(self, col):
        # Harcoded height here
        for i in range(6, -1, -1):
            if self.board[col][i] != 0:
                self.board[col][i] = 0
                return

    def mprint(self):
        height = len(self.board[0])
        width = len(self.board)
        for x in range(height - 1, -1, -1):
            for y in range(width):
                if self.board[y][x] == 0:
                    print("", end="  ")
                else:
                    print (self.board[y][x], end=" ")
            print ("")
        print ("")

    def checkWin(self, agent):
        #ranges height = 0,6
        #ranges wifth = 0,
        # check South & North
        for x in range(0, 5):
            for y in range (0,5):
                if (self.board[x][y] == agent and self.board[x+1][y] == agent and self.board[x+2][y] == agent and self.board[x+1][y+1] == agent):
                    return True
        # check North (this is the T)
        for x in range(0,5):
            for y in range (1,6):
                if (self.board[x][y] == agent and self.board[x+1][y] == agent and self.board[x+2][y] == agent and self.board[x+1][y-1] == agent):
                    return True
        # check West
        for x in range(0,6):
            for y in range (0,4):
                if (self.board[x][y] == agent and self.board[x][y+1] == agent and self.board[x][y+2] == agent and self.board[x+1][y+1] == agent):
                    return True
        # check East
        for x in range(1,7):
            for y in range (0,4):
                if (self.board[x][y] == agent and self.board[x][y+1] == agent and self.board[x][y+2] == agent and self.board[x-1][y+1] == agent):
                    return True
        # check NW
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == agent and self.board[x+1][y+1] == agent and self.board[x+2][y+2] == agent and self.board[x+2][y] == agent):
                    return True
        # check NE
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == agent and self.board[x][y+2] == agent and self.board[x+1][y+1] == agent and self.board[x+2][y] == agent):
                    return True
        # check SW
        for x in range(0,5):
            for y in range (2,6):
                if (self.board[x][y] == agent and self.board[x+1][y-1] == agent and self.board[x+2][y-2] == agent and self.board[x+2][y] == agent):
                    return True
        # check SE
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == agent and self.board[x+1][y+1] == agent and self.board[x+2][y+2] == agent and self.board[x][y+2] == agent):
                    return True
        return False

class MinMax:
    def __init__(self, agent):
        self.agent = agent

    def getNextAgent(self, agent):
        # Returns opposite agent
        if agent == 1:
            return 2
        else:
            return 1

    def evaluate(self, board, depth):
        return 0

    def minimax(self, agent, depthMax, board):
        self.depthMax = depthMax
        opt = maxValue(board, 1, agent, -math.inf, math.inf)

    def maxValue(self, board, depth, agent, alpha, beta):
        if depth > self.depthMax: return self.evaluate(board, depth)
        actions = board.getLegalActions()
        if len(actions) == 0: return board.evaluate(board, depth)
        maximum = -math.inf
        nextAgent = self.getNextAgent(agent)
        for action in actions:
            board.insertCoin(action, agent)
            value = self.minValue(board, depth, nextAgent, alpha, beta)
            board.removeCoin(action)
            if maximum < value:
                maximum = value
                maxAction = action
            if maximum > beta:
                return maximum

            if alpha < maximum:
                alpha = maximum
            #alpha = max(alpha, maximum)

        if depth == 1:
            return maxAction
        else:
            return maximum

    def minValue(self, board, depth, agent, alpha, beta):
        if depth > self.depthMax: return self.evaluate(board, depth)
        actions = board.getLegalActions()
        if len(actions) == 0: return board.evaluate(board, depth)
        minimum = math.inf
        nextAgent = self.getNextAgent(agent)
        for action in actions:
            board.insertCoin(action, agent)
            value = self.maxValue(board, depth, nextAgent, alpha, beta)
            board.removeCoin(action)
            if minimum > value:
                minimum = value

            if minimum < alpha:
                return minimum

            #beta = min(beta, minimum)
            if beta > minimum:
                beta = minimum

        return minimum
