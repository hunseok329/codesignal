def allLongestStrings(inputArray):
    list = []
    result = []
    for word in inputArray:
        list.append(len(word))
    for word in inputArray:
        if max(list) == len(word):
            result.append(word)
    return result