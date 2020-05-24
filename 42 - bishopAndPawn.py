def bishopAndPawn(bishop, pawn):
    x = bishop[0]
    y = bishop[1]

    xp = pawn[0]
    yp = pawn[1]

    X = abs(ord(x) - ord(xp))
    Y = abs(int(y) - int(yp))
    return X == Y
