def chessKnight(cell):
    moves = 0
    if ord(cell[0]) >= ord('c') and int(cell[1]) <= 7:
        moves += 1
    if ord(cell[0]) >= ord('b') and int(cell[1]) <= 6:
        moves += 1
    if ord(cell[0]) >= ord('c') and int(cell[1]) >= 2:
        moves += 1
    if ord(cell[0]) >= ord('b') and int(cell[1]) >= 3:
        moves += 1
    if ord(cell[0]) <= ord('g') and int(cell[1]) >= 3:
        moves += 1
    if ord(cell[0]) <= ord('f') and int(cell[1]) >= 2:
        moves += 1
    if ord(cell[0]) <= ord('f') and int(cell[1]) <= 7:
        moves += 1
    if ord(cell[0]) <= ord('g') and int(cell[1]) <= 6:
        moves += 1
    return moves
