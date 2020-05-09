def palindromeRearranging(inputString):
    if len(inputString) == 0 or len(inputString) == 1:
        return True
    if len(inputString) % 2 == 0:
        result = 0
        for word in set(inputString):
            h = inputString.count(word)
            if h % 2 != 0:
                result += 1
        if result == 0:
            return True
        else:
            return False
    else:
        result = 0
        for word in set(inputString):
            h = inputString.count(word)
            if h % 2 != 0:
                result += 1
        if result >= 2:
            return False
        else:
            return True