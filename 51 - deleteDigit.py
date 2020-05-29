def deleteDigit(n):
    line = len(str(n))
    result = 0
    for i in range(line):
        word = str(n)[:i] + str(n)[i+1:]
        if result < int(word):
            result = int(word)
    return result
