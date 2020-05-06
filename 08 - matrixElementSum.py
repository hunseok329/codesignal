def matrixElementsSum(matrix):
    result = 0
    for num in range(len(matrix)-1):
        for n in range(len(matrix[num])):
            if matrix[num][n] == 0:
                matrix[num+1][n] = 0

    for i in matrix:
        result += sum(i)
    return result