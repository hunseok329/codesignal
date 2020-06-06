def sudoku(grid):
    for x in grid:
        if len(set(x)) != 9:
            return False

    y = []
    for num in range(9):
        for x in grid:
            y.append(x[num])
        if len(set(y)) != 9:
            return False

    for by in range(0, 9, 3):
        for bx in range(0, 9, 3):
            square = []
            for i in range(3):
                square += grid[by+i][bx:bx+3]
            if len(set(square)) != 9:
                return False
    return True
