def extractEachKth(inputArray, k):
    result = []
    for index, number in enumerate(inputArray):
        if (index+1) % k != 0:
            result.append(number)
    return result
