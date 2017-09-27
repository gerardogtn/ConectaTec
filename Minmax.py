import math
import time
import random

class Board:
    def __init__(self, board):
        self.board = board

    def getLegalActions(self):
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
        for i in range(5, -1, -1):
            if self.board[col][i] != 0:
                self.board[col][i] = 0
                return

    def mprint(self):
        for x in range(5, -1, -1):
            for y in range(0,7):
                print (self.mapChar(self.board[y][x]), end=" ")
            print ("")
        for x in range(0,7):
            print("-", end=" ")
        print ("")

    def mapChar(self, inpt):
        if inpt == 0:
            return " "
        elif inpt == 1:
            return "X"
        elif inpt == 2:
            return "O"
    evaluations = 0
    def evaluate(self, agent, depth):
        #start = time.time()
        val = self.evaluate2(agent, depth)
        #end = time.time()
        #print("Time: " + str((end - start)*1000) + "ms")
        #Board.evaluations += 1
        #print(Board.evaluations)
        return val

    def evaluate2(self, agent, depth):
        """ Returns the 'score' for the given state """
        if self.checkWin(agent):
            return 100 - depth
        elif self.checkWin(self.getNextAgent(agent)):
            return depth - 100
        else:
            return 0
    def getNextAgent(self, agent):
        # Returns opposite agent
        if agent == 1:
            return 2
        else:
            return 1

    def score(self, agent, depth, player):
        #antiagent
        aa = self.getNextAgent(agent)
        depth -= 1
        scoreS = 0
        scoreN = 0
        scoreE = 0
        scoreW = 0
        scoreNW = 0
        scoreNE = 0
        scoreSW = 0
        scoreSE = 0
        #check South
        for x in range(0, 5):
            for y in range (0,5):
                if (self.board[x][y] == aa or self.board[x+1][y] == aa or self.board[x+2][y] == aa or self.board[x+1][y+1] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x+1][y] == agent:
                    t += 1
                if self.board[x+2][y] == agent:
                    t += 1
                if self.board[x+1][y+1] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreS += t

        # check North (this is the T)
        for x in range(0,5):
            for y in range (1,6):
                if (self.board[x][y] == aa or self.board[x+1][y] == aa or self.board[x+2][y] == aa or self.board[x+1][y-1] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x+1][y] == agent:
                    t += 1
                if self.board[x+2][y] == agent:
                    t += 1
                if self.board[x+1][y-1] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreN += t

        # check West
        for x in range(0,6):
            for y in range (0,4):
                if (self.board[x][y] == aa or self.board[x][y+1] == aa or self.board[x][y+2] == aa or self.board[x+1][y+1] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x][y+1] == agent:
                    t += 1
                if self.board[x][y+2] == agent:
                    t += 1
                if self.board[x+1][y+1] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreW += t

        # check East
        for x in range(1,7):
            for y in range (0,4):
                if (self.board[x][y] == aa or self.board[x][y+1] == aa or self.board[x][y+2] == aa or self.board[x-1][y+1] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x][y+1] == agent:
                    t += 1
                if self.board[x][y+2] == agent:
                    t += 1
                if self.board[x-1][y+1] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreE += t

        # check NW
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == aa or self.board[x+1][y+1] == aa or self.board[x+2][y+2] == aa or self.board[x+2][y] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x+1][y+1] == agent:
                    t += 1
                if self.board[x+2][y+2] == agent:
                    t += 1
                if self.board[x+2][y] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreNW += t

        # check NE
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == aa or self.board[x][y+2] == aa or self.board[x+1][y+1] == aa or self.board[x+2][y] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x][y+2] == agent:
                    t += 1
                if self.board[x+1][y+1] == agent:
                    t += 1
                if self.board[x+2][y] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreNE += t

        # check SW
        for x in range(0,5):
            for y in range (2,6):
                if (self.board[x][y] == aa or self.board[x+1][y-1] == aa or self.board[x+2][y-2] == aa or self.board[x+2][y] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x+1][y-1] == agent:
                    t += 1
                if self.board[x+2][y-2] == agent:
                    t += 1
                if self.board[x+2][y] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreSW += t

        # check SE
        for x in range(0,5):
            for y in range (0,4):
                if (self.board[x][y] == aa or self.board[x+1][y+1] == aa or self.board[x+2][y+2] == aa or self.board[x][y+2] == aa):
                    continue
                t = 0
                if self.board[x][y] == agent:
                    t += 1
                if self.board[x+1][y+1] == agent:
                    t += 1
                if self.board[x+2][y+2] == agent:
                    t += 1
                if self.board[x][y+2] == agent:
                    t += 1
                t -= depth
                if t < 0:
                    t = 0
                scoreSE += t
        score = scoreN + scoreS + scoreE + scoreW + scoreNW + scoreNE + scoreSW + scoreSE
        if player != agent:
            score = -score

        print("Scored: " + str(score) + " for agent " + str(self.mapChar(agent)))
        return score

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
    turn = 0
    recursion = 0
    def __init__(self, agent, depthMax):
        self.agent = agent
        self.depthMax = depthMax

    def getNextAgent(self, agent):
        # Returns opposite agent
        if agent == 1:
            return 2
        else:
            return 1

    def minimax(self, agent, board):
        MinMax.turn += 1
        if MinMax.turn == 1:
            return 3
        return self.maxValue(board, 1, agent, -math.inf, math.inf)

    def maxValue(self, board, depth, agent, alpha, beta):
        MinMax.recursion += 1
        print("Rec: " + str(MinMax.recursion))
        if depth > self.depthMax or board.checkWin(1) or board.checkWin(1):
            print("Dead [" + str(depth) + "]")
            return board.evaluate(agent, depth)
        actions = board.getLegalActions()
        print("Will launch " + str(len(actions)))
        #if len(actions) == 0: return board.evaluate(agent, depth)
        maximum = -math.inf
        nextAgent = self.getNextAgent(agent)
        for action in actions:
            board.insertCoin(action, agent)
            value = self.minValue(board, depth+1, nextAgent, alpha, beta)
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
        MinMax.recursion += 1
        print("Rec: " + str(MinMax.recursion))
        if depth > self.depthMax or board.checkWin(1) or board.checkWin(1):
            print("Dead [" + str(depth) + "]")
            return board.evaluate(agent, depth)
        #print("Min [" + str(depth) + "]" )
        actions = board.getLegalActions()
        print("Will launch " + str(len(actions)))
        #if len(actions) == 0: return board.evaluate(agent, depth)
        minimum = math.inf
        nextAgent = self.getNextAgent(agent)
        for action in actions:
            board.insertCoin(action, agent)
            value = self.maxValue(board, depth+1, nextAgent, alpha, beta)
            board.removeCoin(action)
            if minimum > value:
                minimum = value

            if minimum < alpha:
                return minimum

            #beta = min(beta, minimum)
            if beta > minimum:
                beta = minimum

        return minimum
