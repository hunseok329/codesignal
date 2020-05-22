def firstDigit(inputString):
    for i in inputString:
        try:
            number = int(i)
            return i
        except ValueError:
            continue
