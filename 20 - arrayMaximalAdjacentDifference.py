def arrayMaximalAdjacentDifference(inputArray):
    result = []
    for i in range(len(inputArray)-1):
        result.append(abs(inputArray[i+1] - inputArray[i]))
    return max(result)