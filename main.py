def maxValue(gameState,depth,agent,alpha,beta):
    if terminal(gameState,depth):
        return evaluate(gameState)

    maximum = float("-inf")
    nextAgent = getNextAgent(gameState,agent)

    for action in gameState.getLegalActions(agent):
        successor = gameState.generateSuccessor(agent, action)
        value = minValue(successor,depth,nextAgent,alpha,beta)

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


def minValue(gameState,depth,agent,alpha,beta):
    if terminal(gameState,depth):
        return evaluate(gameState)

    minimum = float("inf")
    nextAgent = getNextAgent(gameState,agent)


    for action in gameState.getLegalActions(agent):
        successor = gameState.generateSuccessor(agent, action)
        if nextAgent == index:
            minimum = min(minimum,maxValue(successor,depth+1,nextAgent,alpha,beta))
        else:
            minimum = min(minimum,minValue(successor,depth,nextAgent,alpha,beta))

        if minimum < alpha:
            return minimum

        beta = min(beta, minimum)

    return minimum
