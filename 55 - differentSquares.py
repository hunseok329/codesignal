def differentSquares(matrix):
    result = []
    x = len(matrix[0])
    y = len(matrix)
    for i in range(y - 1):
        for j in range(x - 1):
            pick = matrix[i][j:j+2] + matrix[i+1][j:j+2]
            if pick in result:
                continue
            else:
                result.append(pick)
    return len(result)
