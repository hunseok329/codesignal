def validTime(time):
    time = time.split(':')
    result = True
    for i, num in enumerate(time):
        if i == 0 and int(num) >= 24:
            result = False
        if i == 1 and int(num) >= 60:
            result = False
    return result
