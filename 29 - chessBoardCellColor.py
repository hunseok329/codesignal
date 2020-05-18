def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1])) % 2 == 0
