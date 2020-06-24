def solution(board, moves):
    result = []
    count = 0
    for num in moves:
        depth = 0
        while depth < len(board):
            if board[depth][num-1] != 0:
                result.append(board[depth][num-1])
                board[depth][num-1] = 0
                break
            depth += 1
        if len(result) > 1:
            if result[-1] == result[-2]:
                del result[-1]
                del result[-1]
                count += 2
    return count
