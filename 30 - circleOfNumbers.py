def circleOfNumbers(n, firstNumber):
    half = n//2
    circle_1 = []
    circle_2 = []
    for num in range(half):
        circle_1.append(num)
    for num in range(half, n):
        circle_2.append(num)
    if firstNumber < half:
        return circle_2[firstNumber]
    else:
        return circle_1[firstNumber-half]
