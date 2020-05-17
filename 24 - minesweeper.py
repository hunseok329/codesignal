def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    copy = []
    false = []
    for i in range(col + 2):
        false.append(False)
    copy.append(false)
    for i in range(row):
        matrix[i].insert(row+1, False)
        matrix[i].insert(0, False)
        copy.append(matrix[i])
    copy.append(false)

    mineList = []
    for i in range(row):
        mine = []
        for j in range(col):
            count = 0
            if copy[i+1][j+1] == True:
                count = -1
            for w in range(3):
                capy = copy[i+w][j:j+3]
                count += capy.count(True)
            mine.append(count)
        mineList.append(mine)
    return mineList
