def absoluteValuesSumMinimization(a):
    result = []
    for num in a:
        absSum = 0
        for i in range(len(a)):
            absSum += abs(a[i]-num)
        result.append(absSum)
    index = result.index(min(result))
    return a[index]
