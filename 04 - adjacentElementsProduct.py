def adjacentElementsProduct(inputArray):
    a = []
    b = len(inputArray)-1
    for i in range(0, b):
        a.append(inputArray[i]*inputArray[i+1])
    return max(a)