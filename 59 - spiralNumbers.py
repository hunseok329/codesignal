def spiralNumbers(n):
    matrix = [[0 for col in range(n)]for row in range(n)]
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    direction = RIGHT
    x = 0
    y = 0
    for num in range(1, (n*n)+1):
        matrix[x][y] = num
        if direction == RIGHT:
            if y != n - 1 and matrix[x][y + 1] == 0:
                y += 1
            else:
                direction = DOWN
                x += 1
        elif direction == DOWN:
            if x != n - 1 and matrix[x + 1][y] == 0:
                x += 1
            else:
                direction = LEFT
                y -= 1
        elif direction == LEFT:
            if y != 0 and matrix[x][y - 1] == 0:
                y -= 1
            else:
                direction = UP
                x -= 1
        elif direction == UP:
            if x != 0 and matrix[x - 1][y] == 0:
                x -= 1
            else:
                direction = RIGHT
                y += 1
    return matrix
