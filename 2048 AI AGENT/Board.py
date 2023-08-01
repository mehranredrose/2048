from copy import deepcopy
from matrix_functions import generic_combine, generic_reverse, generic_stack, generic_transpose

class Board:

    def __init__(self, matrix):
        self.setMatrix(matrix)

    def setMatrix(self, matrix):
        self.matrix = deepcopy(matrix)

    def getMatrix(self):
        return deepcopy(self.matrix)

    def heuristic(self):

        gradients = [
            [[ 3,  2,  1,  0],[ 2,  1,  0, -1],[ 1,  0, -1, -2],[ 0, -1, -2, -3]],
            [[ 0,  1,  2,  3],[-1,  0,  1,  2],[-2, -1,  0,  1],[-3, -2, -1, -0]], 
            [[ 0, -1, -2, -3],[ 1,  0, -1, -2],[ 2,  1,  0, -1],[ 3,  2,  1,  0]], 
            [[-3, -2, -1,  0],[-2, -1,  0,  1],[-1,  0,  1,  2],[ 0,  1,  2,  3]]
            ]

        values = [0,0,0,0]

        for i in range(4):
            for x in range(4):
                for y in range(4):
                    values[i] += gradients[i][x][y]*(self.matrix[x][y])

        return max(values)

    def stack(self):
        temp_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    temp_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = temp_matrix



    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0

    def reverse(self):
        temp_matrix = []
        for i in range(4):
            temp_matrix.append([])
            for j in range(4):
                temp_matrix[i].append(self.matrix[i][3-j])
        self.matrix = temp_matrix

    def transpose(self):
        temp_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                temp_matrix[i][j] = self.matrix[j][i]
        self.matrix = temp_matrix

    def right_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1] and self.matrix[i][j] != 0:
                    return True
        temp_matrix = self.getMatrix()
        temp_matrix = generic_reverse(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_combine(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_reverse(temp_matrix)
        if temp_matrix == self.matrix:
            return False
        return True

    def left_move_exists(self):
        for i in range(4):
            for j in range(1,4):
                if self.matrix[i][j] == self.matrix[i][j-1] and self.matrix[i][j] != 0:
                    return True
        temp_matrix = self.getMatrix()
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_combine(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        if temp_matrix == self.matrix:
            return False
        return True

    def down_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j] and self.matrix[i][j] != 0:
                    return True
        temp_matrix = self.getMatrix()
        temp_matrix = generic_transpose(temp_matrix)
        temp_matrix = generic_reverse(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_combine(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_reverse(temp_matrix)
        temp_matrix = generic_transpose(temp_matrix)
        if temp_matrix == self.matrix:
            return False
        return True

    def up_move_exists(self):
        for i in range(1,4):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i-1][j] and self.matrix[i][j] != 0:
                    return True
        temp_matrix = self.getMatrix()
        temp_matrix = generic_transpose(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_combine(temp_matrix)
        temp_matrix = generic_stack(temp_matrix)
        temp_matrix = generic_transpose(temp_matrix)
        if temp_matrix == self.matrix:
            return False
        return True

    def getAvailableMovesForMax(self):
        moves = []
        if self.up_move_exists():
            moves.append(0)
        if self.down_move_exists():
            moves.append(1)
        if self.left_move_exists():
            moves.append(2)
        if self.right_move_exists():
            moves.append(3)
        return moves

    def getAvailableMovesForMin(self):
        places = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    places.append((i+1, j+1, 2))
                    places.append((i+1, j+1, 4))
        return places

    def getChildren(self, who):
        if who == "max":
            return self.getAvailableMovesForMax()
        elif who == "min":
            return self.getAvailableMovesForMin()

    def isTerminal(self, who):
        if who == "max":
            if self.up_move_exists():
                return False
            if self.down_move_exists():
                return False
            if self.left_move_exists():
                return False
            if self.right_move_exists():
                return False
            return True
        elif who == "min":
            for i in range(4):
                for j in range(4):
                    if self.matrix[i][j] == 0:
                        return False
            return True

    def isGameOver(self):
        return self.isTerminal("max")

    def left(self):
        if self.left_move_exists():
            self.stack()
            self.combine()
            self.stack()

    def right(self):
        if self.right_move_exists():
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.reverse()

    def up(self):
        if self.up_move_exists():
            self.transpose()
            self.stack()
            self.combine()
            self.stack()
            self.transpose()

    def down(self):
        if self.down_move_exists():
            self.transpose()
            self.reverse()
            self.stack()
            self.combine()
            self.stack()
            self.reverse()
            self.transpose()

    def move(self, moveCode):
        if moveCode == 0:
            self.up()
        elif moveCode == 1:
            self.down()
        elif moveCode == 2:
            self.left()
        else:
            self.right()

    def getMoveTo(self, child):
        if self.up_move_exists():
            g = Board(self.getMatrix())
            g.up()
            if g.matrix == child.matrix:
                return 0
        if self.down_move_exists():
            g = Board(self.getMatrix())
            g.down()
            if g.matrix == child.matrix:
                return 1
        if self.left_move_exists():
            g = Board(self.getMatrix())
            g.left()
            if g.matrix == child.matrix:
                return 2
        return 3