def isBeautifulString(inputString):
    if 'a' not in inputString:
        return False
    if (ord(sorted(inputString)[-1]) - ord('a')) > len(inputString):
        return False
    sortList = sorted(set(inputString))
    count = inputString.count('a')
    for word in sortList:
        if count >= inputString.count(word):
            count = inputString.count(word)
        else:
            return False
    return True
