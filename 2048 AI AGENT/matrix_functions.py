# General matrix manipulation functions to help simulate a move

def generic_stack(matrix):
    temp_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        fill_position = 0
        for j in range(4):
            if matrix[i][j] != 0:
                temp_matrix[i][fill_position] = matrix[i][j]
                fill_position += 1
    return temp_matrix

def generic_combine(matrix):
    for i in range(4):
        for j in range(3):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j+1]:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
    return matrix

def generic_reverse(matrix):
    temp_matrix = []
    for i in range(4):
        temp_matrix.append([])
        for j in range(4):
            temp_matrix[i].append(matrix[i][3-j])
    return temp_matrix

def generic_transpose(matrix):
    temp_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp_matrix[i][j] = matrix[j][i]
    return temp_matrix