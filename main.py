import copy
class GameState:
    def __init__(self, board):
        self.board = board

    def getLegalActions(self, agent):
        """ Return an iterable representing the legal actions to take. """
        actions = []
        for i in range(0, 7):
            if self.board[i][-1] == 0:
                actions.append(i)
        return actions

    def generateSuccessor(self, agent, action):
        """ Generates the successor for the given action
        Keyword arguments:
        action -- The column in which to add the disk.
        """
        rows = self.board[action]
        for i, row in enumerate(rows):
            if row == 0:
                self.board[action][i] = agent
                break
        return self

    def removeTopCoin(self, col):
        rows = self.board[col]
        for i in range(len(self.board[0]) - 1, -1, -1):
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
 
class MiniMax:
    def __init__(self, agent):
        self.agent = agent

    def maxValue(self, gameState, depth, agent, alpha, beta):
        if self.terminal(gameState, depth):
            ev = self.evaluate(gameState, depth)
            return ev

        maximum = float("-inf")
        nextAgent = self.getNextAgent(agent)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            value = self.minValue(successor, depth, nextAgent, alpha, beta)
            #gameState.deleteLast()
            gameState.removeTopCoin(action)

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
            return self.evaluate(gameState, depth)

        minimum = float("inf")
        nextAgent = self.getNextAgent(agent)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            minimum = min(minimum, self.maxValue(successor, depth + 1, nextAgent, alpha, beta))
            #gameState.deleteLast()
            gameState.removeTopCoin(action)

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

    def checkAnyT(self,board,player_number):
        width = len(board)
        height = len(board[0])
        for r in range(0,width):
            for c in range(0,height):
                if(board[r][c] == player_number):
                    if(checkWinBelow(board, width, height, c, r, player_number)
                    or checkWinAbove(board, width, height, c, r, player_number)
                    or checkLeft(board, width, height, c, r, player_number)
                    or checkRight(board, width, height, c, r, player_number)
                    or checkWinBottomRight(board, width, height, c, r, player_number)
                    or checkWinBottomLeft(board, width, height, c, r, player_number)
                    or checkWinTopLeft(board, width, height, c, r, player_number)
                    or checkWinTopRight(board, width, height, c, r, player_number)):
                        return True
        return False

    def evaluate(self, gameState, depth):
        """ Returns the 'score' for the given state """
        if self.checkAnyT(gameState.board,self.agent):
            #print(str(1000-depth))
            #gameState.mprint()
            return 1000-depth
        elif self.checkAnyT(gameState.board,self.getNextAgent(self.agent)):
            #if depth==1:
                #print(str(-100+depth))
                #gameState.mprint()
            return -100+depth
        else:
            return 0

    def terminal(self, gameState, depth):
        return depth > 3 or not gameState.getLegalActions(self.agent) or self.checkAnyT(gameState.board,1) or self.checkAnyT(gameState.board,2)


def checkWinBelow(board, width, height,col, row, player_number):
    if(col+1 == height or row == 0 or row+1 == width): return False
    if(board[row-1][col+1] == player_number and board[row][col+1] == player_number and board[row+1][col+1] == player_number): return True
    return False

def checkWinAbove(board, width, height,col, row, player_number):
    if(col == 0 or row == 0 or row+1 == width): return False
    if(board[row-1][col-1] == player_number and board[row][col-1] == player_number and board[row+1][col-1] == player_number): return True
    return False

def checkLeft(board, width, height,col, row, player_number):
    if(row + 1 >= width or col + 1 >= height or col - 1 < 0 ): return False
    if(board[row+1][col-1] == board[row+1][col] == board[row+1][col+1] == player_number): return True
    return False

def checkRight(board, width, height,col, row, player_number):
    if(row - 1 < 0 or col + 1 >= height or col - 1 < 0 ): return False
    if(board[row-1][col-1] == board[row-1][col] == board[row-1][col+1] == player_number): return True
    return False

def checkWinBottomRight(board, width, height,col, row, player_number):
    if(row - 2 < 0 or col + 2 >= height): return False
    if(board[row-2][col] == player_number and board[row-1][col+1] == player_number and board[row][col+2] == player_number): return True
    return False

def checkWinBottomLeft(board, width, height,col, row, player_number):
    if(row + 2 >= width or col - 2 < 0): return False
    if(board[row+2][col] == player_number and board[row+1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False

def checkWinTopLeft(board, width, height,col, row, player_number):
    if(row + 2 >= width or col - 2 < 0): return False
    if(board[row+2][col] == player_number and board[row+1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False

def checkWinTopRight(board, width, height,col, row, player_number):
    if(row - 2 < 0 or col - 2 < 0): return False
    if(board[row-2][col] == player_number and board[row-1][col-1] == player_number and board[row][col-2] == player_number): return True
    return False
