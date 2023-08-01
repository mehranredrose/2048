from Board import Board
from sys import maxsize

def maximize(state, a, b, d):
    maxChild, maxEval = None, -1

    if d == 0 or state.isTerminal("max"):
        return None, state.heuristic()
    
    d -= 1
    
    for child in state.getChildren("max"):
        board = Board(state.getMatrix())
        board.move(child)
        _, evaluation = minimize(board, a, b, d)
        if evaluation > maxEval:
            maxChild, maxEval = board, evaluation
        if maxEval >= b:
            break
        if maxEval > a:
            a = maxEval

    return maxChild, maxEval

def minimize(state, a, b, d):
    minChild, minEval = None, maxsize

    if d == 0 or state.isTerminal("min"):
        return None, state.heuristic()

    d -= 1
    
    for child in state.getChildren("min"):
        board = Board(state.getMatrix())
        board.matrix[child[0]-1][child[1]-1] = child[2]
        _, evaluation = maximize(board, a, b, d)
        if evaluation < minEval:
            minChild, minEval = board, evaluation
        if minEval <= a:
            break
        if minEval < b:
            b = minEval

    return minChild, minEval

def getBestMove(board, depth):
    child, _ = maximize(Board(board.getMatrix()), -1, maxsize, depth)
    return board.getMoveTo(child)