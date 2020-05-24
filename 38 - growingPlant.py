def growingPlant(upSpeed, downSpeed, desiredHeight):
    result = 0
    count = 0
    while True:
        result += upSpeed
        count += 1
        if result >= desiredHeight:
            return count
        result -= downSpeed
    return count
